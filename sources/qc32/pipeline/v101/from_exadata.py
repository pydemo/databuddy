import types, re, os,sys
#from subprocess import Popen, PIPE
from db.v101.db_exadata import Exadata
from subprocess import Popen, PIPE
#import db.v101.db_sqlserver as db2
from pprint import pprint
import string
#import codecs, tempfile

class FromExadata(Exadata):
	"""Exadata db"""
	def __init__(self,parent,log,login,from_table, datadir,args):
		self.log=log
		self.login=login
		self.from_table=from_table
		self.datadir=datadir
		#self.nlsdf=args.nls_date_format
		#self.nlstf=args.nls_time_format
		self.args=args
		self.tab_cols={}
		self.ctldir='%s/sqlloader' % self.datadir
		self.from_tab_cols={}
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir) 
	def print_copy_details(self):		
		print """		
	From Exadata:	
		from db: %s
		from table: %s
		""" % (self.login,self.from_table)
	def get_firstrow(self):
		return 1	

	def set_payload(self,num_of_shards):
		#options={'_PARTITION':pt}
		options={}
		(shards, status)=self.get_tab_shards_dbms(self.log,num_of_shards, self.login, self.from_table.split('.'),options)
		assert shards, 'Cannot create source table %s shards.' % self.from_table
		qry='SELECT * FROM %s' % self.from_table
		#print qry
		(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
		assert cols_from, 'Cannot fetch source query columns'
		from_pld=[]		
		#globalStatus={}
		
		for i in range(len(shards)):
			#sys.exit(1)
			#print shards
			(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
			#if 1:
			#	ctlfn= self.save_ctl(self.from_table,i)
			
			if 1:	
				outfn=self.get_outfn(i)
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,None))

				#globalStatus[i]=(99, None)	
		#print from_pld
		#sys.exit(1)
		return (shards,from_pld) 
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, 0,0)
	def spool_source_data(self,outfn, spConf, payload):
		(shard_name,from_pld,to_pld)=payload
		#(rowid_from,rowid_to,ctlfn,from_db,from_table,cols_from)=from_pld
		#shard=shard_name.split('-')[1]
		#outfn='%s\\shard_%s.data' % (self.datadir,shard)
		#outfn=r'C:\Python27\ora2ss_data_pipe\data\\shard_%s.data' % shard
		outf=open(outfn, "w")
		#pprint (spConf)
		#print outfn
		os.environ['NLS_DATE_FORMAT'] = self.args.nls_date_format
		os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
		p2 = Popen(spConf,  stdout=outf) # '-S',  stdin=p1.stdout, stdout=outf
		#status=p2.wait()
		#pprint(dir(outf))
		#outf.flush()
		#outf.flush()
		#os.fsync(outf)
		output, err = p2.communicate()
		#print output
		#print err
		if err:
			self.log.err(err)
		status=p2.wait()
		outf.close()
		#time.sleep(1)
		if 0:
			if p2.stdout:
				output=' '
				while output:
					output = p2.stdout.readline()
					print output
				#status=p2.wait()
		#sys.exit(1)
		count=-1
		if 1:
			#print 'spooled %d B' % stat
			import io
			#file = open(outfn,  mode='r+')
			file = io.open(outfn, 'r+', encoding = 'utf-8')

			file.seek(0, os.SEEK_END)
			pos = file.tell() - 3
			char=file.read(1)
			eol=char != "\n"	
			nums=[str(i) for i in range(0,10)]
			#print nums
			cnt=[]
			while pos > 0 and eol:
				#pprint(file.read(1))
				pos -= 1
				file.seek(pos, os.SEEK_SET)
				char=file.read(1)
				eol=char != "\n"
				#pprint(char)
				#print 1,pos


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
			eol=char != "\n"	
			while pos > 0 and eol:
				
				pos -= 1
				file.seek(pos, os.SEEK_SET)
				char=file.read(1)
				eol=char != "\n"
				#pprint(char)				
				if char in nums:
					cnt.append(char)
				#print 3,pos, char, ord(char)
			#print 'last',pos			
			if pos > 0:
				pos -= 2
				file.seek(pos, os.SEEK_SET)
				#pprint(file.read(1))
				#print 'truncate'
				file.truncate()
			count=int( ''.join(cnt[::-1]))
			file.close()
			#print ord('0'),  ord('9')

			#stat=os.stat(outfn).st_size		
		
		return (count, status)
		
	def get_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.limit)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		qry = "SELECT * FROM %s WHERE ROWID BETWEEN '%s' AND '%s' %s" % (self.from_table,rowid_from,rowid_to,lim) #AND ROWNUM<1000
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from
		status=None
		if self.from_tab_cols.has_key(self.from_table):
			(r_from,status)=self.from_tab_cols[self.from_table]
		else:
			self.from_tab_cols[self.from_table]=(r_from,0)
		from_schema=self.from_table.split('.')[0]
		if len(self.from_table.split('.'))!=2:
			from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		from_t= list((from_schema, tempt))
		
		if not status:
			ft = field_term 
			lt = '' 

			ca=self.ckey2cols(r_from)
			cl =  "%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			llen=32767
			orderby=''
			q=''
			if 0: #column word_wrapped
				wwp = "COLUMN %s WORD_WRAPPED\n" % string.join(ca,' WORD_WRAPPED\n COLUMN ')
				q= "%s set head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nalter session set NLS_DATE_FORMAT='DD-MON-RR HH.MI.SS'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='yyyy/mm/dd hh24:mi:ss'\n/\nSELECT /*+PARALLEL1(%s)*/ %s FROM %s %s;\nexit;\n" % (wwp, llen,   from_t[1], cl, string.join(get_from_tab(from_t),'.'), get_q_options(self._pp))
			else:
				q= "set timing off head off line %s pages 0 newpage 0 echo off feedback off define off  arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET hash_area_size = 524288000\n/\nalter session set NLS_DATE_FORMAT='%s'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='%s'\n/\nset feedback on\nSELECT %s FROM (%s) %s %s;\nexit;\n" % (llen,  self.args.nls_date_format,self.args.nls_timestamp_format,  cl, qry, ' ',orderby)
				#q= "set head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET sort_hash_size = 524288000\n/\nalter session set NLS_DATE_FORMAT='DD-MON-RR HH.MI.SS AM'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp,{'_PARTITION':self._pp.get('PARTITION',None)}),orderby)
				#q= "set line %s arraysize 5000\nalter session set NLS_DATE_FORMAT='DD-MON-YY'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp))
			#set timing off pagesize 0 heading off line 2000 long 128000  feedback off\ncolumn object_ddl format a121 word_wrapped
			tab= string.join(from_t,'.')
			sqfn=self.save_qry('spool_sql_%s' % shard_name,q)
			
			#abspath= os.path.abspath(os.path.dirname(sys.argv[0]))
			spConf=[ 'sqlplus','-S','%s' % (self.login),'@%s' % sqfn]
		return spConf
	def get_tab_shards_dbms2(self,log,nosh,from_db,from_t,options):
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
	
	