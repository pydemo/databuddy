#__builtin__ args
import sys
from pprint import pprint
from common.v101.base import base 
import re, types, os, codecs
from subprocess import Popen, PIPE,STDOUT
import yaml
e=sys.exit

class common(base):
	"""Common Oracle methods"""
	def __init__(self,datadir,login,conf):
		self.datadir=datadir
		self.login=login
		self.conf=conf
		#self.db=db
		self.args=conf.args
	def get_table_columns(self,  tab_name):
		if self.tab_cols.has_key(tab_name):
			return self.tab_cols[tab_name]
		else:
			print tab_name
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
	def do_query(self,login, query, query_file=None, regexp=None, grp=None, spset='', qname=None):
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
			#q = "%s\n%s\n@%s" % ( spset,opt,query_file)			
			assert os.path.isfile(query_file), 'Query file does not exists!'
			
		else:		
			#print self.datadir
			q = "%s\n%s\n%s\nexit;" % ( spset,opt, query)
			assert qname, 'query name "qname" is not set'
			query_file=self.save_qry(qname,q)
			#print query_file
			#q = "%s%s" % ( opt,query)
			#cfg=[ db_client_dbshell, login]
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
			#print o
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
	def coldef (self,x): 
		#pprint(x)
		(colname, colsize, coltype)= x[0].split(':')
		#print x, int(colsize), int(colsize)>265
		if colsize:
			if int(colsize)>255:
				#print x, '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
				#row = x.split(':')
				if coltype in ('VARCHAR2'):
					return '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
				if coltype in ('CHAR'):
					return '%s filler CHAR(%s)' % (colname,colsize)				
			if coltype in ('DATE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_date_format)
			if coltype in ('TIMESTAMP'):
				return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_format)
			if coltype in ('TIMESTAMP WITH TIMEZONE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_tz_format)
					
		return colname			
class source(common):
	"""Source Oracle methods"""
	def __init__(self,datadir,login,conf,db,from_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		#self.conf=conf
		self.db=db
		self.from_table=from_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
	def get_db_client_dbshell(self):
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(self.conf.dbtools['DBSHELL'][self.db])
		if self.args.source_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.args.source_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=self.conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_dbshell
	
#
# Define your custom SQL*Loader config
#	
class target(common):
	"""Target Oracle methods"""
	def __init__(self,datadir,login,conf,db,to_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		#self.conf=conf
		self.db=db.upper()
		self.to_table=to_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir)		
	def get_load_config(self, db_loader_loc,shard_name, row_from, row_to,ctlfn,outfn, datadir):
		to_db=self.args.copy_vector.split('2')[1].upper()
		loader_profile= self.conf.dlp[to_db].strip('"')
		if hasattr(self.args, 'loader_profile') and self.args.loader_profile:
			print 'using non-default loader profile'
			loader_profile=self.args.loader_profile.strip('"')
		assert os.path.isfile(loader_profile), 'Loader profile\n%s\ndoes not exists.' % loader_profile
			
		loader={}
		with open(loader_profile, 'r') as f:
			loader = yaml.load(f)

		loader_args= ['%s=%s' % (x,loader[x].strip().strip(' ')) for x in loader]
		loader_errors=10
		ptn=''
		sptn=''
		userid = self.args.to_db
		#check if url connect
		c,sid = self.args.to_db.split('@')
		if sid.strip().startswith("'(DESCRIPTION"):
			u,p=c.split('/')
			userid='%s@\"%s\"/%s' % (u,sid.strip("'").replace('(',r'\(').replace(')',r'\)'),p)
		
		loadConf=[db_loader_loc, 
		'control="%s"' % ctlfn, 
		'userid=%s' % userid, #args.to_db,
		'DATA="%s"' % outfn,
		#'EXTERNAL_TABLE=EXECUTE', %s/sqlloader/%s%s_%s.log
		'LOG=%s' % os.path.join(datadir,'sqlloader','%s%s_%s.log' % (self.args.to_table, "%s%s" % (ptn,sptn),shard_name)), 
		'BAD=%s' % os.path.join(datadir,'sqlloader','%s%s_%s.bad' % (self.args.to_table, "%s%s" % (ptn,sptn),shard_name)),
		'DISCARD=%s' % os.path.join(datadir,'sqlloader','%s%s_%s.dsc' % (self.args.to_table, "%s%s" % (ptn,sptn),shard_name))
		] + loader_args
		if row_from:
			loadConf.append('SKIP=%s' % (row_from-1))
		if row_to:
			loadConf.append('LOAD=%s' % (row_to-row_from))
			
		#pprint(loadConf)
		#e(0)
		
		return loadConf	
		

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
	def load_data(self,logger,loadConf,outfn,shard):
		
		out=[]
		err=[]
		if 1:
			if self.args.nls_date_format:
				os.environ['NLS_DATE_FORMAT'] = self.args.nls_date_format
			#else:
				#os.environ['NLS_DATE_FORMAT'] = ''
			if self.args.nls_timestamp_format:
				os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
			if self.args.nls_timestamp_format:
				os.environ['NLS_TIMESTAMP_TZ_FORMAT'] = self.args.nls_timestamp_tz_format				

		
		#pprint(loadConf)
		p3 = Popen(loadConf, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output=' '
		while output:
			output = p3.stdout.readline()
			#print output
			out.append(output)
		status=p3.wait()
		if status==0:
			logger.info('SQL*Loader status =%s' % status)
		if status!=0:
			logger.error('SQL*Loader status =%s' % status)
		if 1:
			
			error=' '
			while error:
				error = p3.stderr.readline()
				print error
				err.append(error)
		status = p3.wait()
		#print 'shard',shard
		ins_cnt = self.get_inserted_count(shard)
		#print ins_cnt
		#sys.exit(0)
		#return (out,status,err)
		return (out,status,err,ins_cnt)	
	def get_inserted_count(self,shard):
		ptn=''
		sptn=''
		
		logfn='%s\\%s%s_Shard-%s.log' % (self.ctldir,self.to_table, "%s%s" % (ptn,sptn),shard)

		rows_copied=-1
		#print logfn
		if not os.path.isfile(logfn):
			print 'Log file for shard "%s" is missing.' % shard
			#self.log.error('Log file for shard %d is missing.' % shard)
		else:
			shl=open(logfn, 'r').read()
			#print shl
			r=re.compile(r'\s+(\d+) Rows successfully loaded\.')

			g=re.search(r,shl)
			#print g.groups()
			if g:
				rows_copied=int(g.groups()[0])
				#rows_total +=rows_copied
				#print rows_total
		#print rows_copied
		return rows_copied		
