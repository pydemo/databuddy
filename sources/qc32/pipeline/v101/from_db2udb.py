import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_db2udb import Db2UDB
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
import shlex
e=sys.exit
class FromDb2UDB(Db2UDB):
	"""DB2 UDB db"""
	def __init__(self,parent,log,datadir,conf, db='DBTUDB'):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(self.args.from_user, self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		Db2UDB.__init__(self,log,self.login,datadir,conf.args) 
		#self.query_sql_file=query_sql_file
		self.db=db
		self.tab_cols={}
		self.db_client_dbshell=None
		self.db_client_spooler=None
		self.from_query=[]
		self.from_query_name=[]	
		#self.db=db
		self.query_sql_file=None
		if hasattr(self.args, 'query_sql_file'):
			self.query_sql_file=self.args.query_sql_file		
		self.T, self.P, self.QF, self.QD =(False, False,  False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
			if self.args.from_partition:
				#assert not self.args.from_sub_partition, 'Set Partition or Subpartition but not both.'
				self.P=True
		else:
			lim=''
			if self.args.lame_duck:
				lim=' FETCH FIRST %s ROWS ONLY' % self.args.lame_duck
			assert self.args.query_sql_file or self.args.query_sql_dir, 'Either query file or query dir has to be set.'
			if self.args.query_sql_file:
				self.QF=True
				assert os.path.isfile(self.args.query_sql_file), 'Query file "%s" does not exists.' % self.args.query_sql_file		
				qry=open(self.args.query_sql_file).read().strip().strip(';')

				self.from_query.append('%s %s' %(qry,lim))
				#self.from_query_name.append(self.args.query_sql_file)
			elif self.args.query_sql_dir:
				self.QD=True
				
				
				#print self.args.query_sql_dir
				assert os.path.isdir(self.args.query_sql_dir), 'Query dir "%s" does not exists.' % self.args.query_sql_dir
				import glob
				for qf in os.listdir(self.args.query_sql_dir):
					#print qf
					qry=open(os.path.join(self.args.query_sql_dir, qf)).read().strip().strip(';')
					self.from_query.append('%s %s' %(qry,lim))
					self.from_query_name.append(qf)				
	def print_copy_details(self):	
		part=''	
		if self.T:
			source='table: %s' % self.args.from_table
			if self.P:
				part="""
	partition: %s""" % self.args.from_partition
		elif self.QF:
			source='query file: %s' % self.args.query_sql_file
		elif self.QD:
			source='query dir: %s' % self.args.query_sql_dir
		else:
			assert False, 'Unknown source type.'
		
		print """		
From %s:	
	from db: %s
	%s%s
	shards:\t%s
		""" % (conf.dbs[self.db],'%s/%s/%s' % (self.args.from_user,self.args.from_db_name,self.args.from_db_server),source,part,self.args.num_of_shards)	
		#sys.exit(1)
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
		

	def get_sharded_sql(self,sql_query,rowid_from,rowid_to, cols,outfn):
		sql_query=sql_query.strip().strip(';')
		from_to=''
		rn='ROW_NUMBER() OVER() rn,'
		#print rowid_from,rowid_to
		#sys.exit(0)
		clist='*'
		if not rowid_from and not rowid_to:
			from_to=''	
			rn=''
		else:
			clist=','.join(cols)
			if not rowid_from:		
				from_to=' where rn  < %s ' % (rowid_to)
			else:			
				if rowid_to: 
					from_to=' where rn  BETWEEN %s and %s ' % (rowid_from-1, rowid_from+rowid_to)
				else:
					from_to=' where rn  > %s' % (rowid_from-1)
		hdr=''
		

		#if self.args.header:
		#	hdr=' WITH COLUMN NAMES'

			
		out=r"""CONNECT TO SAMPLE
EXPORT TO %s OF DEL MODIFIED BY NOCHARDEL COLDEL%s 	select %s from (select %s t.* from (%s) t ) v %s
CONNECT RESET
""" % (os.path.normpath(outfn).replace("\\", "\\\\"),self.args.field_term, clist, rn,sql_query.strip().strip(';'), from_to)	
		#print out
		#sys.exit(0)
		
		return out
	def get_firstrow(self):
		return 0
	def count_rows(self,query):
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:(\d+)')

		q="""select 'ROW COUNT:'||count(*) cnt from (%s) as t;""" % query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		r=None
		err=None
		try:
			lqfn = self.save_qry('source_row_count',q)
			(r, status,sql_err) = self.do_query(self.log,self.login, q,regexp=regexp,query_file=None, field_term=fterm)
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
		rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert rc, 'Source table is empty.'
		assert rc>0, 'Cannot get source record count. Exiting...'
		return rc
		self.log.info('Done.')
		
	def set_payload(self,num_of_shards,toDb=None):
		print ''
		#print self.QD
		#sys.exit(0)
		
		self.toDb=toDb
		if self.T:
			if self.P:
				return self.set_part_table_payload(num_of_shards)
			#if self.SP:
			#	return self.set_subpart_table_payload(num_of_shards)
			else:
				return self.set_table_payload(num_of_shards)
		else:
			if self.QF:
				return self.set_query_payload(num_of_shards)
			else:
				#print 3
				return self.set_querylist_payload()
				
	def set_querylist_payload(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		from_pld=[]
		shards=[]
		qid=0
		
		for q in self.from_query:
			q=q.strip().strip(';')
			#rc=self.count_rows(q)
			#print rc
			#sys.exit(0)
			#assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			#qry='SELECT * FROM (%s)' % q
			#print qry
			#(cols_from,status) = self.get_query_columns( q)
			cols_from =None
			#assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			if 1:
				#sys.exit(1)
				#print shards
				#(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#(sid,rowid_from, rowid_to, _) = shards[qid]
				#sql_query= 'SELECT * FROM (%s)' % q
				#qry=self.get_query(cols_from,sql_query)
				if self.toDb:
					outfn=self.toDb.get_out_fn(qid)
				else:
					outfn=self.get_outfn(qid)				
				qry=self.get_sharded_sql(q,None,None,None,outfn)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_qdir_%s.sql' % (sqdir,qid)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				
				from_pld.append(('Shard-%d' % qid,outfn,None,None,cols_from,sqfn))
				shards.append('%s||||||' % qid)
				qid +=1
					#globalStatus[i]=(99, None)	
			#pprint (from_pld)
			#pprint(shards)
			#sys.exit(1)
		return (shards,from_pld) 			

				
	def set_table_payload(self, num_of_shards):
		lim=''
		if self.args.lame_duck:
			lim=' FETCH FIRST %s ROWS ONLY' % self.args.lame_duck	
		sql_query ='SELECT * FROM %s %s' % (self.args.from_table, lim)
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)', re.M|re.I)
		#q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		
		fterm=self.field_term
		rc=self.count_rows(sql_query)
		if 1:
			self.log.info('Fetching query columns.')
			header=self.get_table_columns()
			
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
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)
				#if 1: #num_of_shards>1:
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,cols,outfn)
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
	def set_part_table_payload(self, num_of_shards):
		if 1:
			self.log.info('Fetching query columns.')
			header=self.get_table_columns()
			
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
		assert 	cols, 'Table columns are not set'
		
		#print cols
		#sys.exit(1)
		lim=''
		if self.args.lame_duck:
			lim=' FETCH FIRST %s ROWS ONLY' % self.args.lame_duck			
		sql_query ='SELECT %s FROM (SELECT DATAPARTITIONNUM(%s) pnum, t.* FROM %s t) where pnum=%s %s' % (','.join(cols),cols[0], self.args.from_table,self.args.from_partition, lim)
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)', re.M|re.I)
		#q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#print sql_query
		fterm=self.field_term
		rc=self.count_rows(sql_query)


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
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)
				#if 1: #num_of_shards>1:
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,cols,outfn)
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
		
	def set_query_payload(self, num_of_shards):
	
		sql_query =''
		#assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file

		#f = open(self.query_sql_file, 'r')

		sql_query= self.from_query[0]  #f.read()
		#sql_query=sql_query.replace('"',"'")
		#print sql_query
		#f.close()
		#print sql_query
		#sys.exit(0)
		assert sql_query, 'Query is not set'	
		regexp=re.compile(r'ROW COUNT\:\s+(\d+)', re.M|re.I)
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		#q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		rc=self.count_rows(sql_query.strip().strip(';'))
		if 1:
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
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)
				#if 1: #num_of_shards>1:
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,cols,outfn)
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
	def get_spool_config(self,from_pld):
		#pprint(from_pld)
		#sys.exit(1)
		if self.T:
			if self.P:
				return self.get_part_table_spool_config(from_pld)
			else:
				return self.get_table_spool_config(from_pld)
		else:
			if self.QF:
				return self.get_query_spool_config(from_pld)
			else:
				return self.get_querylist_spool_config(from_pld)
	def get_part_table_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server]
		#connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.from_user,self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		
		#spConf=[ r'%s\db2cmdadmin' % conf.dbclients[self.db],r'db2setcp', r'"db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"']
		spConf=[ db_client_loc , '-f', sqfn, '-z' ,'%s_spool_log.txt' % outfn.split('.')[0]]
		#'"%s"' % db_client_loc ,'-nogui','-c', connect_str, '-onerror', 'exit']
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf				
	def get_table_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server]
		#connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.from_user,self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		
		#spConf=[ r'%s\db2cmdadmin' % conf.dbclients[self.db],r'db2setcp', r'"db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"']
		spConf=[ db_client_loc , '-f', sqfn, '-z' ,'%s_spool_log.txt' % outfn.split('.')[0]]
		#'"%s"' % db_client_loc ,'-nogui','-c', connect_str, '-onerror', 'exit']
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf	
	def get_querylist_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server]
		#connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.from_user,self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		
		#spConf=[ r'%s\db2cmdadmin' % conf.dbclients[self.db],r'db2setcp', r'"db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"']
		spConf=[ db_client_loc , '-f', sqfn, '-z' ,'%s_spool_log.txt' % outfn.split('.')[0]]
		#'"%s"' % db_client_loc ,'-nogui','-c', connect_str, '-onerror', 'exit']
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf			
	def get_query_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server]
		#connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.from_user,self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		
		#spConf=[ r'%s\db2cmdadmin' % conf.dbclients[self.db],r'db2setcp', r'"db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"']
		spConf=[ db_client_loc , '-f', sqfn, '-z' ,'%s_spool_log.txt' % outfn.split('.')[0]]
		#'"%s"' % db_client_loc ,'-nogui','-c', connect_str, '-onerror', 'exit']
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf		
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
		#if sqfn:
		#	spConf=spConf+ [r'"%s"' % sqfn]	
		#cmd=  ' '.join(spConf)
		#print cmd
		#"C:\Program Files (x86)\IBM\SQLLIB_01\BIN\db2cmdadmin" db2setcp "db2 -f C:\\Python27\\data_mule_db2\\cmd2.sql -z C:\\Python27\\data_mule_db2\\DB2UploadLog.txt"

		#sys.exit(1)		
	
		
		#spConf=shlex.split(cmd)
		#pprint (spConf)
		#sys.exit(0)


		#p2 = Popen(r'C:\Python27\data_mule_db2\run.bat',stdin=PIPE,  stdout=PIPE )# '-S',  stdin=p1.stdout,
		if 0:
			import subprocess
			kwargs = {}
			if subprocess.mswindows:
				su = subprocess.STARTUPINFO()
				su.dwFlags |= subprocess.STARTF_USESHOWWINDOW
				su.wShowWindow = subprocess.SW_HIDE
				kwargs['startupinfo'] = su 
		if 1:
			os.environ['DB2CLP'] = 'DB20FADE'
			os.environ['DB2INSTANCE'] = 'DB2'
			os.environ['DB2PATH'] = r'C:\Program Files (x86)\IBM\SQLLIB_01'
			#cmd=r'db2.exe -f "%s" -z C:\\Python27\\data_mule_db2\\DB2UploadLog.txt' % sqfn
			#spConf=shlex.split(cmd) 
			#pprint (spConf)
			#print sqfn
			#e(0)
			p2 = Popen(spConf,stdin=PIPE,  stdout=PIPE, shell=True)# '-S',  stdin=p1.stdout,
			"""	['C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN\\db2.exe',
			 '-f',
			 'C:\\Python27\\data_migrator_1239\\logs\\20141201_194315_505000\\sql\\spool_qdir_0.sql',
			 '-z',
			 'C:\\Python27\\data_migrator_1239\\CSV_OUT\\spool_20141201_194315_505000_db2_query_spool_log.txt']
			"""
			#p2 = Popen(['cmd','/C',r'C:\Python27\data_mule_db2\run.bat'],stdin=PIPE,  stdout=PIPE, **kwargs )# '-S',  stdin=p1.stdout,
			output, err = p2.communicate()
		else:
			os.environ['DB2CLP'] = 'DB20FADE'
			os.environ['DB2INSTANCE'] = 'DB2'
			#os.environ['CLASSPATH'] = r'C:\Program Files (x86)\IBM\SQLLIB_01\java\db2java.zip;C:\Program Files (x86)\IBM\SQLLIB_01\java\db2jcc.jar;C:\Program Files (x86)\IBM\SQLLIB_01\java\sqlj.zip;C:\Program Files (x86)\IBM\SQLLIB_01\java\db2jcc_license_cu.jar;C:\Program Files (x86)\IBM\SQLLIB_01\bin;C:\Program Files (x86)\IBM\SQLLIB_01\java\common.jar;.;C:\PROGRA~2\TimesTen\TT1122~1\lib\ttjdbc6.jar;.;C:\Program Files (x86)\Java\jre7\lib\ext\QTJava.zip'
			
			os.environ['DB2PATH'] = r'C:\Program Files (x86)\IBM\SQLLIB_01'
			#"C:\Program Files (x86)\IBM\SQLLIB_01\BIN\db2cmdadmin" db2setcp "C:\Python27\data_mule_db2\db2_test.bat"
			cmd=r'db2.exe -f C:\\Python27\\data_mule_db2\\cmd2.sql -z C:\\Python27\\data_mule_db2\\DB2UploadLog.txt'
			spConf=shlex.split(cmd) 
			#pprint (spConf)
			#sys.exit(0)
			p2 = Popen([r"C:\Program Files (x86)\IBM\SQLLIB_01\BIN\db2cmdadmin", 'db2setcp', '"C:\Python27\data_mule_db2\db2exe_test.bat"'],stdin=PIPE,  stdout=PIPE, shell=True)# '-S',  stdin=p1.stdout,
		
			#p2 = Popen(['cmd','/C',r'C:\Python27\data_mule_db2\run.bat'],stdin=PIPE,  stdout=PIPE, **kwargs )# '-S',  stdin=p1.stdout,
			output, err = p2.communicate()
		#print output 
		#print err
		regexp=re.compile(r'Number of rows exported\: (\d+)')
		grp=None
		out=[]
		status=p2.wait()
		#sys.exit(0)
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
											
		#print out
		#sys.exit(0)
		#print err
		cnt=int(out[0])
		if err:
			self.log.error(err)
		#
		
		return (cnt,status)
	
