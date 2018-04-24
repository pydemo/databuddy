import types, re, os,sys
#from subprocess import Popen, PIPE
#from db.v101.db_oracle import Oracle
from db.v101.db_generic import GenericDb
from subprocess import Popen, PIPE
#import db.v101.db_sqlserver as db2
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
from common.v101.exceptions import RowCountError
import string
import pprint as pp
from include.v101.host_map import host_map as hmap
#import codecs, tempfile
e=sys.exit

class FromDb(GenericDb):
	"""Oracle db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.args.from_db='%s/%s@%s' % (self.args.from_user,self.args.from_passwd,self.args.from_db_name)
		GenericDb.__init__(self,log,datadir,self.args.from_db,conf) 
		self.log=log
		
		self.login=self.args.from_db
		self.from_table=self.args.from_table
		self.datadir=datadir
		self.db=db
		
		self.uargs_db=self.uargs.source.source(self.log,datadir,self.login,self.conf,db,self.args.from_table)
		self.uargs_common=self.uargs.source.common(datadir,self.login,self.conf)
		#print self.uargs_db
		#e(0)
		#self.nlsdf=args.nls_date_format
		#self.nlstf=args.nls_time_format
		self.args.nls_date_format=self.args.nls_date_format.strip('"')
		self.args.nls_timestamp_format=self.args.nls_timestamp_format.strip('"')
		self.args.nls_timestamp_tz_format=self.args.nls_timestamp_tz_format.strip('"')
		#self.args=args
		self.tab_cols={}
		#self.ctldir='%s/sqlloader' % self.datadir
		self.from_tab_cols={}
		self.from_query=[]
		self.new_query=[]
		self.shards=[]
		self.from_pld=[]
		self.spConf=[]
		self.from_query_name=[]
		self.cols_from=None
		self.kW=self.args.keep_whitespace
		self.V=self.args.validate
		host_map_loc= self.args.host_map
		self.hm = hmap(self.args.copy_vector.split(self.conf._to),host_map_loc)
		self.H=self.args.header
		self.Sh=self.args.num_of_shards>1
		#print self.args.num_of_shards
		#e(0)
		self.db_client_loc=self.get_db_client_loc()
		#if not os.path.isdir(self.ctldir):
		#	os.makedirs(self.ctldir) 
		self.T, self.P, self.SP, self.QF, self.QD =(False, False, False, False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
			if hasattr(args, 'from_partition') and self.args.from_partition:
				assert not self.args.from_sub_partition, 'Set Partition or Subpartition but not both.'
				self.P=True
			elif hasattr(args, 'from_sub_partition') and self.args.from_sub_partition:				
				self.SP=True
		else:

			assert self.args.query_sql_file or self.args.query_sql_dir, 'Either query file or query dir has to be set.'
			if self.args.query_sql_file:
				self.QF=True
				assert os.path.isfile(self.args.query_sql_file), 'Query file "%s" does not exists.' % self.args.query_sql_file		
				qry=open(self.args.query_sql_file).read().strip().strip(';')
				self.from_query.append(qry)
				qf=os.path.basename(self.args.query_sql_file)
				self.from_query_name.append(qf)

			elif self.args.query_sql_dir:
				self.QD=True
				
				
				#print self.args.query_sql_dir
				assert os.path.isdir(self.args.query_sql_dir), 'Query dir "%s" does not exists.' % self.args.query_sql_dir
				import glob
				for qf in os.listdir(self.args.query_sql_dir):
					qry=open(os.path.join(self.args.query_sql_dir, qf)).read().strip().strip(';')
					self.from_query.append(qry)
					self.from_query_name.append(qf)
					#self.from_query_file_name.append(qf)
		#validate

		if self.V:
			if self.T:
				(partitioned, temporary, valid) = self.get_table_info()		
				if self.P or self.SP:
					#print self.SP, self.P
					assert partitioned in ('YES'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
				assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
				assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)	
			if self.P:
				self.detect_partition()
			if self.SP:
				self.detect_subpartition()
		self.outfn=[]
		self.set_outfn()				
		#
		#rewrite queries
		#
		if self.QF or self.QD:
			self.rewrite_queries()
		#
		#create queries for tables/partitions/sub-partitions
		#
		if self.T or self.P or self.SP:
			if self.Sh:
				if self.SP:			
					(self.shards, status)=self.get_subpart_tab_shards(self.args.num_of_shards, self.login, self.from_table.split('.'))		
				elif self.P:				
					(self.shards, status)=self.get_part_tab_shards_dbms(self.args.num_of_shards, self.login, self.from_table.split('.'))		
				else:
					(self.shards, status)=self.get_tab_shards_dbms(self.args.num_of_shards, self.login, self.from_table.split('.'))		

			self.create_table_queries()
			
		#print self.outfn
		#e(0)
	def if_remote(self, shard):
		assert shard != None, 'Shard is not set (%s)' % shard
		assert self.hm, 'host_map is not set'
		if self.hm:
			return self.hm.if_remote(self.hm,shard)
		return False

	def set_payload(self,num_of_shards,toDb=None):
		self.toDb=toDb
		if self.Sh and self.shards:
			for i in range(len(self.shards)):
				sid,rowid_from, rowid_to,part = self.shards[i].split('||')
				outfn=self.outfn[i]
				qname=None
				if self.QD or self.QF:
					qname=self.from_query_name[i]				
					
				self.from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,qname,None))
		else:
			for i in range(num_of_shards):					
				outfn=self.outfn[i]	
				#self.get_outfn(0)
				qname=None
				if self.QD or self.QF:
					qname=self.from_query_name[i]
				self.from_pld.append(('Shard-%d' % i,outfn, None,None,qname,None))
				self.shards=['0||||||']
		#print self.shards
		#e(0)
		return (self.shards,self.from_pld) 			
	def get_spool_config(self,from_pld):
		#pprint(from_pld)
		sid=int(from_pld[0].split('-')[1])
		#e(0)
		#sys.exit(1)
		#pprint (self.spConf)
		#print sid
		#pprint (self.spConf)
		#e(0)
		return self.spConf[sid]
		if 0:
			if self.T:
				if self.P:
					return self.get_part_table_spool_config(from_pld)
				else:
					
					return self.spConf[sid]
					#return self.get_table_spool_config(from_pld)
			else:
				return self.spConf[sid]
				#if self.QF:
				#	return self.get_query_spool_config(from_pld)
				#else:
				#	return self.get_querylist_spool_config(from_pld)

	def get_ddl_extract_config(self,from_pld):
		sid=int(from_pld[0].split('-')[1])
		q= self.uargs_db.get_ddl_sppol_query()		
		#self.new_query.append(q)
		sqfn=self.save_qry('table_ddl_spool%s' % sid,q)
		return [self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn]
	def set_outfn(self):
		#pprint(self.from_query_name)
		if self.Sh and self.shards:			
			for i in range(len(self.shards)):
				qname=None
				if self.QD or self.QF:
					qname=self.from_query_name[i]
				self.outfn.append(self.get_outfn(i,qname))
		else:
			for i in range(self.args.num_of_shards):
				qname=None
				if self.QD or self.QF:
					qname=self.from_query_name[i]
				self.outfn.append(self.get_outfn(i,qname))
			
	def create_table_queries(self):
		tab=self.from_table				
		(from_cols, cols) =  self.uargs_db.get_table_columns(tab)

		if not self.kW:
	
			self.set_tWs_table_query(from_cols)
			#self.new_query.append(qry)
			#e(0)
		else: #keep white-space
			self.set_Ws_table_query(from_cols)	
				
	def set_tWs_table_query(self,  cols_from):
		status=0
		options={}
		#print self.V, self.TT
		ptn=''
		if hasattr(self.args, 'from_partition') and self.args.from_partition:
			ptn=' PARTITION(%s) ' % self.args.from_partition
		elif hasattr(self.args, 'from_sub_partition') and self.args.from_sub_partition:
			ptn=' SUBPARTITION(%s) ' % self.args.from_sub_partition
		if self.Sh:
			#(self.shards, status)=self.get_tab_shards_dbms(self.args.num_of_shards, self.login, self.from_table.split('.'),options)
			lim=''
			limit =self.args.lame_duck
			if limit:
				lim= ' WHERE ROWNUM<%d' % (limit+1)			
			for shard in self.shards:
				#print shard
				#print shard.split('||')
				sid,rowid_from, rowid_to,_ = shard.split('||')
				assert rowid_from, 'rowid_from is not set'
				assert rowid_to, 'rowid_to is not set'  
				qry = "SELECT * FROM %s %s WHERE ROWID BETWEEN '%s' AND '%s'" % (self.from_table,ptn,rowid_from,rowid_to) #AND ROWNUM<1000
				#print qry
				#print cols_from
				q= self.get_noWs_query(qry, cols_from, 0)
				#print q
				self.new_query.append(q)
				sqfn=self.save_qry('table_spool_tW_sh_%s' % sid,q)
				self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
		else:	
			qry = 'SELECT * FROM %s %s' % (self.from_table,ptn)
			q=self.get_noWs_query(qry, cols_from, 0)	
			sqfn=self.save_qry('table_spool_tW_%s' % 0,q)
			self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
		
	def set_Ws_table_query(self,cols_from):
		status=0
		options={}
		ptn=''
		if hasattr(self.args, 'from_partition') and self.args.from_partition:
			ptn=' PARTITION(%s) ' % self.args.from_partition
		elif hasattr(self.args, 'from_sub_partition') and self.args.from_sub_partition:
			ptn=' SUBPARTITION(%s) ' % self.args.from_sub_partition		
		#e(0)

		r_from=cols_from
		col_buckets=1
		
		if hasattr(self.args, 'column_buckets') and self.args.column_buckets:
			col_buckets=self.args.column_buckets
		if 1:
			ft = self.args.field_term 
			lt = '' 
			bca=[]
			ca=self.get_key2cols(r_from)
			if col_buckets==1:
				#ca=self.get_key2cols(r_from)
				cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			else:
				step=int(len(ca)/col_buckets)
				#print step
				for b in range(0,col_buckets):
					bca.append (ca[b*step:(b+1)*step])
				if len(ca)>col_buckets*step:
					bca.append (ca[col_buckets*step:])
				#pprint(bca)
				#print ca
				
				cl =','.join(["%s||'%s'" % (string.rstrip(string.join(x,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt) for x in bca ])
				
				#print(cl)
				#e(0)
			h=''
			if 0 and self.H:
				hc=[]
				for c in cols_from:
					hc.append(c[0].split(':')[0])
				
				h="SELECT '%s' FROM DUAL UNION ALL" % ft.join(hc)
				
		if self.Sh:
			#(self.shards, status)=self.get_tab_shards_dbms(self.args.num_of_shards, self.login, self.from_table.split('.'),options)
			lim=''
			limit =self.args.lame_duck
			if limit:
				lim= ' WHERE ROWNUM<%d' % (limit+1)			
			for shard in self.shards:
				sid,rowid_from, rowid_to,_ = shard.split('||')
				assert rowid_from, 'rowid_from is not set'
				assert rowid_to, 'rowid_to is not set'  
				qry = "SELECT %s FROM %s %s WHERE ROWID BETWEEN '%s' AND '%s'" % (cl,self.from_table,ptn,rowid_from,rowid_to) #AND ROWNUM<1000
				#print qry
				#print cols_from
				q= self.get_Ws_query(qry,  sid)
				#print q
				self.new_query.append(q)
				sqfn=self.save_qry('table_spool_Ws_sh_%s' % sid,q)
				self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
				
		else:	
			qry = 'SELECT %s FROM %s %s' % (cl,self.from_table,ptn)
			q=self.get_Ws_query(qry, 0)	
			self.new_query.append(q)
			sqfn=self.save_qry('table_spool_Ws_%s' % 0,q)
			self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])			
		
	def rewrite_queries(self):
		if not self.kW:
			if self.QF:
				qry=self.from_query[0]
				(from_cols,status) =  self.get_query_columns(self.log,self.login, qry)
				assert not status, 'Error fetching query columns\n status %s\n query %s' % (status,qry)
				#print from_cols
				q=self.get_noWs_query(qry, from_cols, 0)
				self.new_query.append(q)
				sqfn=self.save_qry('query_spool_tW_%s' % 0,q)
				self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])				
			elif self.QD:
				for qid in range(len(self.from_query)):
					qry=self.from_query[qid]
					#print qry
					(from_cols,status) =  self.get_query_columns(self.log,self.login, qry)
					assert not status, 'Error fetching query columns\n status %s\n query %s' % (status,qry)
					#print from_cols
					q=self.get_noWs_query(qry, from_cols, qid)
					#print q
					self.new_query.append(q)
					sqfn=self.save_qry('query_spool_tW_%s' % qid,q)
					self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
			else:
				pass #not a query
		else: #self.tW=False
			if self.QF:
				qry=self.from_query[0]	
				q=self.get_Ws_query(qry, 0)
				self.new_query.append(q)
				sqfn=self.save_qry('query_spool_%s' % 0,q)
				self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
			elif self.QD:
				for qid in range(len(self.from_query)):
					qry=self.from_query[qid]
					q=self.get_Ws_query(qry, qid)
					self.new_query.append(q)
					sqfn=self.save_qry('query_spool_%s' % qid,q)
					self.spConf.append([self.db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn])
					
			else:
				pass #not a query
	def get_Ws_query(self, qry, shard_id):
		feedback='on'
		if self.if_remote(shard_id): #remote
			feedback='off'
		lim=''
		limit =self.args.lame_duck
		llen=32767
		if limit:
			lim= ' WHERE ROWNUM<%d' % (limit+1)
		h='off'
		if self.H:
			h='on'
		q = """
