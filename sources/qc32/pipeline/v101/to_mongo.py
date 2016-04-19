import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_mongo import MongoDb
import codecs, tempfile
from pprint import pprint
import config.config as conf
#import common.v101.config as conf 
from include.v101.host_map import host_map as hmap
e=sys.exit
class ToMongo(MongoDb):
	"""SQLServer db"""
	def __init__(self,parent,log,datadir,conf, db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.args.to_db='%s/%s@%s' % (self.args.to_user,self.args.to_passwd,self.args.to_db_name)
		self.login=self.args.to_db
		MongoDb.__init__(self,log,datadir,self.args.to_db,conf) 
		self.log=log
		
		
		self.to_table=self.args.to_collection
		self.db=db
		self.field_term=args.field_term
		self.datadir=datadir
		self.to_pld={}
		self.tab_cols={}
		self.uargs_db=self.uargs.target.target(self.log,datadir,self.login,self.conf,db,self.args.to_collection)
		self.uargs_common=self.uargs.target.common(datadir,self.login,self.conf)
		#self.args=args
		#self.args.nls_date_format=self.args.nls_date_format.strip('"')
		#self.args.nls_timestamp_format=self.args.nls_timestamp_format.strip('"')
		#self.args.nls_timestamp_tz_format=self.args.nls_timestamp_tz_format.strip('"')
		host_map_loc= self.args.host_map
		
		#print dir(conf)
		self.hm = hmap(self.args.copy_vector.split(self.conf._to),host_map_loc)		
		self.TT=self.args.truncate_target
		self.T=True
		self.P=False
		if hasattr(self.args, 'to_partition') and self.args.to_partition:
			self.P=True
		self.SP=False
		if hasattr(self.args, 'to_sub_partition') and self.args.to_sub_partition:
			self.SP=True
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir) 
	def if_truncate(self,msg, obj):
		if self.args.ask_to_truncate:
			var = raw_input('Do you want to truncate %s "%s"?(y/n): ' % (msg,obj))
			if var.upper() not in ('Y','N','YES','NO'):
				self.log.info('Exiting...')
				e(0)
			if var.upper() in ('N','NO'):
				self.log.info('Exiting...')
				e(0)
		return True
		
	def truncate_target(self):

			
		if self.SP:
			assert self.to_table, 'Table is not set'
			self.log.warn('Target is subpartition.')
			self.truncate_subpartition()
		elif self.P:
			assert self.to_table, 'Table is not set'
			self.log.warn('Target is partition.')
			self.truncate_partition()
		elif self.T:
			assert self.to_table, 'Table is not set'
			self.log.warn('Target is table.')
			self.truncate_table()
		#e(0)
	def truncate_table(self):
		
		if self.if_truncate('table',args.to_table.upper()):
			print ''
			self.log.warn('Truncating table %s' % self.args.to_collection)
			q='TRUNCATE TABLE %s;\nexit;\n' % self.args.to_collection
			qfn=self.save_qry('truncate_table_%s' % self.args.to_collection,q)		
			(r_int, status, err)=self.uargs_db.do_query(self.login, query=None,query_file=qfn)
			self.log.info(os.linesep.join(r_int))
	def truncate_partition(self):
		
		if self.if_truncate('partition',args.to_partition.upper()):
			print ''
			self.log.warn('Truncating partiton %s' % self.args.to_partition)
			q='ALTER TABLE %s TRUNCATE PARTITION %s;\nexit;\n' % (self.args.to_collection,args.to_partition)
			qfn=self.save_qry('truncate_partition_%s.%s' % (self.args.to_collection,args.to_partition),q)		
			(r_int, status, err)=self.uargs_db.do_query(self.login, query=None,query_file=qfn)
			self.log.info(os.linesep.join(r_int))		
	def truncate_subpartition(self):
		
		if self.if_truncate('sub-partition',args.to_sub_partition.upper()):
			print ''
			self.log.warn('Truncating sub-partiton %s' % self.args.to_sub_partition)
			q='ALTER TABLE %s TRUNCATE SUBPARTITION %s;\nexit;\n' % (self.args.to_collection,args.to_sub_partition)
			qfn=self.save_qry('truncate_sub_partition_%s.%s' % (self.args.to_collection,args.to_sub_partition),q)		
			(r_int, status, err)=self.uargs_db.do_query(self.login, query=None,query_file=qfn)
			self.log.info(os.linesep.join(r_int))		
	def print_copy_details(self):	
		trunc=''
		if self.TT:
			trunc="""
    TTTTTT  RRRRR   UU  UU  NN  NN   CCCCC    AA    TTTTTT  EEEEEE
      TT    RR  RR  UU  UU  NNN NN  CC       AAAA     TT    EE
      TT    RRRR    UU  UU  NN NNN  CC      AA  AA    TT    EEEE
      TT    RR  RR  UU  UU  NN  NN  CC      AAAAAA    TT    EE
      TT    RR  RR   UUUU   NN  NN   CCCCC  AA  AA    TT    EEEEEE"""
		print """		
To %s:	
	to db: %s@%s
	to table: %s
	%s""" % (conf.dbs[self.db],self.login.split('/')[0],self.login.split('@')[1],self.to_table,trunc)
		print """
	Logging to:
%s\n""" % self.uargs.logdir
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['SPOOLER'][self.db])
		if self.args.target_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['SPOOLER'][self.db]
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to source loader is not set. Defaulting to %s' % loader)	
		return self.db_client_loc
	def get_db_client_dbshell(self):
		assert self.args.target_client_home, 'self.args.target_client_home is not set'
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(conf.dbtools['DBSHELL'][self.db])
		if self.args.target_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=conf.dbtools['DBSHELL'][self.db]
			print self.db_client_dbshell,self.db
			print self.args.target_client_home
			e(0)
			
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %s' % loader)	
		return self.db_client_dbshell
	def get_db_client_loader(self):
		if self.db_client_loader:
			return self.db_client_loader
		loader= os.path.basename(conf.dbtools['LOADER'][self.db])
		if self.hm.local_target_client_home:
			self.db_client_loader=(r'%s\%s' % (self.hm.local_target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loader=conf.dbtools['LOADER'][self.db]
			if not os.path.isfile(self.db_client_loader):
				self.log.warn('Path to source loader is not set. Defaulting to %s' % loader)	
		return self.db_client_loader			
	def set_payload(self,shard,num_of_shards, qname=None):
		#options={'_PARTITION':pt}
		tabname= self.to_table
		if self.to_table:
			return (self.login, self.to_table) 	
		else:
			assert qname, 'Query name should be set if table name is not defined.'
			q=qname.split('.')
			assert len(q)>2, 'Wrong query file name format "%s".\nShould be: TOSCHEMA.TOTABLE.id.sql' % qname #;TOPART;TOSUBPART
			schema,table=q[:2]
			#t=tab.split(';')
			
			return (self.login, '.'.join([schema,table])) 	
			
				
	def load_data(self,logger,loadConf,outfn,shard):
		return self.uargs_db.load_data(logger,loadConf,outfn,shard)

	def get_load_config(self,to_pld):
		#pprint(to_pld)
		(_, _, shard_name,outfn,row_from, row_to)=to_pld
		#shard=shard_name.split('-')[1]
		#pprint (to_pld)
		#ctlfn= self.uargs_db.save_ctl(to_table,shard)
		
		db_loader_loc=self.get_db_client_loader()
		loadConf=self.uargs_db.get_load_config(db_loader_loc,shard_name,row_from, row_to,None,outfn,self.datadir)
			
		#pprint(loadConf)
		#sys.exit(1)
		
		return loadConf		

	def get_tab_shards_dbms(self,log,nosh,from_db,from_t,options):
		p= options.get('_PARTITION')
		#datadir = options.get('datadir')
		#pprint(p)
		#sys.exit(1)
		prtn =''
		if p:
			prtn = "AND SUBOBJECT_NAME = '%s'" % p
		#sys.exit(1)
		q="""set pagesize 0 feedback off TIMING OFF
	select distinct grp||'||'||min_rid||'||'||max_rid||'||'||SUBOBJECT_NAME cln
	FROM (
	SELECT DBMS_ROWID.rowid_create (1,
								data_object_id,
								lo_fno,
								lo_block,
								0
							   ) min_rid,
	   DBMS_ROWID.rowid_create (1,
								data_object_id,
								hi_fno,
								hi_block,
								100
							   ) max_rid,grp,SUBOBJECT_NAME
	FROM (SELECT DISTINCT grp,
						FIRST_VALUE (relative_fno) OVER (PARTITION BY grp ORDER BY relative_fno,
						 block_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
																	   lo_fno,
						FIRST_VALUE (block_id) OVER (PARTITION BY grp ORDER BY relative_fno,
						 block_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
																	 lo_block,
						LAST_VALUE (relative_fno) OVER (PARTITION BY grp ORDER BY relative_fno,
						 block_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
																	   hi_fno,
						LAST_VALUE (block_id + blocks - 1) OVER (PARTITION BY grp ORDER BY relative_fno,
						 block_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
																	 hi_block,
						SUM (blocks) OVER (PARTITION BY grp) sum_blocks
				   FROM (SELECT   segment_name, relative_fno, block_id,
								  blocks,
								  TRUNC
									  (  (  SUM (blocks) OVER (ORDER BY relative_fno,
											 block_id)
										  - 0.01
										 )
									   / (SUM (blocks) OVER () / %d)
									  ) grp
							 FROM dba_extents
							WHERE segment_name =
											 UPPER ('%s')
							  AND owner = '%s'
						 ORDER BY block_id)),
	   (SELECT data_object_id, SUBOBJECT_NAME
		  FROM all_objects
		 WHERE object_name = UPPER ('%s') and owner='%s' and data_object_id is not null  %s)
	);
	exit;
	""" % (nosh,from_t[1],from_t[0],from_t[1],from_t[0],prtn)
		#print q
		#sys.exit(1)
		regexp=re.compile(r'(.*)')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		assert from_db, 'TO_DB is not set.'
		#opt='set echo off pagesize 0 serveroutput off feedback off termout off\n'
		opt=''
		#print q
		#sys.exit(1)
		cqdir='%s\\sql' % (self.datadir)
		#to_table='Persons_pipe2'
		cqfn='%s\\sharding_%s.sql' % (cqdir,from_t[1])
		#to_tab='Persons_pipe'
		#to_schema='SCOTT'
		#conn=('XE', 'SCOTT', 'TIGER')
		
		cqf = open(cqfn, "w")
		cqf.write(q)
		cqf.close()
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		(r_int, status)=self.uargs_db.do_query(from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r)
		#t= 
		#sys.exit(1)
		return (r_int, status)
	
