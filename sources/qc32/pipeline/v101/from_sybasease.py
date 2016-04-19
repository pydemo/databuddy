import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_sybasease import SybaseASE
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
import shlex
class FromSybaseASE(SybaseASE):
	"""SybaseASE db"""
	def __init__(self,parent,log,login,query_sql_file,datadir,args):
		SybaseASE.__init__(self,log,login,datadir,args) 
		self.query_sql_file=query_sql_file
		if 0:
			self.log=log
			self.login=login
			
			self.field_term=args.field_term
			#self.ss_user=ss_user
			#self.ss_passwd=ss_passwd
			#self.ss_db_name=ss_db_name
			#self.ss_db_server=ss_db_server
			self.datadir=datadir
			self.args=args
			self.tab_cols={}
	def print_copy_details(self):		
		print """		
	From Sybase ASE:	
		from db: %s
		query file: %s
		""" % ('%s/%s/%s' % (self.args.from_user,self.args.from_db_name,self.args.from_db_server),self.args.query_sql_file)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['SPOOLER']['SYANY'])
		if self.args.source_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.source_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['SPOOLER']['SYANY']
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc
		
	def get_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server]
		connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.from_user,self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		spConf=[ '"%s"' % db_client_loc ,'-nogui','-c', connect_str, '-onerror', 'exit']
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf
	def get_sharded_sql(self,sql_query,rowid_from,rowid_to, rc,outfn):
		sql_query=sql_query.strip().strip(';')
		from_to=''
		if not rowid_from and not rowid_to:
			from_to=''			
		else:
			if not rowid_from:		
				from_to=' TOP %s ' % (rowid_to)
			else:			
				if rowid_to: 
					from_to=' TOP %s START AT %s ' % (rowid_to+1, rowid_from-1)
				else:
					from_to=' TOP %s START AT %s' % (rc-rowid_from+1,  rowid_from-1)
		hdr=''
		if self.args.header:
			hdr=' WITH COLUMN NAMES'
		out=r"""SELECT %s * FROM (%s) t ORDER BY 1; 
OUTPUT TO '%s' FORMAT ASCII DELIMITED BY '%s' QUOTE ''%s;
""" % (from_to,sql_query.strip().strip(';'),os.path.normpath(outfn).replace("\\", "\\\\"),self.args.field_term, hdr)	
		#print out
		#sys.exit(0)
		return out
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;
	def get_firstrow(self):
		return 0
	def set_payload(self, num_of_shards):
	
		sql_query =''
		assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file

		f = open(self.query_sql_file, 'r')

		sql_query= f.read()
		#sql_query=sql_query.replace('"',"'")
		#print sql_query
		f.close()
		#print sql_query
		#sys.exit(0)
		assert sql_query, 'Query is not set'	
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)', re.M|re.I)
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		lqfn = self.save_qry('source_row_count',q)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		#regexp=re.compile(r'^(\d+) row', re.M|re.I)
		
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, None,regexp=regexp,query_file=lqfn, field_term=fterm)
		except WindowsError, value:
			err= value.args 
			self.log.error( 'ERROR '*5)
			self.log.error( 'ERROR '*5)
			
			if 'Warning: Using a password on the' in err:
				self.log.warn(sql_err)
			else:
				self.log.error( err)
				
			self.log.error( 'ERROR '*5)
			self.log.error( 'ERROR '*5)
			raise

		#assert not err, 
		#print '@'*20
		#print r
		#sys.exit(0)
		assert len(r)==1, 'Cannot get query recordcount.'
		rc=int(r[0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert rc, 'Source table is empty.'
		assert rc>0, 'Cannot estimate query record count. Exiting...'
		if 0:
			self.log.info('Fetching query columns.')
			header=self.get_query_columns(sql_query)
			
			#header=self.get_SS_query_columns(self.log,self.login,sql_query)
			
			#print header
			#sys.exit(1)
			self.log.info('Got %d columns.' % len(header))
		else:
			header =''
		cols=[]			
		for h in header:
			#print h
			#self.log.info('%s %s(%s)' % tuple(h[:3]))	
			cols.append(h)
		#print cols
		header_line= self.field_term.join(cols)	
		shard_size=rc/num_of_shards
		#print shard_size

		assert shard_size>1 or num_of_shards==1, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,rc)
	
		shards=[]
		for s in range(num_of_shards):
			if s==(num_of_shards-1):
				shards.append([s,shard_size*s,0,0])
			else:
				if s==0:
					shards.append([s,0,shard_size-1,0])
				else:
					shards.append([s,shard_size*s,shard_size-1,0])
		from_pld=[]	
		
		#if num_of_shards>1:
		#	self.log.info('Sharding query by %s' % cols[0])
		for i in range(len(shards)):
			#print i
			#print shards[i]
			(sid,rowid_from, rowid_to, _) = shards[i]
			if 1:
				#rowid_from=i
				#rowid_to = i+1
				#qry= sql_query
				outfn=self.get_outfn(i)
				#if 1: #num_of_shards>1:
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,rc,outfn)
				#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_query_%s.sql' % (sqdir,i)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,header_line,sqfn))
				#from_pld.append((sqfn,header_line))
				#print ("Shard-%d" % i,rowid_from,rowid_to,conf)
				#print skip
				#globalStatus[i]=(99, None)
		#pprint (from_pld)
		#sys.exit(1)
		return (shards,from_pld) 	
	def get_inserted_count(self,cnt):
		return cnt
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, self.get_firstrow(),0)		
	def spool_source_data(self,outfn, spConf, env):
		(shard_name,from_pld,to_pld)=env
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#(rowid_from,rowid_to,ctlfn,from_db,from_table,cols_from)=from_pld
		#shard=shard_name.split('-')[1]
		#outfn='%s\\shard_%s.data' % (self.datadir,shard)
		#outfn=r'C:\Python27\ora2ss_data_pipe\data\\shard_%s.data' % shard
		#print outfn
		#sys.exit(0)
		#outf=open(outfn, "w")
		#pprint (spConf)
		#print outfn
		#pprint( spConf)
		#
		#print sqfn
		#sys.exit(0)
		if sqfn:
			spConf=spConf+ [r'"%s"' % sqfn]	
		cmd=  ' '.join(spConf)
		#print cmd
		#sys.exit(1)			
		
		spConf=shlex.split(cmd)
		p2 = Popen(spConf,stdin=PIPE,  stdout=PIPE , shell=True )# '-S',  stdin=p1.stdout,
		output, err = p2.communicate()
		#print output 
		regexp=re.compile(r'(\d+) rows written to', re.M|re.I)
		grp=None
		out=[]
		status=p2.wait()
		for o in output.split('\r'):
		#while output:
			#output = p2.stdout.readline()
			#pprint(o)
			#if o.strip():					
			#	logger.info( output.strip())
			if 1:
				if regexp:
					#print regexp, o
					#pprint(dir(re))
					m = re.match(regexp, o.strip()) 
					#print m
					if m:
						if grp:
							out.append(m.group(grp))
						else:
							groups=m.groups()
							if groups:
								if groups[0]:
									#print 'groups', groups
									out.append(groups[0])
											
		#print out
		#sys.exit(0)
		#print err
		cnt=int(out[0])
		if err:
			self.log.error(err)
		#
		
		return (cnt,status)
	