SET TAB OFF timing off head %s line %d pages 0 newpage 0 echo off feedback on define off feed off arraysize 5000
set embedded on
set und off
set embedded on
set pagesize 0
set colsep '|'
set echo off
set feedback %s
set trimspool on
set headsep off
SET newpage none 
SET verify off 
SET trims ON 
SET trimspool ON 
set underline off
SELECT * FROM (%s) %s;
exit;
""" % (h, llen, feedback, qry, lim) 
		#print q
		#e(0)
		return q
			
	def get_noWs_query(self, qry, cols_from, shard_id):
		if hasattr(self.args, 'column_buckets'):
			if self.args.column_buckets>1:
				return self.get_ColBuckets_query(qry, cols_from, shard_id, self.args.column_buckets)
			else:
				return self.get_noColBuckets_query(qry, cols_from, shard_id)
		else:
			return self.get_noColBuckets_query(qry, cols_from, shard_id)

	def get_ColBuckets_query(self, qry, cols_from, shard_id, col_buckets):
		feedback='on'
		if self.if_remote(shard_id): #remote
			feedback='off'
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		limit =self.args.lame_duck
		if limit:
			lim= ' WHERE ROWNUM<%d' % (limit+1)
		qry = 'SELECT2 * FROM (%s) %s' % (qry, lim) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from

		from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		from_t= list((from_schema, tempt))
		#print self.args.column_buckets
		#e(0)
		if 1:
			ft = self.args.field_term 
			lt = '' 
			bca=[]
			ca=self.get_key2cols(r_from)
			step=int(len(ca)/col_buckets)
			#print step
			for b in range(0,col_buckets):
				bca.append (ca[b*step:(b+1)*step])
			if len(ca)>col_buckets*step:
				bca.append (ca[col_buckets*step:])
			#pprint(bca)
			#print ca
			
			cl =','.join(["%s||'%s'" % (string.rstrip(string.join(x,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt) for x in bca ])
			
			#print(cl)
			#e(0)
			h=''
			if 0 and self.H:
				hc=[]
				for c in cols_from:
					hc.append(c[0].split(':')[0])
				
				h="SELECT '%s' FROM DUAL UNION ALL" % ft.join(hc)
			#print cl
			#e(0)
			llen=32767
			orderby=''
			q=''
			if 1:
				q= """SET TAB OFF timing off head off line %s pages 0 newpage 0 echo off define off feed off arraysize 5000\n\n\n\n%s\n
