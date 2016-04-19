import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_sqlserver import SQLServer
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
from common.v101.exceptions import RowCountError

class FromSQLServer(SQLServer):
	"""SQLServer db"""
	def __init__(self,parent,log,datadir,conf, db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(self.args.from_user, self.args.from_passwd, self.args.from_db_name, self.args.from_db_server)
		SQLServer.__init__(self,log,self.login,datadir,self.args) 
		self.log=log
		#self.login=login
		self.query_sql_file=self.args.query_sql_file
		self.field_term=args.field_term
		self.db=db
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		#if hasattr(args, 'from_partition') and args.query_sql_file:
		#	self.partitions
		self.ent = False #Enterpise
		
		if db in ('SSENT'):
			self.ent =True 
		self.lim=''
		if self.args.lame_duck:
			self.lim  = 'TOP %s' % self.args.lame_duck				
		self.db_client_dbshell=None
		self.db_client_spooler=None
		self.from_query=[]
		self.from_query_name=[]		
		self.T, self.P, self.QF, self.QD =(False,  False, False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
			if hasattr(args, 'from_partition') and self.args.from_partition:
				#assert not self.args.from_sub_partition, 'Set Partition or Subpartition but not both.'
				self.P=True
		else:
			assert self.args.query_sql_file or self.args.query_sql_dir, 'Either query file or query dir has to be set.'
			if self.args.query_sql_file:
				self.QF=True
				assert os.path.isfile(self.args.query_sql_file), 'Query file "%s" does not exists.' % self.args.query_sql_file		
				q=open(self.args.query_sql_file).read().strip().strip(';')
				if self.lim:
					q='SELECT %s * FROM (%s) t' % (self.lim,q.strip().strip(';'))
				self.from_query.append(q)				
				#self.from_query.append(open(self.args.query_sql_file).read().strip().strip(';'))
				#self.from_query_name.append(self.args.query_sql_file)
			elif self.args.query_sql_dir:
				self.QD=True
				#print self.args.query_sql_dir
				assert os.path.isdir(self.args.query_sql_dir), 'Query dir "%s" does not exists.' % self.args.query_sql_dir
				import glob
				for qf in os.listdir(self.args.query_sql_dir):
					#print qf
					q=open(os.path.join(self.args.query_sql_dir, qf)).read().strip().strip(';')
					if self.lim:
						q='SELECT %s * FROM (%s) t' % (self.lim,q.strip().strip(';'))
					self.from_query.append(q)
					self.from_query_name.append(qf)			
		if 0:
			self.Q, self.T, self.P =(False, False, False)
			if self.args.from_table:
				assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
				self.T=True
				if self.ent and self.args.from_partition:				
					self.P=True
				#elif self.args.from_sub_partition:				
				#	self.SP=True
			else:
				if  self.ent:
					assert not self.args.from_partition, 'You cannot use partition "%s" (--from_partition) in QUERY mode.' % self.args.from_partition
				#assert not self.args.from_sub_partition, 'You cannot use sub-partition "%s" (--from_partition) in QUERY mode.' % self.args.from_sub_partition
				assert self.args.query_sql_file, 'Data source should be Table or Query. None is set.'
				
				
				#assert int(self.args.num_of_shards) == 1, 'Cannot shard in QUERY mode. Set num_of_shards=1.'
				self.Q=True
				assert os.path.isfile(self.args.query_sql_file)
				
				self.from_query=open(self.args.query_sql_file).read()
			
	def print_copy_details(self):
		if self.T:
			source='table: %s' % self.args.from_table
		else:
			if self.QF:
				source='query: %s' % self.args.query_sql_file
			else:
				source='query dir: %s' % self.args.query_sql_dir
		part=''
		if self.ent and self.P:
			part="""
		partition: %s""" % self.args.from_partition	
		print """		
	From %s:	
		from db: %s
		%s%s
		shards:\t%s
		""" % (conf.dbs[self.db],'%s/%s/%s' % (self.args.from_user,self.args.from_db_name,self.args.from_db_server),source,part,self.args.num_of_shards)	
	def get_db_client_spooler(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['SPOOLER'][self.db])
		if self.args.source_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.source_client_home.strip('"'), loader)).strip("'").strip('\\').strip('\\')
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
			self.db_client_dbshell=(r'%s\%s' % (self.args.source_client_home.strip('"'), loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_dbshell		
	def get_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		db_client_sp=self.get_db_client_spooler()
		fterm=self.field_term
		if self.field_term =='|':
			fterm='%s' % self.field_term
		spConf=[ db_client_sp,'-s',fterm,'-W','-i',sqfn,'-U', self.args.from_user, '-P', self.args.from_passwd, '-S', self.args.from_db_server, '-d',self.args.from_db_name, '-h','-1']
		#	pprint(spConf)
		#sys.exit(0)
		return spConf
	def get_sharded_sql(sql_query,rowid_from,rowid_to):	
		qry='%s%s' % (sql_query,' ORDER BY 1 ASC OFFSET %s ROWS' % (rowid_from))
		if rowid_to:
			qry='%s%s' % (qry,' FETCH NEXT %s ROWS ONLY ' % (rowid_to))
		return qry
	def get_sharded_sql_2008(self,logger,cols, sql_query,rowid_from,rowid_to):	
		#qry='select %s from ( SELECT Item.*, ROW_NUMBER() OVER (ORDER BY NewId())  row_number FROM (%s) as Item) as t' % (','.join(cols),sql_query)
		#qry='select %s from ( SELECT Item.*, CAST(ABS(CHECKSUM(NEWID())) ' % (','.join(cols))
		#qry=qry+'%'+' 10000000 AS bigint)  as  row_number FROM (%s) as Item) as t' % (sql_query)
		shard_by =cols[0]
		#shard_by ='AccountId'
		#print cols
		
		qry='select %s from ( SELECT Item.*, ROW_NUMBER() OVER (ORDER BY %s)  row_number FROM (%s) as Item) as t' % (','.join(cols),shard_by,sql_query)
		
		if rowid_to:
			qry='%s%s' % (qry,' WHERE row_number between %d and %d' % (rowid_from,rowid_from+rowid_to))
		else:
			qry='%s%s' % (qry,' WHERE row_number >= %d ' % (rowid_from))
		#print qry
		#sys.exit(0)
		return qry
	def get_firstrow(self):
		return 0
	def get_ddl_extract_config(self,from_pld):
		return None		
	def count_rows(self,query):
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:\|(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""SET NOCOUNT ON
	select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t
		""" % query.strip().strip(';')
		#q="""select 'ROW COUNT:'||count(*) cnt from (%s);""" % 
		#q= sql_query.strip().strip(';')
		#print q
		#select 'ROW COUNT:'||count(*) cnt from (select 'ROW COUNT:' filter ,count(*) cnt from (SELECT * FROM     Persons_pipe_datetime LIMIT 20) as t) as t;
		
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
		rc=int(r[0][0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert rc, 'Source table is empty.'
		assert rc>0, 'Cannot get source record count. Exiting...'
		return rc
		self.log.info('Done.')
		
	def set_payload(self,num_of_shards,toDb=None):
		#print self.T
		#sys.exit(0)
		self.toDb=toDb
		if self.T:
			if self.ent and self.P:
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
				return self.set_querylist_payload(num_of_shards)
				
			#return self.set_query_payload()
			
	def set_query_payload(self,num_of_shards):
		print ''
		sql_query =self.from_query[0]
		assert sql_query, 'Query is not set'	
		rc=self.count_rows(sql_query)
		#self.log.info('Fetching query columns.')
		header=''
		header=self.get_query_columns(self.log,self.login,sql_query)
		#print header
		#sys.exit(1)
		#self.log.info('Got %d columns.' % len(header[0]))
		cols=[]	
		if 1:
			for h in header[0]:
				#print h
				#self.log.info('%s' % h)	
				cols.append(h)
		#else:
		#	cols.append('*')
		#print cols
		header_line=''
		#header_line= self.field_term.join(cols)
		num_of_shards=	self.args.num_of_shards	
		shard_size=rc/num_of_shards
		#print shard_size

		assert shard_size>0, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,rc)
	
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
				#qry='SET NOCOUNT ON\n%s' % sql_query
				qry= sql_query
				if num_of_shards>1:
					qry=self.get_sharded_sql_2008(self.log,cols,sql_query,rowid_from,rowid_to)
					#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_query_%s.sql' % (sqdir,i)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)	
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,header_line,sqfn))
				#from_pld.append((sqfn,header_line))
				#print ("Shard-%d" % i,rowid_from,rowid_to,conf)
				#print skip
				#globalStatus[i]=(99, None)
		#print from_pld
		#sys.exit(1)
		return (shards,from_pld) 
	def set_querylist_payload(self,num_of_shards):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		from_pld=[]
		shards=[]
		qid=0

		from_pld=[]			
		for q in self.from_query:
			q=q.strip().strip(';')
			#print q
			#rc=self.count_rows(q)
			(sid,rowid_from, rowid_to) = (qid,0,0)
			#print sid,rowid_from, rowid_to
			#sys.exit(0)
			#assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			#qry='SELECT * FROM (%s) as p' % q
			#print qry
			(cols_from,status) = self.get_query_columns( self.log,self.login,q)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			if 1:
				#sys.exit(1)
				#print shards
				#(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#(sid,rowid_from, rowid_to, _) = shards[qid]
				#sql_query= """\\t\nSELECT * FROM (%s) as t""" % q
				#qry=sql_query #self.get_query(cols_from,sql_query)
				if self.toDb:
					outfn=self.toDb.get_out_fn(qid)
				else:
					outfn=self.get_outfn(qid)					

				qry=self.get_sharded_sql_2008(self.log,cols_from,q,rowid_from,rowid_to)
				#pprint (qry)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_table_%s.sql' % (sqdir,qid)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				if self.toDb:
					outfn=self.toDb.get_out_fn(qid)
				else:
					outfn=self.get_outfn(qid)				
				from_pld.append(('Shard-%d' % qid,outfn,None,None,cols_from,sqfn))
				shards.append('%s||||||' % qid)
				qid +=1
					#globalStatus[i]=(99, None)	
			#pprint (from_pld)
			#pprint(shards)
			#sys.exit(1)
		return (shards,from_pld) 
	def spool_ddl(self,outfn, spConf, payload):
		self.log.error('DDL extract is not supported')
		return (-1, -1)
	def set_table_payload(self, num_of_shards):
		print ''
		self.log.info('Counting rows...')
		sql_query ='SELECT %s * FROM %s' % (self.lim,self.args.from_table)
		rc=self.count_rows(sql_query)
		header=''
		header=self.get_table_columns(self.log,self.login,self.args.from_table)
		#print header
		#sys.exit(1)
		#self.log.info('Got %d columns.' % len(header[0]))
		cols=[]	
		if 1:
			for h in header[0]:
				#print h
				#self.log.info('%s' % h)	
				cols.append(h)
		#else:
		#	cols.append('*')
		#print cols
		header_line=''
		#header_line= self.field_term.join(cols)	
		shard_size=rc/num_of_shards
		#print shard_size

		assert shard_size>0, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,rc)
	
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
				#qry='SET NOCOUNT ON\n%s' % sql_query
				#sql_query= 'SELECT * FROM %s t' % self.args.from_table
				qry= sql_query
				if num_of_shards>1:
					qry=self.get_sharded_sql_2008(self.log,cols,sql_query,rowid_from,rowid_to)
					#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_table_%s.sql' % (sqdir,i)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)	
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,header_line,sqfn))
				#from_pld.append((sqfn,header_line))
				#print ("Shard-%d" % i,rowid_from,rowid_to,conf)
				#print skip
				#globalStatus[i]=(99, None)
		#print from_pld
		#sys.exit(1)
		return (shards,from_pld) 
	def set_part_table_payload(self, num_of_shards):
		print ''
		
		sql_query ='select %s * from %s WHERE $Partition.%s' % (self.lim,self.args.from_table, self.args.from_partition)
		rc=self.count_rows(sql_query)
		#self.log.info('Fetching query columns.')
		header=''
		header=self.get_table_columns(self.log,self.login,self.args.from_table)
		#print header
		#sys.exit(1)
		#self.log.info('Got %d columns.' % len(header[0]))
		cols=[]	
		if 1:
			for h in header[0]:
				#print h
				#self.log.info('%s' % h)	
				cols.append(h)
		#else:
		#	cols.append('*')
		#print cols
		header_line=''
		#header_line= self.field_term.join(cols)	
		shard_size=rc/num_of_shards
		#print shard_size

		assert shard_size>0, 'num_of_shards (%d) is too high for a given query record count (%d)' % (num_of_shards,rc)
	
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
				#qry='SET NOCOUNT ON\n%s' % sql_query
				#sql_query= 'SELECT * FROM %s as t WHERE $Partition.%s' % (self.args.from_table, self.args.from_partition)
				qry= sql_query
				if num_of_shards>1:
					qry=self.get_sharded_sql_2008(self.log,cols,sql_query,rowid_from,rowid_to)
					#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_table_%s.sql' % (sqdir,i)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)	
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,header_line,sqfn))
				#from_pld.append((sqfn,header_line))
				#print ("Shard-%d" % i,rowid_from,rowid_to,conf)
				#print skip
				#globalStatus[i]=(99, None)
		#print from_pld
		#sys.exit(1)
		return (shards,from_pld) 
		
	def get_inserted_count(self,cnt):
		return cnt
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, self.get_firstrow()+1,0)	
	def read_last_line(self, outfn):
		count=-1
		#stat=os.stat(outfn).st_size
		#print stat
		if 1:
			#print 'spooled %d B' % stat
			import io
			#file = open(outfn,  mode='r+')
			file = io.open(outfn, 'r+', encoding = 'utf-8')

			file.seek(0, os.SEEK_END)
			pos = file.tell() - 3
			#print pos
			char=file.read(1)
			#pprint (char)
			eol=char != "\n"	
			nums=[str(i) for i in range(0,10)]
			#print nums
			cnt=[]
			out=[]
			while pos > 0 and eol:
				#pprint(file.read(1))
				pos -= 1
				file.seek(pos, os.SEEK_SET)
				char=file.read(1)
				eol=char != "\n"
				#pprint(char)
				#print 1,pos
				if char in nums:
					cnt.append(char)
				else:
					out.append(char)
			if 0:
				char=file.read(1)
				eol=char != "\n"				
				while pos > 0 and eol:
					#pprint(file.read(1))
					pos -= 1
					file.seek(pos, os.SEEK_SET)
					char=file.read(1)
					eol=char != "\n"
					#pprint(char)
					#print 2,pos
				char=file.read(1)
			if 0:
				eol=char != "\n"	
				while pos > 0 and eol:
					
					pos -= 1
					file.seek(pos, os.SEEK_SET)
					char=file.read(1)
					eol=char != "\n"
					#pprint(char)				
					if char in nums:
						cnt.append(char)
					else:
						out.append(char)
					#print 3,pos, char, ord(char)
				#print 'last',pos			
			if pos > 2:
				pos -= 2
				file.seek(pos, os.SEEK_SET)
				#pprint(file.read(1))
				#print 'truncate'
				file.truncate()
				
			else:
				
				self.log.error('Cannot get spool row count.')
				last_line=''.join(out[::-1])
				#print lastline
				file.close()
				raise RowCountError(last_line)
				
			file.close()
			#print ord('0'),  ord('9')

			#stat=os.stat(outfn).st_size		
		
		return (cnt,out)	
		
	def spool_source_data(self,outfn, spConf, env):
		(shard_name,from_pld,to_pld)=env
		#(rowid_from,rowid_to,ctlfn,from_db,from_table,cols_from)=from_pld
		#shard=shard_name.split('-')[1]
		#outfn='%s\\shard_%s.data' % (self.datadir,shard)
		#outfn=r'C:\Python27\ora2ss_data_pipe\data\\shard_%s.data' % shard
		outf=open(outfn, "w")
		#pprint (spConf)
		#print ' '.join(spConf)
		#sqlcmd -s | -W -i C:\Python27\data_mule_sybase\logs\20141004_105809\sql\query_0.sql -U sa -P 198Morgan -S ALEX_BUZ-PC\SQLEXPRESS

		#print spConf
		#sys.exit(0)
		p2 = Popen(spConf,  stdout=outf , stderr=PIPE ) # '-S',  stdin=p1.stdout,
		#status=p2.wait()
		#pprint(dir(outf))
		#outf.flush()
		#outf.flush()
		#os.fsync(outf)
		outf.close()
		#time.sleep(1)
		if p2.stdout:
			output=' '
			while output:
				output = p2.stdout.readline()
				print output
			#status=p2.wait()
		#sys.exit(1)
		status=p2.wait()
		count=-1
		(cnt,out)=self.read_last_line(outfn)
		#print cnt
		#print out
		
		
		count=int( ''.join(cnt[::-1]))
		#print count
		#sys.exit(1)
		
		return (count, status)	
	
