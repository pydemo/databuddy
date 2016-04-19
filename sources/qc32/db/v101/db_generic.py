import types, re, os, sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
#import common.v101.config as conf 
import config.config as conf
from pprint import pprint
import shlex
e=sys.exit
class GenericDb(base):
	"""Oracle db"""
	def __init__(self,log, datadir,login, conf):
		base.__init__(self, log)
		self.log=log
		self.login=login
		#self.from_table=from_table
		self.datadir=datadir
		self.tab_cols={}
		self.to_pld={}
		self.db_client_loc=None	
		self.db_client_dbshell=None	
		self.db_client_loader=None
		self.conf=conf
		self.dbg=0
		if conf.args.debug_level:
			self.dbg=int(conf.args.debug_level)		
		#self.args.nls_date_format=conf.args.nls_date_format.strip('"')
		#self.args.nls_timestamp_format=conf.args.nls_timestamp_format.strip('"')
		#self.args.nls_timestamp_tz_format=conf.args.nls_timestamp_tz_format.strip('"')
		#print self.uargs.db
		
		
	def set_payload2(self,num_of_shards):
		#options={'_PARTITION':pt}
		options={}
		(shards, status)=self.get_tab_shards_dbms(self.log,num_of_shards, self.login, self.from_table.split('.'),options)
		qry='SELECT * FROM %s' % self.from_table
		(cols_from,status) = self.get_query_columns(self.log,self.login, qry)


		from_pld=[]		
		#globalStatus={}
		
		for i in range(len(shards)):
			#sys.exit(1)
			(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
			if 1:
				ctlfn= self.save_ctl(self.from_table,i)
			
			if 1:	
			
				from_pld.append((rowid_from,rowid_to,ctlfn,self.login,self.from_table,cols_from))

				#globalStatus[i]=(99, None)	
		return (shards,from_pld) 
	def get_tab_shards_dbms(self,nosh,from_db,from_t):

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
		 WHERE object_name = UPPER ('%s') and owner='%s' and data_object_id is not null)
	);
	exit;
	""" % (nosh,from_t[1],from_t[0],from_t[1],from_t[0])
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
		(r_int, status, err)=self.uargs_db.do_query(from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r)
		#t= 
		#sys.exit(1)
		return (r_int, status)
	def get_part_tab_shards_dbms(self,nosh,from_db,from_t):

		prtn =self.args.from_partition

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
	FROM (SELECT DISTINCT grp,PARTITION_NAME,
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
				   FROM (SELECT   segment_name, relative_fno, block_id,PARTITION_NAME,
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
							  AND UPPER(PARTITION_NAME)=UPPER('%s')
						 ORDER BY block_id)),
	   (SELECT data_object_id, SUBOBJECT_NAME
		  FROM all_objects
		 WHERE object_name = UPPER ('%s') and owner='%s' and data_object_id is not null  AND UPPER(SUBOBJECT_NAME) = UPPER('%s'))
		 WHERE PARTITION_NAME=SUBOBJECT_NAME
	);
	exit;
	""" % (nosh,from_t[1],from_t[0],self.args.from_partition,from_t[1],from_t[0],prtn)
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
		(r_int, status, err)=self.uargs_db.do_query(from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r)
		#t= 
		#sys.exit(1)
		return (r_int, status)
	def get_subpart_tab_shards(self,nosh,from_db,from_t):

		prtn =self.args.from_sub_partition
		#if p:
		#	prtn = "AND SUBOBJECT_NAME = '%s'" % p
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
	FROM (SELECT DISTINCT grp,PARTITION_NAME,
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
				   FROM (SELECT   segment_name, relative_fno, block_id,PARTITION_NAME,
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
							  AND UPPER(PARTITION_NAME)=UPPER('%s')
						 ORDER BY block_id)),
	   (SELECT data_object_id, SUBOBJECT_NAME
		  FROM all_objects
		 WHERE object_name = UPPER ('%s') and owner='%s' and data_object_id is not null  AND UPPER(SUBOBJECT_NAME) = UPPER('%s'))
		 WHERE PARTITION_NAME=SUBOBJECT_NAME
	);
	exit;
	""" % (nosh,from_t[1],from_t[0],self.args.from_sub_partition,from_t[1],from_t[0],prtn)
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
		(r_int, status, err)=self.uargs_db.do_query(from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r_int)
		#t= 
		#sys.exit(1)
		return (r_int, status)	
	def get_spool_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		#if not os.path.isdir(datdir):
		#	os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)	
		
	


		
	def get_log_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		if not os.path.isdir(datdir):
			os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)
	def get_spool_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		#if not os.path.isdir(datdir):
		#	os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)		


	def get_query_columns(self,log,login,  qry):
		#assert self._pp.get('FROM_SCHEMA'), 'FROM_SCHEMA is not set'
		#t= list((from_schema, get_temp_table_name()))
		#col_key = self.get_cc_key((login, t))
		#print 'col_key = ',col_key
		#if not self._ci.has_key(col_key):
		#	self._ci[col_key]={}
		#pprint(self._ci)
		self.log.info('Fetching column info...')
		if 1: #len(self._ci[col_key])==0:
			"""['ASET_LVL_0_DESC:120:VARCHAR2',
	'ASET_LVL_1_DESC:120:VARCHAR2',
	'ASET_LVL_2_DESC:120:VARCHAR2',
	'ASET_LVL_KEY:180:VARCHAR2',
	'BLTR_CD:10:VARCHAR2',
			"""
			#print len(qry[70000:100000])
			#sys.exit(1)
			q="""
	set serveroutput on echo on termout on feedback off timing off
	DECLARE
	c           NUMBER;
	d           NUMBER;
	col_cnt     INTEGER;
	f           BOOLEAN;
	rec_tab     DBMS_SQL.DESC_TAB;
	col_num    NUMBER;
	v_sql dbms_sql.varchar2a;
	v_sql_1 varchar2(32767);
	v_sql_2 varchar2(32767);
	v_sql_3 varchar2(32767);
	v_sql_4 varchar2(32767);
	v_type VARCHAR2(32):='';
	PROCEDURE print_rec(rec in DBMS_SQL.DESC_REC) IS
	BEGIN
	v_type:=CASE rec.col_type
				WHEN 1 THEN 'VARCHAR2'
				WHEN 12 THEN 'DATE'
				WHEN 2 THEN 'NUMBER'
				WHEN 180 THEN 'TIMESTAMP'
			ELSE ''||rec.col_type
			END;
	DBMS_OUTPUT.PUT_LINE(rec.col_name||':'||rec.col_name_len||':'||v_type);
	END;
	BEGIN
	v_sql(1):='%s';
	v_sql(2):='%s';
	v_sql(3):='%s';
	v_sql(4):='%s';
	v_sql(5):='%s';
	c := DBMS_SQL.OPEN_CURSOR;
	DBMS_SQL.PARSE(c, v_sql,1,5,False, DBMS_SQL.NATIVE);
	d := DBMS_SQL.EXECUTE(c);
	DBMS_SQL.DESCRIBE_COLUMNS(c, col_cnt, rec_tab);
	/*
	* Following loop could simply be for j in 1..col_cnt loop.
	* Here we are simply illustrating some of the PL/SQL table
	* features.
	*/
	col_num := rec_tab.first;
	IF (col_num IS NOT NULL) THEN
	LOOP
	  print_rec(rec_tab(col_num));
	  col_num := rec_tab.next(col_num);
	  EXIT WHEN (col_num IS NULL);
	END LOOP;
	END IF;
	DBMS_SQL.CLOSE_CURSOR(c);
	END;
	/
	exit;

	""" % (qry[0:32000].replace("'","''"),qry[32000:64000].replace("'","''"),qry[64000:96000].replace("'","''"),qry[96000:128000].replace("'","''"),qry[128000:160000].replace("'","''"))
			regexp=re.compile(r'([\w\_\:\(\)\d]+)')
			#regexp=re.compile(r'(.*)')
			#print(q);
			#sys.exit(1)
			qfn=self.save_qry('get_query_columns',q)
			(r, status,err)=self.uargs_db.do_query(login, query=None,query_file=qfn,regexp=regexp)

			if not status:
				if len(r)==0:
					status=2
					print 'Table %s doesn\'t exist in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login))
					#self._logger.fatal('Table %s doesn\'t exist1 in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login)))
			#r.sort()
			#self._ci[col_key]=r	
			#pprint(r)
			#sys.exit(1)
			self.log.info('Done.')
			return (r,status)
		else:
			return (self._ci[col_key],0)
	def ckey2cols(self, col_key):
		return map(lambda x: x[0].split(':')[0],col_key)
	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
		

	def do_query2(self, login, query, query_file=None, regexp=None, grp=None, spset=''):
		f = ""
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(login)>0, 'Default login is not set.'
		show=False
		if type(login) == types.TupleType:
			to_tab=login[1]
			login=login[0]
			#query = string.replace ()
			#sys.exit(1)
		else:
			pass
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''

			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q = "%s\n%s\n%s" % ( spset,opt,query)
				#q = "%s" % ( query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q,'<'
			p1 = Popen(['echo', q.replace('\n','')], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				while output:
					output = p1.stdout.readline()
					#print output
				sys.exit(0)
			p2 = Popen([ 'sqlplus', "-S", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE)
			output=' '
			status=0
			while output:
				output = string.replace(p2.stdout.readline(),'SQL>','')
				#print output
				#err.append(output)
				if regexp:
					#print regexp
					m = re.match(regexp, output) 
					if m:
						if grp:
							out.append(m.group(grp))
						else:
							groups=m.groups()
							if groups:
								if groups[0]:
									out.append(groups)
							#self._logger.info(output.rstrip())
						#else out.append(m.group(grp))
				else:
					out.append(output)
					if show:
						#print output,
						self._logger.info(output.rstrip())	
				if errpos>-1:
					self._logger.error(output.rstrip())	
					status=1					
				#errpos=output.find('ERROR') 
				#print  output.find('2COLUMN.')
				if output.find('COLUMN.')==-1:
					errpos=output.find('ERROR ')
					#print "%s, %s ,%s" % (errpos, output, output.find('COLUMN.'))
					if errpos>-1:
						status=1
						
						#self._logger.error(output.rstrip())	
					
			pstatus=p2.wait()
			er='none.'
			if pstatus:
				while er:
					er = p2.stderr.readline()
					if er:
						print 'P2-ERROR: ',er
				
			if int(status)+int(pstatus)>0:
				print 'error', status,pstatus
				#self._logger.error(string.join(err,'\n'))	
			if status!=0:
				return (err,status)
		#print "====================", out,status
		return (out,status+pstatus)		

	def get_ctl_filler(self, to_tab, r_int, dpl_mode, term):
		(line_term,field_term) =term
		part = ''
		if 0:
			if self.is_set('PARTITION'):
				if self._pp.has_key('TO_PARTITION'):
					to_part = self._pp.get('TO_PARTITION')
					if to_part:
						part = 'PARTITIOn (%s)' % to_part
					else:
						pass
				else:
					part = 'PARTITION (%s)' % self.p('PARTITION')
			unrec = ''
			if self.p_if('IF_UNRECOVERABLE'):
				unrec = 'UNRECOVERABLE'	
		unrec = 'UNRECOVERABLE'				
		tmpl="""%s
	LOAD DATA
	INFILE '-' "str '%s\n'"
	%s
	INTO TABLE %s %s
	FIELDS TERMINATED BY '%s'
	TRAILING NULLCOLS
	(C_FILLER FILLER,
	 %s)""" % (unrec,line_term,dpl_mode,to_tab, part, field_term, ','.join(r_int))
		#pprint(tmpl)
		#pprint(r_int)
		#sys.exit(1)
		return tmpl	

	def do_query_new(self,logger,login, query, query_file=None, regexp=None, grp=None, spset=''):
		f = ""
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(login)>0, 'Default login is not set.'
		show=False
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q = "%s%s" % ( opt,query)

			if 1:
				#print login
				#print query_file
				#print q
				#@C:\Python27\data_mule_sqllite\logs\20141016_145220\sql\sharding_Persons_pipe_datetime_1.sql
				#sys.exit(0)
				#assert os.path.isfile(query_file), 'Query file does not exists!'
				#db_client_loc=self.get_db_client_loc()
				#print os.path.dirname(db_client_loc)
				db_client_dbshell= self.get_db_client_dbshell()
				cfg=[ db_client_dbshell, login]
				#pprint(cfg)
				#cmdList=shlex.split(''.join(cfg))
				#pprint(cmdList)
				#if self.args.nls_date_format:
				#	os.environ['NLS_DATE_FORMAT'] = self.args.nls_date_format
				#if self.args.nls_timestamp_format:
				#	os.environ['NLS_TIMASTAMP_FORMAT'] = self.args.nls_timestamp_format
				p2 = Popen(cfg,  stdout=PIPE, shell=True  ) # '-S',  stdin=p1.stdout,
				#print query
				qry='set serveroutput on echo on termout on feedback on timing off\nSELECT * FROM DUAL;\n'
				#print qry
				output, err = p2.communicate(qry)
				#print output
				#print err
				
				if err:
					self.log.err(err)
				status=p2.wait()
				sys.exit(1)
				

				
	def do_query_uargs(self,logger,login, query, query_file=None, regexp=None, grp=None, spset=''):
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
