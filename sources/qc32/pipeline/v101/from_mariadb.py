import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_mariadb import MariaDB
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf

class FromMariaDB(MariaDB):
	"""MariaDB db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(self.args.from_user, self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
	
		MariaDB.__init__(self,log,self.login,datadir,self.args) 
		self.log=log
		#self.login=login
		self.query_sql_file=self.args.query_sql_file
		self.field_term=args.field_term
		self.db=db
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		self.Q, self.T, self.P, self.SP =(False, False, False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
			if self.args.from_partition:
				assert not self.args.from_sub_partition, 'Set Partition or Subpartition but not both.'
				self.P=True
			elif self.args.from_sub_partition:				
				self.SP=True
		elif self.args.query_sql_file:
			assert not self.args.from_partition, 'You cannot use partition "%s" (--from_partition) in QUERY mode.' % self.args.from_partition
			assert not self.args.from_sub_partition, 'You cannot use sub-partition "%s" (--from_partition) in QUERY mode.' % self.args.from_sub_partition
			assert self.args.query_sql_file, 'Data source should be Table or Query. None is set.'
			assert not self.args.from_partition, 'Set Query or Table/Partition but not both.'
			self.args.num_of_shards, 'Number of shards is not set'
			#assert int(self.args.num_of_shards) == 1, 'Cannot shard in QUERY mode. Set num_of_shards=1.'
			self.Q=True
			assert os.path.isfile(self.args.query_sql_file)
			
			self.from_query=open(self.args.query_sql_file).read()
		else:
			assert not self.args.from_partition, 'Source table name (--from_table) is not set for partition "%s".' % self.args.from_partition
			assert not self.args.from_sub_partition, 'Source table name (--from_table) is not set for subpartition "%s".' % self.args.from_sub_partition
			
	def print_copy_details(self):		
		print """		
	From %s:	
		from db: %s
		query file: %s
		""" % (conf.dbs[self.db], '%s/%s/%s' % (self.args.from_user,self.args.from_db_name,self.args.from_db_server),self.args.query_sql_file)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['SPOOLER'][self.db])
		if self.args.source_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.source_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['SPOOLER'][self.db]
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc
	def get_db_client_dbshell(self):
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(conf.dbtools['DBSHELL'][self.db])
		if self.args.source_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.args.source_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_dbshell
	def detect_partition(self):
		self.log.info('Verifying partition...')
		#qry="SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_PARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('%s') AND UPPER(partition_name)=UPPER('%s');" % (self.args.from_table,self.args.from_partition)		
		#print self.args.from_table
		#print self.args.from_partition
		self.args.from_table.split
		(schema, table)=self.args.from_table.split('.')
		qry="select TABLE_SCHEMA,TABLE_NAME, PARTITION_NAME from information_schema.PARTITIONS  where TABLE_SCHEMA = '%s' and TABLE_NAME='%s' and partition_name='%s' \G;" % (schema, table,self.args.from_partition)
		#print qry
		sqfn=self.save_qry('get_part_info_%s.%s' % (self.args.from_table,self.args.from_partition),qry)	
		tab=''.join([r'\\%s' %i for i in self.args.from_table.split('.')[1]])
		part=''.join([r'\\%s' %i for i in self.args.from_partition])
		regstr = r'\s?(TABLE_NAME|PARTITION_NAME)\:\s+(.*|.*)'
		regexp=re.compile(regstr)			
		(r_int, status,err)=self.do_query(self.log,self.login, query=None,regexp=regexp,query_file=sqfn)
		#print r_int, status
		assert r_int and r_int[0] , 'Partition "%s" does not exists in table %s' % (self.args.from_partition,self.args.from_table)
		pdict = {v[0]:v[1] for v in r_int}
		assert pdict.has_key('TABLE_NAME') , 'TABLE_NAME:Partition "%s" does not exists in table %s' % (self.args.from_partition,self.args.from_table)
		assert pdict.has_key('PARTITION_NAME') , 'PARTITION_NAME: Partition "%s" does not exists in table %s' % (self.args.from_partition,self.args.from_table)
		self.log.info('Check OK. Partition "%s" exists in table "%s".' % (self.args.from_partition,self.args.from_table))
		#print pdict
		#sys.exit(1)
		
		self.log.info('Done.')		
	def detect_sub_partition(self):
		self.log.info('Verifying partition...')
		#qry="SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_PARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('%s') AND UPPER(partition_name)=UPPER('%s');" % (self.args.from_table,self.args.from_partition)		
		
		#print self.args.from_table
		#print self.args.from_sub_partition
		self.args.from_table.split
		(schema, table)=self.args.from_table.split('.')
		qry="select TABLE_SCHEMA,TABLE_NAME, SUBPARTITION_NAME from information_schema.PARTITIONS  where TABLE_SCHEMA = '%s' and TABLE_NAME='%s' and subpartition_name='%s' \G;" % (schema, table,self.args.from_sub_partition)
		#print qry
		sqfn=self.save_qry('get_part_info_%s.%s' % (self.args.from_table,self.args.from_sub_partition),qry)	
		tab=''.join([r'\\%s' %i for i in self.args.from_table.split('.')[1]])
		part=''.join([r'\\%s' %i for i in self.args.from_sub_partition])
		regstr = r'\s?(TABLE_NAME|SUBPARTITION_NAME)\:\s+(.*|.*)'
		regexp=re.compile(regstr)			
		(r_int, status,err)=self.do_query(self.log,self.login, query=None,regexp=regexp,query_file=sqfn)
		#print r_int, status
		assert r_int and r_int[0] , 'Partition "%s" does not exists in table %s' % (self.args.from_sub_partition,self.args.from_table)
		pdict = {v[0]:v[1] for v in r_int}
		assert pdict.has_key('TABLE_NAME') , 'TABLE_NAME:Partition "%s" does not exists in table %s' % (self.args.from_sub_partition,self.args.from_table)
		assert pdict.has_key('SUBPARTITION_NAME') , 'SUBPARTITION_NAME: Partition "%s" does not exists in table %s' % (self.args.from_sub_partition,self.args.from_table)
		self.log.info('Check OK. Partition "%s" exists in table "%s".' % (self.args.from_sub_partition,self.args.from_table))
		#print pdict	

		#sys.exit(1)
	def get_sharded_sql(self,sql_query,rowid_from,rowid_to, rc,outfn):
		sql_query=sql_query.strip().strip(';')
		if not rowid_from and not rowid_to:
			qry=sql_query
		else:
			if not rowid_from:		
				qry='%s LIMIT %s' % (sql_query, rowid_to)
			else:			
				if rowid_to:
					qry='%s LIMIT %s,%s' % (sql_query, rowid_from-1,rowid_to+1)
				else:
					qry='%s LIMIT %s,%s' % (sql_query, rowid_from-1,rc-rowid_from+1)
		out=r"""%s
