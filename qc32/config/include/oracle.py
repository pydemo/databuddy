#__builtin__ args
import sys
from pprint import pprint
from common.v101.base import base 
import re, types, os, codecs
from subprocess import Popen, PIPE,STDOUT

e=sys.exit
#
# Define your custom SQL*Loader config
#	
class target(base):
	"""target Oracle methods"""
	def __init__(self,datadir,login,conf,db):
		self.datadir=datadir
		self.login=login
		self.conf=conf
		self.db=db
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir)		
	def get_load_config(self, db_loader_loc,shard_name, row_from, row_to,ctlfn,outfn, datadir):
		dpl_columnarrayrows=10000
		dpl_streamsize=500000
		dpl_readsize=200000
		if_dpl_parallel='TRUE'
		dpl_bindsize=200000
		dpl_skip_index_maintenance='TRUE'
		dpl_skip_unusable_indexes='TRUE'
		if_direct='TRUE'
		loader_errors=10
		ptn=''
		sptn=''
		userid = args.to_db
		#check if url connect
		c,sid = args.to_db.split('@')
		if sid.strip().startswith("'(DESCRIPTION"):
			u,p=c.split('/')
			userid='%s@\"%s\"/%s' % (u,sid.strip("'").replace('(',r'\(').replace(')',r'\)'),p)
		
		loadConf=[db_loader_loc, 
		'control=%s' % ctlfn, 
		'userid=%s' % userid, #args.to_db,
		'DATA=%s' % outfn,
		'COLUMNARRAYROWS=%s' % dpl_columnarrayrows,
		'STREAMSIZE=%s' % dpl_streamsize,'READSIZE=%s' % dpl_readsize,
		'PARALLEL=%s' % if_dpl_parallel,
		'BINDSIZE=%s' % dpl_bindsize, 
		#'UNRECOVERABLE=Y', 
		'SKIP_INDEX_MAINTENANCE=%s' % dpl_skip_index_maintenance, 'SKIP_UNUSABLE_INDEXES=%s' % dpl_skip_unusable_indexes,
		'DIRECT=%s' % if_direct, 	
		'MULTITHREADING=TRUE', 
		#'EXTERNAL_TABLE=EXECUTE',
		'LOG=%s/sqlloader/%s%s_%s.log' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name), 
		'BAD=%s/sqlloader/%s%s_%s.bad' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name),
		'DISCARD=%s/sqlloader/%s%s_%s.dsc' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name),				
		'ERRORS=%s' % loader_errors]
		if row_from:
			loadConf.append('SKIP=%s' % (row_from-1))
		if row_to:
			loadConf.append('LOAD=%s' % (row_to-row_from))
			
		#pprint(loadConf)
		#e(0)
		
		return loadConf	
		
	def get_table_columns(self,  tab_name):
		if self.tab_cols.has_key(tab_name):
			return self.tab_cols[tab_name]
		else:
			assert len(tab_name.upper().split('.'))==2, 'Table format: SCHEMA.TABLE'
			qry="""
			set pagesize 0 feedback off TIMING OFF
			SELECT COLUMN_NAME||':'||DATA_LENGTH||':'||DATA_TYPE
			FROM ALL_TAB_COLUMNS WHERE OWNER=UPPER('%s') AND TABLE_NAME=UPPER('%s')
			ORDER BY COLUMN_ID;
			exit;
			""" % tuple(tab_name.upper().split('.'))
			#print qry
			cqfn=self.save_qry('get_table_columns',qry)
			regexp=re.compile(r'(.*)')
			(r_int, status,err)=self.do_query(self.login, query=None,query_file=cqfn,regexp=regexp)
			assert r_int, 'Table %s does not exists in %s.' % (tab_name, self.login.split('@')[1])
			#pprint(r_int)		
			assert not status, 'Cannot fetch table columns (%s)' % tab_name
			self.tab_cols[tab_name] = (r_int, map(self.coldef, r_int))
			return self.tab_cols[tab_name]
	def save_ctl(self,  to_table,shard):
		ptn=''
		sptn=''
		cols = self.get_table_columns(to_table)
		#print cols
		dpl_mode='APPEND'
		line_term=''
		ctl=self.get_ctl(to_table,cols,dpl_mode,(line_term,'|'))

		ctlfn= '%s/%s%s_Shard-%s.ctl' % (self.ctldir,to_table, "%s%s" % (ptn,sptn),shard)


		f = codecs.open(ctlfn, 'w',"utf-8")
		status = f.write(unicode(ctl))

		if status!= None:
			self._logger.error('Cannot write to %s.' % ctlfn)
		f.close()
		return 	ctlfn	

	def get_ctl(self,  to_tab, r_int, dpl_mode, term):
		(line_term,field_term) =term
		part = ''
		#pprint(r_int)
		unrec = 'UNRECOVERABLE'	#INFILE '-' "str '%s\n'"			
		tmpl="""%s
	LOAD DATA
	%s
	INTO TABLE %s %s
	FIELDS TERMINATED BY '%s'
	TRAILING NULLCOLS
	(%s)""" % (unrec,dpl_mode,to_tab, part, field_term, ','.join(r_int[1]))
		#pprint(tmpl)
		#pprint(r_int)
		#sys.exit(1)
		return tmpl	
	def coldef (self,x): 
		#pprint(x)
		(colname, colsize, coltype)= x[0].split(':')
		#print x, int(colsize), int(colsize)>265
		if colsize:
			if int(colsize)>5000:
				#print x, '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
				#row = x.split(':')

				return '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
			if coltype in ('DATE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_date_format)
			if coltype in ('TIMESTAMP'):
				return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_format)
			if coltype in ('TIMESTAMP WITH TIMEZONE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_tz_format)
					
		return colname			
	def get_db_client_dbshell(self):
		assert self.args.target_client_home, 'self.args.target_client_home is not set'
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(self.conf.dbtools['DBSHELL'][self.db])
		if self.args.target_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=self.conf.dbtools['DBSHELL'][self.db]
			print self.db_client_dbshell,self.db
			print self.args.target_client_home
			e(0)
			
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %s' % loader)	
		return self.db_client_dbshell		
	def do_query(self,login, query, query_file=None, regexp=None, grp=None, spset=''):
		status=0
		out=[]
		assert  len(login)>0, 'Default login is not set.'
		show=False
		if type(login) == types.TupleType:
			to_tab=login[1]
			login=login[0]
		q=''
		opt=''
		db_client_dbshell= self.get_db_client_dbshell()		
		assert os.path.isfile(db_client_dbshell), 'Oracle sqlplus.exe does not exists at %s.' % db_client_dbshell
		if query_file:
			q = "%s\n%s\n@%s" % ( spset,opt,query_file)			
			assert os.path.isfile(query_file), 'Query file does not exists!'
		else:		
			q = "%s%s" % ( opt,query)
			
		
		cfg=[ db_client_dbshell,"-S", login,r'@%s' %  query_file]

		if self.args.nls_timestamp_format:
			os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
		else:
			#print '2'
			os.environ['NLS_TIMESTAMP_FORMAT']=''
		#print cfg
		p = Popen(cfg,  stdout=PIPE,stderr=PIPE, shell=True)
		output, err = p.communicate()
		#print output, err
		if err:
			self.log.err(err)
		status=p.wait()	
		for o in output.split(os.linesep):
			if o.strip():
				if regexp:
					m = re.match(regexp, o.strip()) 
					#print m
					if m:
						if grp:
							out.append(m.group(grp).strip())
						else:
							groups=m.groups()
							if groups:
								out.append(groups)
				else:
					
					out.append(output.strip())



		return (out,status,err)	