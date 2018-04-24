import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_exadata import Exadata
import codecs, tempfile
from pprint import pprint
class ToExadata(Exadata):
	"""Exadata db"""
	def __init__(self,parent,log,login,to_table,datadir,args):
		self.log=log
		self.login=login
		self.to_table=to_table
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.field_term=args.field_term
		#self.wait_sec=int(args.wait_limit_sec)
		self.datadir=datadir
		self.to_pld={}
		self.tab_cols={}
		self.args=args
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir) 		
	def print_copy_details(self):		
		print """		
	To Exadata:	
		to db: %s
		to table: %s
		""" % (self.login,self.to_table)
		
	def set_payload(self,shard,num_of_shards):
		#options={'_PARTITION':pt}
		
		return (self.login, self.to_table) 	

	def load_data(self,logger,loadConf,outfn,shard):
		out=[]
		err=[]
		#print loadConf
		#sys.exit(0)
		os.environ['NLS_DATE_FORMAT'] = self.args.nls_date_format
		#os.environ['NLS_TIME_FORMAT'] = "HH24.MI.SS"
		os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_datetime_format
		
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
		#sys.exit(0)
		#return (out,status,err)
		return (out,status,err,ins_cnt)	
	def get_load_config(self,to_pld):
		#(shard_name,from_pld,to_pld)=payload
		#pprint(to_pld)
		#sys.exit(1)
		#(shard_name, outfn) =to_pld[:2]
		#print shard_name, outfn
		#sys.exit(1)
		#pprint(to_pld)
		(login, to_table, shard_name,outfn,row_from, row_to)=to_pld
		shard=shard_name.split('-')[1]
		ctlfn= self.save_ctl(to_table,shard)
		
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
			
		loadConf=['sqlldr', 'control=%s' % ctlfn, 'userid=%s' % login, #'ROWS=%s' % dpl_rows,
		'DATA=%s' % outfn,
		'COLUMNARRAYROWS=%s' % dpl_columnarrayrows,#'size=10000',
		'STREAMSIZE=%s' % dpl_streamsize,'READSIZE=%s' % dpl_readsize,
		'PARALLEL=%s' % if_dpl_parallel,
		'BINDSIZE=%s' % dpl_bindsize, #' UNRECOVERABLE=Y ', 
		'SKIP_INDEX_MAINTENANCE=%s' % dpl_skip_index_maintenance, 'SKIP_UNUSABLE_INDEXES=%s' % dpl_skip_unusable_indexes,
		'DIRECT=%s' % if_direct, #"data=\'-\'",
		'MULTITHREADING=TRUE', #'EXTERNAL_TABLE=EXECUTE',
		'LOG=%s/sqlloader/%s%s_%s.log' % (self.datadir,to_table, "%s%s" % (ptn,sptn),shard_name), 'BAD=%s/sqlloader/%s%s_%s.bad' % (self.datadir,to_table, "%s%s" % (ptn,sptn),shard_name),
		'DISCARD=%s/sqlloader/%s%s_%s.dsc' % (self.datadir,to_table, "%s%s" % (ptn,sptn),shard_name),				
		#'ROWS=%s' % dpl_rows,
		
		'ERRORS=%s' % loader_errors]
		if row_from:
			loadConf.append('SKIP=%s' % (row_from-1))
		if row_to:
			loadConf.append('LOAD=%s' % (row_to-row_from))
			
		#pprint(loadConf)
		#sys.exit(1)
		
		return loadConf		
	def get_inserted_count(self,shard):
		ptn=''
		sptn=''
		
		logfn='%s\\%s%s_Shard-%s.log' % (self.ctldir,self.to_table, "%s%s" % (ptn,sptn),shard)

		rows_copied=-1
		#print logfn
		if not os.path.isfile(logfn):
			self.log.error('Log file for shard %d is missing.' % shard)
		else:
			shl=open(logfn, 'r').read()

			r=re.compile(r'(\d+) Rows successfully loaded\.')

			g=re.search(r,shl)
			if g:
				rows_copied=int(g.groups()[0])
				#rows_total +=rows_copied
				#print rows_total
		#print rows_copied
		return rows_copied
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
		(r_int, status)=self.do_query(log,from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r)
		#t= 
		#sys.exit(1)
		return (r_int, status)
	
