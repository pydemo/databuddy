import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_sqllite import SQLLite
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf
import config.config as conf 

class FromSQLLite(SQLLite):
	"""SQLLite db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(args.from_db_name)
		SQLLite.__init__(self,log,self.login,datadir,args) 
		self.log=log
		self.query_sql_file=None
		if hasattr(self.args, 'query_sql_file'):
			self.query_sql_file=self.args.query_sql_file
		self.field_term=args.field_term
		self.db=db
		self.datadir=datadir
		self.args=args
		self.db_client_dbshell=None
		self.db_client_spooler=None
		self.from_query=[]
		self.from_query_name=[]			
		self.tab_cols={}
		self.T, self.QF, self.QD =(False,  False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
		else:
			assert self.args.query_sql_file or self.args.query_sql_dir, 'Either query file or query dir has to be set.'
			if self.args.query_sql_file:
				self.QF=True
				assert os.path.isfile(self.args.query_sql_file), 'Query file "%s" does not exists.' % self.args.query_sql_file		
				self.from_query.append(open(self.args.query_sql_file).read().strip().strip(';'))
			elif self.args.query_sql_dir:
				self.QD=True
				assert os.path.isdir(self.args.query_sql_dir), 'Query dir "%s" does not exists.' % self.args.query_sql_dir
				import glob
				for qf in os.listdir(self.args.query_sql_dir):
					self.from_query.append(open(os.path.join(self.args.query_sql_dir, qf)).read())
					self.from_query_name.append(qf)	
					
	def print_copy_details(self):		
		if self.T:
			source='table: %s' % self.args.from_table
		elif self.QF:
			source='query file: %s' % self.args.query_sql_file
		elif self.QD:
			source='query dir: %s' % self.args.query_sql_dir
		else:
			assert False, 'Unknown source type.'
		part=''	
		print """		
From %s:	
	from db: %s
	%s%s
	shards:\t%s

		""" % (conf.dbs[self.db], '%s' % (self.args.from_db_name),source,part,self.args.num_of_shards)	
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
	def get_spool_config(self,from_pld):
		#pprint(from_pld)
		#sys.exit(1)
		if self.T:
			#if self.P:
			#	return self.get_part_table_spool_config(from_pld)
			#else:
			return self.get_table_spool_config(from_pld)
		else:
			if self.QF:
				return self.get_query_spool_config(from_pld)
			else:
				return self.get_querylist_spool_config(from_pld)	
	def get_table_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		spConf=[ db_client_loc ,self.args.from_db_name]
					
		
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
		spConf=[ db_client_loc ,self.args.from_db_name]
					
		
		#pprint(spConf)
		#sys.exit(0)
		return spConf
	def get_querylist_spool_config(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		spConf=[ db_client_loc ,self.args.from_db_name]
					
		
		#pprint(spConf)
		#sys.exit(0)
		return spConf		
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
		hdr=''
		if self.args.header:
			hdr='.headers on'
		out=r"""
%s
.mode list
.separator "%s"
.output %s
%s;
.output stdout
select 'ROWCOUNT'||count(*) cnt from (%s) t;
.quit
""" % (hdr,self.args.field_term, os.path.normpath(outfn).replace("\\", "\\\\"), qry,qry)
				
		return out
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;
	def get_firstrow(self):
		return 0
	def count_rows(self,query):
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
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
			#if self.P:
			#	return self.set_part_table_payload(num_of_shards)
			#if self.SP:
			#	return self.set_subpart_table_payload(num_of_shards)
			#else:
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
	
		sql_query ='SELECT * FROM %s' % self.args.from_table
		regexp=re.compile(r'ROW COUNT\:\|(\d+)')
		
		self.rc=self.count_rows(sql_query.strip().strip(';'))

		header='' #self.get_query_columns(sql_query)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		#self.log.info('Got %d columns.' % len(header))
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

	def set_query_payload(self, num_of_shards):
	
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
		regexp=re.compile(r'ROW COUNT\:\|(\d+)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		self.rc=-1
		opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		
		#q="""select 'ROW COUNT:' filter ,count(*) cnt from (%s) as t;""" % sql_query.strip().strip(';')
		#q= sql_query.strip().strip(';')
		#print q
		
		fterm=self.field_term
		self.rc=self.count_rows(sql_query.strip().strip(';'))

		header='' #self.get_query_columns(sql_query)
		
		#header=self.get_SS_query_columns(self.log,self.login,sql_query)
		
		#print header
		#sys.exit(1)
		#self.log.info('Got %d columns.' % len(header))
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
		#print outfn
		
		#os.environ['MYSQL_HOME'] = r'%s\data' % conf.dbclients[self.db][:-3]
		
		#sys.exit(1)
		p2 = Popen(spConf,stdin=PIPE,  stdout=PIPE, stderr=PIPE)# '-S',  stdin=p1.stdout,
		output, err = p2.communicate(file(sqfn).read())
		#print(file(sqfn).read())
		#pprint(output)
		#print err
		status=p2.wait()
		ins_cnt = -1
		grp=None
		out=[]
		status=p2.wait()
		#print self.rc
		#sys.exit(0)
		regexp=re.compile(r'^ROWCOUNT(\d+)')
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
	