set embedded on
set und off
set embedded on
set pagesize 0
set colsep '|'
set echo off
set feedback %s
set trimspool on
set headsep off
SET newpage none 
SET verify off 
SET trims ON 
SET trimspool ON 
set underline off
SELECT %s FROM (%s) %s %s;\nexit;\n""" % (llen,feedback, h, cl, qry, ' ',orderby)
			tab= string.join(from_t,'.')
			#sqfn=self.save_qry('spool_sql_%d' % shard_id,q)
			#print 			q
			#e(0)
			return q				
	def get_noColBuckets_query(self, qry, cols_from, shard_id):
		feedback='on'
		if self.if_remote(shard_id): #remote
			feedback='off'
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		limit =self.args.lame_duck
		if limit:
			lim= ' WHERE ROWNUM<%d' % (limit+1)
		qry = 'SELECT * FROM (%s) %s' % (qry, lim) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from

		from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		from_t= list((from_schema, tempt))
		#print self.args.column_buckets
		#e(0)
		if 1:
			ft = self.args.field_term 
			lt = '' 

			ca=self.get_key2cols(r_from)
			cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			h=''
			if self.H:
				hc=[]
				for c in cols_from:
					hc.append(c[0].split(':')[0])
				
				h="SELECT '%s' FROM DUAL UNION ALL" % ft.join(hc)
			#print cl
			#e(0)
			llen=32767
			orderby=''
			q=''
			if 1:
				q= "SET TAB OFF timing off head on line %s pages 0 newpage 0 echo off feedback on define off feed off arraysize 5000\n\n\n\nset feedback %s\n %s\nSELECT %s FROM (%s) %s %s;\nexit;\n" % (llen, feedback, h, cl, qry, ' ',orderby)
			tab= string.join(from_t,'.')
			#sqfn=self.save_qry('spool_sql_%d' % shard_id,q)
			#print 			q
			#e(0)
			return q				
		
	def print_copy_details(self):
		if self.T:
			source='table: %s' % self.from_table
		elif self.QF:
			source='query: %s' % self.args.query_sql_file
		else:
			source='query: %s' % self.args.query_sql_dir			
		part=''
		if self.P:
			part="""
	partition: %s""" % self.args.from_partition
		if self.SP:
			part="""
	sub-partition: %s""" % self.args.from_sub_partition		
		print """		