INTO OUTFILE '%s'
FIELDS ENCLOSED BY '' TERMINATED BY '%s' ESCAPED BY ''
LINES TERMINATED BY '\r\n';
SELECT ROW_COUNT();
""" % (qry,os.path.normpath(outfn).replace("\\", "\\\\"),self.args.field_term)
				
		return out
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;
	def get_firstrow(self):
		return 0
	def set_part_table_payload(self, num_of_shards):
		print ''
		sql_query =''
		(table, partitioned) = self.get_table_info()
		#print table, partitioned
		#sys.exit(0)
		assert partitioned , 'Table table %s is not partitioned.\n Fix: Unset --from_partition' % self.args.from_table
		#sys.exit(1)
		#if self.P:
		#check if partition exists
		self.detect_partition()
		#sys.exit(1)
		sql_query= 'SELECT * FROM %s PARTITION(%s)' % (self.args.from_table, self.args.from_partition)
		assert sql_query, 'Query is not set'
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, q,0,regexp,field_term=fterm)
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
		assert len(r[0])==1, 'Cannot get query recordcount.'
		self.rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert self.rc, 'Source table is empty.'
		assert self.rc>0, 'Cannot get source record count. Exiting...'
		self.log.info(self.rc)
		self.log.info('Done.')
		#self.log.info('Fetching query columns.')
		self.log.info('Fetching source column names...')
		header=self.get_query_columns(sql_query)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		self.log.info('Got %d columns.' % len(header))
		self.log.info('Done.')
		cols=[]			
		for h in header:
			#print h
			#self.log.info('%s %s(%s)' % tuple(h[:3]))	
			cols.append(h)
		#print cols
		header_line= self.field_term.join(cols)	
		shard_size=self.rc/num_of_shards
		#print shard_size

		assert shard_size>1 or num_of_shards==1, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,self.rc)
	
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
		
		if num_of_shards>1:
			self.log.info('Sharding query by %s' % cols[0])
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
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,self.rc,outfn)
				#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\query_%s.sql' % (sqdir,i)
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
	def set_subpart_table_payload(self, num_of_shards):
		print ''
		sql_query =''
		(table, partitioned) = self.get_table_info()
		#print table, partitioned
		#sys.exit(0)
		assert partitioned , 'Table table %s is not partitioned.\n Fix: Unset --from_partition' % self.args.from_table
		#sys.exit(1)
		#if self.P:
		#check if partition exists
		self.detect_sub_partition()
		#sys.exit(1)
		sql_query= 'SELECT * FROM %s PARTITION(%s)' % (self.args.from_table, self.args.from_sub_partition)
		assert sql_query, 'Query is not set'
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, q,0,regexp,field_term=fterm)
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
		assert len(r[0])==1, 'Cannot get query recordcount.'
		self.rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert self.rc, 'Source table is empty.'
		assert self.rc>0, 'Cannot get source record count. Exiting...'
		self.log.info(self.rc)
		self.log.info('Done.')
		#self.log.info('Fetching query columns.')
		self.log.info('Fetching source column names...')
		header=self.get_query_columns(sql_query)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		self.log.info('Got %d columns.' % len(header))
		self.log.info('Done.')
		cols=[]			
		for h in header:
			#print h
			#self.log.info('%s %s(%s)' % tuple(h[:3]))	
			cols.append(h)
		#print cols
		header_line= self.field_term.join(cols)	
		shard_size=self.rc/num_of_shards
		#print shard_size

		assert shard_size>1 or num_of_shards==1, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,self.rc)
	
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
		
		if num_of_shards>1:
			self.log.info('Sharding query by %s' % cols[0])
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
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,self.rc,outfn)
				#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\query_%s.sql' % (sqdir,i)
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
	def get_table_info(self):
		self.log.info('Fetching table info...')
		#self.args.from_table='test.Persons_partitioned'
		qry="select * from information_schema.TABLES where TABLE_SCHEMA = 'test' and TABLE_NAME='%s' \G" % (self.args.from_table.split('.')[1]); 
		#print qry
		
		sqfn=self.save_qry('get_table_info_%s.%s' % (self.args.from_table,self.args.from_partition),qry)	
		#print self.args.from_table.split('.')[1]
		#print r'\s+TABLE_NAME\:\s([%s]+)' % ''.join([r'\%s' %i for i in self.args.from_table.split('.')[1].lower()])
		#tab=''.join([r'\\%s' %i for i in self.args.from_table.split('.')[1].lower()])
		#tab=''.join([r'\\%s' %i for i in self.args.from_table.split('.')[1].lower()])
		
		regexp=re.compile(r'(TABLE_NAME|CREATE_OPTIONS)\:\s?(.*|.*)')	
		(r_int, status, err)=self.do_query(self.log,self.login, query=None,regexp=regexp,query_file=sqfn)
		#print r_int
		assert r_int , 'Table "%s" does not exists.' % (self.args.from_table)
		tinfo= {k[0].upper():k[1].upper() for k in r_int}
		assert tinfo.has_key('TABLE_NAME') , 'Cannot read TABLE_NAME from information_schema.TABLES for table "%s".' % (self.args.from_table)
		assert tinfo.has_key('CREATE_OPTIONS') , 'Cannot read CREATE_OPTIONS from information_schema.TABLES for table "%s".' % (self.args.from_table)
		#assert r_int[0].upper() in (self.args.from_table.split('.')[1].upper()), 'Table "%s" does not exists.' % (self.args.from_table)
		#print tinfo
		(ts,to) = self.args.from_table.upper().split('.')
		assert tinfo['TABLE_NAME'].strip()==to.strip() , 'Table "%s" does not exists in "%s".' % (to,ts)
		partitioned=False
		if 'PARTITIONED' in tinfo['CREATE_OPTIONS']:
			partitioned=True
		#sys.exit(0)	
		
		self.log.info('Done.')
		return (self.args.from_table, partitioned)
	def get_table_part_info(self):
		self.log.info('Fetching table info...')
		#qry="SELECT 'TABLE_INFO='||PARTITIONED||':'||TEMPORARY||':'||STATUS info from ALL_TABLES where UPPER(OWNER||'.'||TABLE_NAME)=UPPER('%s');" % (self.args.from_table)
		#qry='explain partitions select * from Persons_sub_partitioned \G'
		#qry='explain  select count(*) from test.Persons_sub_partitioned \G;'
		qry="select * from information_schema.TABLES where TABLE_SCHEMA = 'test' and TABLE_NAME='%s'\G" % (self.args.from_table); 
		#print qry
		sqfn=self.save_qry('get_table_info_%s.%s' % (self.args.from_table,self.args.from_partition),qry)	
		regexp=re.compile(r'\s+TABLE_SCHEMA\:\s(test)' % ''.join([r'\%s' %i for i in self.args.from_table]))		
		(r_int, status, err)=self.do_query(self.log,self.login, query=None,regexp=regexp,query_file=sqfn)
		#print r_int
		assert r_int , 'Table "%s" does not exists.' % (self.args.from_table)

		#assert r_int[0] , 'Table "%s" does not exists.' % (self.args.from_table)
		#assert r_int[0].upper() in (self.args.from_table.upper()), 'Table "%s" does not exists.' % (self.args.from_table)
		#sys.exit(0)
		assert r_int and r_int[0] and r_int[0][0], 'Table "%s" does not exists.' % (self.args.from_table)
		self.log.info('Done.')
		return r_int[0][0].split(':')		
	def set_table_payload(self, num_of_shards):
		print ''
		(table, partitioned) = self.get_table_info()
		assert not partitioned , 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table

		#sql_query =''
		#assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file

		#f = open(self.query_sql_file, 'r')

		#sql_query= ''f.read()
		#sql_query=sql_query.replace('"',"'")
		#print sql_query
		#f.close()
		#print sql_query
		#sys.exit(0)
		#assert sql_query, 'Query is not set'
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from %s as t;""" % self.args.from_table.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, q,0,regexp,field_term=fterm)
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
		print r
		#sys.exit(0)
		assert len(r)==1, 'Cannot get query recordcount.'
		assert len(r[0])==1, 'Cannot get query recordcount.'
		self.rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert self.rc, 'Source table is empty.'
		assert self.rc>0, 'Cannot get source record count. Exiting...'
		self.log.info(self.rc)
		self.log.info('Done.')
		#self.log.info('Fetching query columns.')
		self.log.info('Fetching source column names...')
		header=self.get_table_columns(self.args.from_table)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		self.log.info('Got %d columns.' % len(header))
		self.log.info('Done.')
		cols=[]			
		for h in header:
			#print h
			#self.log.info('%s %s(%s)' % tuple(h[:3]))	
			cols.append(h)
		#print cols
		header_line= self.field_term.join(cols)	
		shard_size=self.rc/num_of_shards
		#print shard_size

		assert shard_size>1 or num_of_shards==1, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,self.rc)
	
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
		
		if num_of_shards>1:
			self.log.info('Sharding query by %s' % cols[0])
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
				shq='SELECT * FROM %s' % self.args.from_table
				qry=self.get_sharded_sql(shq,rowid_from,rowid_to,self.rc,outfn)
				#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\query_%s.sql' % (sqdir,i)
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
	def set_payload(self,num_of_shards):
		#print self.T
		#sys.exit(0)
		if self.T:
			if self.P:
				return self.set_part_table_payload(num_of_shards)
			if self.SP:
				return self.set_subpart_table_payload(num_of_shards)
			else:
				return self.set_table_payload(num_of_shards)
		else:
			return self.set_query_payload(num_of_shards)
	def set_query_payload000(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file
		qry='SELECT * FROM (%s) p' % self.from_query.strip().strip(';').strip()
		#print qry
		#sys.exit(1)
		(cols_from) = self.get_query_columns( qry)
		assert cols_from, 'Cannot fetch source query columns'
		from_pld=[]		
		#globalStatus={}
		from_pld=[]	
		
		if 1:	
			(rowid_from,rowid_to) = (None,None)
			outfn=self.get_outfn(0)
			qry=self.get_sharded_sql(self.args.query_sql_file,rowid_from,rowid_to,self.rc,outfn)
			#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
			#print qry
			#sys.exit(0)
			sqdir= '%s\\sql' % self.datadir
			sqfn='%s\\query_%s.sql' % (sqdir,i)
			sqf = open(sqfn, "w")
			sqf.write(qry)
			sqf.close()			
			from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,sqfn))
		#print from_pld
		#sys.exit(1)
		#shards=((0,0,0),)
		shards=['0||||||']
		return (shards,from_pld) 	
	def count_source_records(self,sql_query):
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, q,0,regexp,field_term=fterm)
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
		return (r, status,sql_err)
		
	def set_query_payload(self, num_of_shards):
		print ''
		sql_query =''
		assert self.query_sql_file, 'Query file is not set.'
		assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file

		f = open(self.query_sql_file, 'r')

		sql_query= f.read()
		#sql_query=sql_query.replace('"',"'")
		#print sql_query
		f.close()
		#print sql_query
		#sys.exit(0)
		assert sql_query, 'Query is not set'
		self.log.info('Counting rows in source...')
		(r, status,sql_err)=self.count_source_records(sql_query)
		#print r
		assert len(r)==1, 'Cannot get query recordcount.'
		assert len(r[0])==1, 'Cannot get query recordcount.'
		self.rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert self.rc, 'Source table is empty.'
		assert self.rc>0, 'Cannot get source record count. Exiting...'
		self.log.info(self.rc)
		self.log.info('Done.')
		#self.log.info('Fetching query columns.')
		self.log.info('Fetching source column names...')
		header=self.get_query_columns(sql_query)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		self.log.info('Got %d columns.' % len(header))
		self.log.info('Done.')
		cols=[]			
		for h in header:
			#print h
			#self.log.info('%s %s(%s)' % tuple(h[:3]))	
			cols.append(h)
		#print cols
		header_line= self.field_term.join(cols)	
		shard_size=self.rc/num_of_shards
		#print shard_size

		assert shard_size>1 or num_of_shards==1, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,self.rc)
	
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
		
		if num_of_shards>1:
			self.log.info('Sharding query by %s' % cols[0])
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
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,self.rc,outfn)
				#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\query_%s.sql' % (sqdir,i)
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
	def get_spool_config(self,from_pld):
		if self.T:
			if self.P:
				return self.get_part_table_spool_config(from_pld)
			else:
				return self.get_table_spool_config(from_pld)
		else:
			return self.get_query_spool_config(from_pld)
	def get_part_table_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		spConf=[ db_client_loc ,'-u', self.args.from_user, '-p%s' % self.args.from_passwd,'-D',self.args.from_db_name, '-h', self.args.from_db_server]
					
		
		#pprint(spConf)
		#sys.exit(0)
		return spConf	
	def get_table_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		spConf=[ db_client_loc ,'-u', self.args.from_user, '-p%s' % self.args.from_passwd,'-D',self.args.from_db_name, '-h', self.args.from_db_server]
					
		
		#pprint(spConf)
		#sys.exit(0)
		return spConf
	def get_query_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		spConf=[ db_client_loc ,'-u', self.args.from_user, '-p%s' % self.args.from_passwd,'-D',self.args.from_db_name, '-h', self.args.from_db_server]
					
		
		#pprint(spConf)
		#sys.exit(0)
		return spConf		
	def get_inserted_count(self,cnt):
		return cnt
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, self.get_firstrow()+1,0)		
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
		#print from_pld
		
		os.environ['MYSQL_HOME'] = r'%s\data' % conf.dbclients[self.db][:-3]
		
		#sys.exit(1)
		p2 = Popen(spConf,stdin=PIPE,  stdout=PIPE, stderr=PIPE)# '-S',  stdin=p1.stdout,
		output, err = p2.communicate(file(sqfn).read())
		#pprint(output)
		#print err
		status=p2.wait()
		ins_cnt = -1
		grp=None
		out=[]
		status=p2.wait()
		#sys.exit(0)
		regexp=re.compile(r'^(\d+)')
		for o in output.split('\r'):
		#while output:
			#output = p2.stdout.readline()
			#pprint(o.strip())
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
											
		ins_cnt=-1
		if out:
			ins_cnt=int(out[0])
		else:
			print output
			if err:
				self.log.error(err)
		
		return (ins_cnt,status)
	
