import types, re, os, sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
class Mysql(base):
	"""Oracle db"""
	def __init__(self,log,login,from_table, datadir):
		base.__init__(self, log)
		self.log=log
		self.login=login
		self.from_table=from_table
		self.datadir=datadir
		self.tab_cols={}

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
	set serveroutput on echo on termout on feedback off
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
			(r, status)=self.do_query(log,login, query=None,query_file=qfn,regexp=regexp)
			if 0:
				(r,status) = do_query(login, 
				#"set echo off pagesize 0 serveroutput off feedback off termout off\n%s" 
				'set serveroutput on echo on termout on feedback off\n%s'% q,0,regexp,1)
				#pprint(r)
			
			#print t, col_key 
			#sys.exit(1)
			if not status:
				if len(r)==0:
					status=2
					print 'Table %s doesn\'t exist1 in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login))
					#self._logger.fatal('Table %s doesn\'t exist1 in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login)))
			#r.sort()
			#self._ci[col_key]=r	
			#pprint(r)
			#sys.exit(1)
			return (r,status)
		else:
			return (self._ci[col_key],0)

	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
		

	def get_table_columns(self, tab_name):
		if self.tab_cols.has_key(tab_name):
			return self.tab_cols[tab_name]
		else:
			qry="""
			set pagesize 0 feedback off TIMING OFF
			SELECT COLUMN_NAME||':'||DATA_LENGTH||':'||DATA_TYPE
			FROM ALL_TAB_COLUMNS WHERE OWNER=UPPER('%s') AND TABLE_NAME=UPPER('%s')
			ORDER BY COLUMN_ID;
			exit;
			""" % tuple(tab_name.upper().split('.'))
			#print qry
			cqfn=self.save_qry('get_table_columns',qry)
			(r_int, status)=self.do_query(self.log,self.login, query=None,query_file=cqfn)

			self.tab_cols[tab_name] = map(self.coldef, r_int)
			return self.tab_cols[tab_name]


	def do_query(self,logger,login, query, query_file=None, regexp=None, grp=None, spset=''):
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
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q = "%s;%s" % ( opt,query)

			if 0:
				while output:
					output = string.replace(p1.stdout.readline(),'SQL>','')
					#print output
				pstatus=p1.wait()
				#print pstatus
				return ([],0)				
			else:
				#print login
				#print query_file
				#print q
				#sys.exit(0)
				p2 = Popen([ 'sqlplus',"-S", login,'@%s' %  query_file],  stdout=PIPE,stderr=PIPE)
				output=' '
				status=0
				er='none'
				if 0:
					while er:
						er = p2.stderr.readline()
						print er
						if er:
							logger.error(er)
				error=False
				while output:
					output = p2.stdout.readline() #string.replace(p2.stdout.readline(),'SQL>','')
					#print output
					if output.strip():
						out.append(output.strip())
						if 'ERROR' in output.upper():
							error=True
						if error:
							print output.strip()
					if 0:
						if not output.startswith('SP2-'):
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
									print output.strip()
									#self._logger.info(output.rstrip())	
							if errpos>-1:
								#self._logger.error(output.rstrip())	
								status=1					
							#errpos=output.find('ERROR') 
							#print  output.find('2COLUMN.')
							if output.find('COLUMN.')==-1:
								errpos=output.find('ERROR ')
								#print "%s, %s ,%s" % (errpos, output, output.find('COLUMN.'))
								if errpos>-1:
									status=1
								
								#self._logger.error(output.rstrip())	
				er='none.'
				if 1:
					while er:
						er = p2.stderr.readline()
						if er:
							print 'P2-ERROR: ',er				
				pstatus=p2.wait()
				#sys.exit(1)
				#print 'pstatus=',pstatus
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