From %s:	
	from db: %s
	%s%s
	shards:\t%s
		""" % (conf.dbs[self.db],'%s@%s' % (self.login.split('/')[0],self.login.split('@')[1]),source,part,self.args.num_of_shards)
		print """default_spool_dir:
	%s""" % self.uargs.default_spool_dir
	def get_firstrow(self):
		return 1	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['SPOOLER'][self.db])
		if self.hm.local_source_client_home:
			self.db_client_loc=(r'%s\%s' % (self.hm.local_source_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['SPOOLER'][self.db]
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc

		
	def get_db_client_dbshell0(self):
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
		qry="SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_PARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('%s') AND UPPER(partition_name)=UPPER('%s');\nexit;\n" % (self.args.from_table,self.args.from_partition)
		#print qry
		sqfn=self.save_qry('get_part_info_%s.%s' % (self.args.from_table,self.args.from_partition),qry)	
		regexp=re.compile(r'ROW_COUNT\:(\d+)')		
		(r_int, status,err)=self.uargs_db.do_query(self.args.from_db, query=None,regexp=regexp,query_file=sqfn)
		#print (r_int, status)
		assert r_int and r_int[0] and r_int[0][0] in '1' , 'Partition "%s" does not exists in table %s' % (self.args.from_partition,self.args.from_table)
		self.log.info('Done.')
	def detect_subpartition(self):
		self.log.info('Verifying sub-partition...')
		qry="SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_SUBPARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('%s') AND UPPER(subpartition_name)=UPPER('%s');\nexit;\n" % (self.args.from_table,self.args.from_sub_partition)
		#print qry
		sqfn=self.save_qry('get_part_info_%s.%s' % (self.args.from_table,self.args.from_sub_partition),qry)	
		regexp=re.compile(r'ROW_COUNT\:(\d+)')		
		(r_int, status,err)=self.uargs_db.do_query(self.args.from_db, query=None,regexp=regexp,query_file=sqfn)
		#print (r_int, status)
		assert r_int and r_int[0] and r_int[0][0] in '1' , 'Sub-Partition "%s" does not exists in table %s' % (self.args.from_sub_partition,self.args.from_table)
		self.log.info('Done.')
	def get_query_columns_local(self,log,login, qry):
		if self.args.header:
			if self.cols_from:
				return (self.cols_from,0)
			else:
				(cols_from,status) = Oracle.get_query_columns(self,log,login, qry)
				self.cols_from = cols_from
				return (cols_from,status)
		else:
			return ([],0)
	def set_part_table_payload(self,num_of_shards):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		from_pld=[]	
		#check if table is partitioned
		(partitioned, temporary, valid) = self.get_table_info()
		#print (partitioned, temporary, valid) 		
		assert partitioned in ('YES'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
		assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
		assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)
		#sys.exit(1)
		#if self.P:
		#check if partition exists
		self.detect_partition()
		#sys.exit(0)
		if num_of_shards>1:
			(shards, status)=self.get_part_tab_shards_dbms(self.log,num_of_shards, self.login, self.from_table.split('.'),options)
			assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
				
			#globalStatus={}
			
			for i in range(len(shards)):
				#sys.exit(1)
				#print shards
				(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#if 1:
				#	ctlfn= self.save_ctl(self.from_table,i)
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)				
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,None))

					#globalStatus[i]=(99, None)	
			#print from_pld
			#pprint(shards)
			#sys.exit(1)
		else:
			assert num_of_shards>0, 'Shard number should be greater than zero'
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			#sys.exit(1)
			outfn=self.get_outfn(0)			
			from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,None))
			shards=['0||||||']
		return (shards,from_pld)	
	def set_subpart_table_payload(self,num_of_shards):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		from_pld=[]	
		#check if table is partitioned
		(partitioned, temporary, valid) = self.get_table_info()
		#print (partitioned, temporary, valid) 		
		assert partitioned in ('YES'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
		assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
		assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)
		#sys.exit(1)
		#if self.P:
		#check if partition exists
		self.detect_subpartition()
		#sys.exit(0)
		if num_of_shards>1:
			(shards, status)=self.get_subpart_tab_shards(self.log,num_of_shards, self.login, self.from_table.split('.'),options)
			assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
				
			#globalStatus={}
			
			for i in range(len(shards)):
				#sys.exit(1)
				#print shards
				(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#if 1:
				#	ctlfn= self.save_ctl(self.from_table,i)
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)				
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,None))

					#globalStatus[i]=(99, None)	
			#print from_pld
			#pprint(shards)
			#sys.exit(1)
		else:
			assert num_of_shards>0, 'Shard number should be greater than zero'
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			#sys.exit(1)
			if self.toDb:
				outfn=self.toDb.get_out_fn(0)
			else:
				outfn=self.get_outfn(0)			
			from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,None))
			shards=['0||||||']
		return (shards,from_pld)
		
	def get_table_info(self):
		self.log.info('Fetching table info...')
		qry="SELECT 'TABLE_INFO='||PARTITIONED||':'||TEMPORARY||':'||STATUS info from ALL_TABLES where UPPER(OWNER||'.'||TABLE_NAME)=UPPER('%s');\nexit;\n" % (self.args.from_table)
		#print qry
		pname=''
		if hasattr(args, 'from_partition') and self.args.from_partition:
			pname=self.args.from_partition
		sqfn=self.save_qry('get_table_info_%s.%s' % (self.args.from_table,pname),qry)	
		regexp=re.compile(r'TABLE_INFO\=([\w:]+)')		
		(r_int, status,err)=self.uargs_db.do_query(self.args.from_db, query=None,regexp=regexp,query_file=sqfn)
		#print r_int
		#sys.exit(0)		
		assert r_int and r_int[0] and r_int[0][0], 'Table "%s" does not exists.' % (self.args.from_table)
		self.log.info('Done.')
		return r_int[0][0].split(':')
		
	def set_table_payload(self,num_of_shards):
		print ''
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		from_pld=[]	
		#check if table is partitioned
		#check if partition exists
		(partitioned, temporary, valid) = self.get_table_info()		
		assert partitioned in ('NO'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
		assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
		assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)
		#print 	is_partitioned
		#sys.exit(1)
		if num_of_shards>1:
			(shards, status)=self.get_tab_shards_dbms(num_of_shards, self.login, self.from_table.split('.'),options)
			assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
				
			#globalStatus={}
			
			for i in range(len(shards)):
				#sys.exit(1)
				#print shards
				(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#if 1:
				#	ctlfn= self.save_ctl(self.from_table,i)
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)	

				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,None))

					#globalStatus[i]=(99, None)	
			#pprint (from_pld)
			#pprint(shards)
			#sys.exit(1)
		else:
			assert num_of_shards>0, 'Shard number should be greater than zero'
			qry='SELECT * FROM %s' % self.from_table
			#print qry
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			#sys.exit(1)
			if self.toDb:
				outfn=self.toDb.get_out_fn(0)
			else:
				outfn=self.get_outfn(0)	
			#print self.toDb
			#print outfn
			#e(0)				
			from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,None))
			shards=['0||||||']
		return (shards,from_pld) 
	def set_payload_old(self,num_of_shards,toDb=None):
		#print self.QD
		#sys.exit(0)
		#print self.T,self.P
		#e(0)
		self.toDb=toDb
		if self.T:
			if self.P:
				return self.set_part_table_payload(num_of_shards)
			if self.SP:
				return self.set_subpart_table_payload(num_of_shards)
			else:
				return self.set_table_payload(num_of_shards)
		else:
			if self.QF:
				return self.set_query_payload()
			else:
				#print 3
				return self.set_querylist_payload()

	def set_query_payload(self):
		
		options={}
		from_pld=[]	
		if self.toDb:
			outfn=self.toDb.get_out_fn(0)
		else:
			outfn=self.get_outfn(0)		

		from_pld.append(('Shard-%d' % 0,outfn,None,None,None,None))
		shards=['0||||||']
		return (shards,from_pld) 			
	def set_querylist_payload(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		from_pld=[]
		shards=[]
		qid=0
		outfn=None
		for q in self.from_query:
			qry='SELECT * FROM (%s)' % q.strip().strip(';').strip()
			#print qry
			#sys.exit(1)
			(cols_from,status) = self.get_query_columns(self.log,self.login, qry)
			assert cols_from, 'Cannot fetch source query columns'

			if self.toDb:
				outfn=self.toDb.get_out_fn(qid)
			else:
				outfn=self.get_outfn(qid)		
			#outfn=os.path.join(os.path.dirname(outfn), self.from_query_name[qid])
			from_pld.append(('Shard-%d' % qid,outfn,None,None,cols_from,None))
			shards.append('%s||||||' % qid)
			qid +=1
		return (shards,from_pld) 
		
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, 0,0)


	def get_part_table_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=self.args.from_partition
		#shard=shard_name.split('-')[1]
		feedback='on'
		if self.if_remote(shard_id): #remote
			feedback='off'		
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		if rowid_from and rowid_to: 
			qry = "SELECT * FROM %s PARTITION(%s) WHERE ROWID BETWEEN '%s' AND '%s' %s" % (self.from_table,ptn,rowid_from,rowid_to,lim) #AND ROWNUM<1000
		else:
			qry = "SELECT * FROM %s PARTITION(%s) WHERE 1=1 %s" % (self.from_table,ptn,lim) #AND ROWNUM<1000
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
			#pprint (cols_from)
			#sys.exit(0)
			ca=self.get_key2cols(r_from)
			
			#self.ckey2cols(r_from)
			cl =  "%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			llen=32767
			orderby=''
			q=''
			if 1:
				q= "SET TAB OFF timing off head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET hash_area_size = 524288000\n/\n\nset feedback %s\nSELECT %s FROM (%s) %s %s;\nexit;\n" % (llen,  feedback, cl, qry, ' ',orderby)
				#q= "set head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET sort_hash_size = 524288000\n/\nalter session set NLS_DATE_FORMAT='DD-MON-RR HH.MI.SS AM'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp,{'_PARTITION':self._pp.get('PARTITION',None)}),orderby)
				#q= "set line %s arraysize 5000\nalter session set NLS_DATE_FORMAT='DD-MON-YY'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp))
			#set timing off pagesize 0 heading off line 2000 long 128000  feedback off\ncolumn object_ddl format a121 word_wrapped
			tab= string.join(from_t,'.')
			sqfn=self.save_qry('part_table_spool_%s' % shard_name,q)
			
			#abspath= os.path.abspath(os.path.dirname(sys.argv[0]))
			db_client_loc=self.get_db_client_loc()
			spConf=[ db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn]
			#pprint(spConf)
			#sys.exit(0)
		return spConf			
	def get_table_spool_config_0(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld
		q=self.new_query[0]
		
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		if rowid_from and rowid_to: 
			qry = "SELECT * FROM %s WHERE ROWID BETWEEN '%s' AND '%s' %s" % (self.from_table,rowid_from,rowid_to,lim) #AND ROWNUM<1000
		else:
			qry = "SELECT * FROM %s  WHERE 1=1 %s" % (self.from_table,lim) #AND ROWNUM<1000
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
			#pprint (cols_from)
			#sys.exit(0)
			#ca=self.ckey2cols(r_from)
			ca=self.get_key2cols(r_from)
			cl =  "%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			#print cl
			#sys.exit(0)
			llen=32767
			orderby=''
			q=''
			if 1:
				q= "SET TAB OFF timing off head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET hash_area_size = 524288000\n/\n\nset feedback on\nSELECT %s FROM (%s) %s %s;\nexit;\n" % (llen,   cl, qry, ' ',orderby)
				#q= "set head off line %s pages 0 newpage 0 echo off feedback off define off feed off arraysize 5000\nALTER SESSION SET workarea_size_policy = manual\n/\nALTER SESSION SET sort_area_size = 524288000\n/\nALTER SESSION SET sort_hash_size = 524288000\n/\nalter session set NLS_DATE_FORMAT='DD-MON-RR HH.MI.SS AM'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp,{'_PARTITION':self._pp.get('PARTITION',None)}),orderby)
				#q= "set line %s arraysize 5000\nalter session set NLS_DATE_FORMAT='DD-MON-YY'\n/\n\nalter session set NLS_TIMESTAMP_FORMAT='DD-MON-RR HH.MI.SSXFF AM'\n/\n\nSELECT %s FROM %s %s;\nexit;\n" % (llen,    cl, string.join(self.get_from_tab(from_t),'.'), self.get_q_options(self._pp))
			#set timing off pagesize 0 heading off line 2000 long 128000  feedback off\ncolumn object_ddl format a121 word_wrapped
			tab= string.join(from_t,'.')
			sqfn=self.save_qry('table_spool_%s' % shard_name,q)
			
			#abspath= os.path.abspath(os.path.dirname(sys.argv[0]))
			db_client_loc=self.get_db_client_loc()
			spConf=[ db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn]
			#pprint(spConf)
			#sys.exit(0)
		return spConf
	def get_key2cols(self,cols):
		out=[]
		for col in cols:
			#print col
			(cname, clength, ctype) = col[0].split(':')
			#print (cname, clength, ctype)
			if ctype in ('DATE'):
				if self.args.nls_date_format:
					out.append( "TO_CHAR(%s,'%s') " % (cname,self.args.nls_date_format))
				else:
					out.append(  "%s  " % (cname))
			elif ctype.endswith('WITH TIME ZONE'):
				if self.args.nls_timestamp_tz_format:
					out.append(  "TO_CHAR(%s,'%s') " % (cname,self.args.nls_timestamp_tz_format))
			elif ctype.startswith('TIMESTAMP'):
				if self.args.nls_timestamp_format:
					out.append(  "TO_CHAR(%s,'%s') " % (cname,self.args.nls_timestamp_format))
					
				else:
					out.append(  "%s " % (cname))
			else:
				out.append(  "%s " % (cname))
		#pprint(cols)
		#print out
		#e(0)
		#sys.exit(0)
		#ca=self.ckey2cols(cols)
		#return "%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
		return out	
	def get_query_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld
		q=self.new_query[0]
		sqfn=self.save_qry('spool_sql_%s' % shard_name,q)

		db_client_loc=self.get_db_client_loc()

		spConf=[ db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn]
		#print sqfn
		#spConf=[ db_client_loc,'%s' % (self.login),'@%s' % sqfn]

		return spConf
	def get_querylist_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld

		sid=shard_name.split('-')[1]
		if 1:

			q=self.new_query[int(sid)]
			
			qname=self.from_query_name[int(sid)]
			sqfn=self.save_qry('spool_sql_%s' % qname,q)
			db_client_loc=self.get_db_client_loc()
			spConf=[ db_client_loc,'-S','%s' % (self.login),'@%s' % sqfn]
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
		(r_int, status,err)=self.uargs_db.do_query(from_db, query=None,query_file=cqfn)
		
		#print from_db
		#pprint(r)
		#t= 
		#sys.exit(1)
		#pprint(r_int)
		#e(0)

		return (r_int, status)
	def spool_source_data(self,outfn, spConf, payload):
		(count, status)	= self.uargs_db.spool_source_data(outfn, spConf, payload)	
		if count:
			if (not self.kW) and self.H:
				count -=1
		return (count, status)	
	def spool_ddl(self,outfn, spConf, payload):
		(shard_name,from_pld,to_pld)=payload

		outf=open(outfn, "w")
		#print self.cols_from
		if self.args.nls_timestamp_format:
			os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
		else:
			os.environ['NLS_TIMESTAMP_FORMAT'] =''
		if self.args.nls_timestamp_tz_format:
			os.environ['NLS_TIMESTAMP_TZ_FORMAT'] = self.args.nls_timestamp_tz_format
		else:
			os.environ['NLS_TIMESTAMP_TZ_FORMAT'] =''	
		#print outfn
		#pprint(spConf )
		#e(0)
		p = Popen(spConf, stdout=outf) # '-S',  stdin=p1.stdout,
		
		output, err = p.communicate()
		#print output, err
		
		if err:
			self.log.err(err)
			#print output
		status=p.wait()
		outf.close()
		#e(0)
		count=1

		
		return (count, status)		