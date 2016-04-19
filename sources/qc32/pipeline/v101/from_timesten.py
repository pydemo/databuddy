import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_timesten import TimesTen
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
import shlex
import string
e=sys.exit
class FromTimesTen(TimesTen):
	"""TimesTen db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(args.from_user, args.from_passwd, args.from_DSN_name)
		TimesTen.__init__(self,log,self.login,datadir,conf.args) 		
		self.db=db
		self.args=args
		self.tab_cols={}
		#self.login=login
		self.from_tab_cols={}
		self.from_query=[]
		self.from_query_name=[]

		self.lim=''
		if self.args.lame_duck:
			self.lim= ' FIRST %d' % (self.args.lame_duck)	
		self.T, self.QF, self.QD =(False,  False, False)
		if self.args.from_table:
			assert not self.args.query_sql_file, 'Set Table/Partition or Query but not both.'
			self.T=True
		else:
			#self.args.num_of_shards, 'Number of shards is not set'
			#assert int(self.args.num_of_shards) == 1, 'Cannot shard in QUERY mode. Set num_of_shards=1.'
			#pprint (dir(self.args))
			assert self.args.query_sql_file or self.args.query_sql_dir, 'Either query file or query dir has to be set.'
			if self.args.query_sql_file:
				self.QF=True
				assert os.path.isfile(self.args.query_sql_file), 'Query file "%s" does not exists.' % self.args.query_sql_file	
				q=open(self.args.query_sql_file).read().strip().strip(';')				

				self.from_query.append(q)
				#self.from_query_name.append(self.args.query_sql_file)
			elif self.args.query_sql_dir:
				self.QD=True
				
				
				#print self.args.query_sql_dir
				assert os.path.isdir(self.args.query_sql_dir), 'Query dir "%s" does not exists.' % self.args.query_sql_dir
				import glob
				for qf in os.listdir(self.args.query_sql_dir):
					#print qf
					self.from_query.append(open(os.path.join(self.args.query_sql_dir, qf)).read())
					self.from_query_name.append(qf)
				
				
	def print_copy_details(self):		
		if self.T:
			source='table: %s' % self.args.from_table
		else:
			if self.QF:
				source='query: %s' % self.args.query_sql_file
			else:
				source='query dir: %s' % self.args.query_sql_dir
		part=''
	
		print """		
From %s:	
	from db: %s
	%s%s
	shards:\t%s
		""" % (conf.dbs[self.db],'%s@%s' % (self.args.from_user,self.args.from_DSN_name),source,part,self.args.num_of_shards)	
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
	def get_db_shell_path(self):
		if self.db_shell_path:
			return self.db_shell_path
		dbshell= os.path.basename(conf.dbtools['DBSHELL'][self.db])
		if self.args.source_client_home:
			self.db_shell_path=os.path.join(self.args.source_client_home.strip('"').strip("'").strip('\\').strip('\\'), dbshell)
		else:
			self.db_shell_path=conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_shell_path):
				self.log.warn('Path to source dbshell is not set. Defaulting to %' % dbshell)	
		print self.db_shell_path
		return self.db_shell_path.strip('"')	
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
				
	def get_table_spool_config_tt(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
		
		spConf=[ '"%s"' %  db_client_loc ,'-Cnone', '-o' ,	'-s','^|',			 
				'-dformat',  r'"%s"' % self.args.nls_date_format, 
				'-tsformat', r'"%s"' % self.args.nls_timestamp_format, 
				'-Q', '0',
				'-connstr', connect_str,
				 self.args.from_table,
				r'"%s"' % outfn]

		
		#"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttBulkCp.exe" -o -s ^| -Cnone  -dformat "YYYY-MM-DD" -tsformat "YYYY-MM-DD HH24.MI.SS.FF" -Q 0 -connstr "DSN=my_ttdb;UID=TERRY;PWD=secret" TERRY.Persons_pipe_datetime  "C:\Python27\csvextractor_1235\CSV_OUT\testTTEN_Table.data"
		
		#print sqfn
		#pprint(spConf)
		print ' '.join(spConf)
		#sys.exit(0)
		return spConf
	def get_query_spool_config_tt(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
		
		spConf=[  db_client_loc ,'-Cnone', '-o' ,	'-s','^|',			 
				'-dformat',  self.args.nls_date_format, 
				'-tsformat', self.args.nls_timestamp_format, 
				'-Q', '0',
				'-connstr', connect_str,
				 self.args.from_table,
				outfn]

		
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf
	def get_table_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,sqfn)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""

		qry = 'SELECT %s * FROM %s' % ( self.lim, self.args.from_table.strip(';').strip()) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from
		status=None
	
		#from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		#from_t= list((from_schema, tempt))
		
		if not status:
			ft = field_term 
			lt = '' 

			ca=self.get_key2cols(r_from)
			#print ca
			#cl =  self. get_column_list_str(r_from,ft,lt)
			cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			#print cl
			#sys.exit(0)
			#print 
			llen=32767
			orderby=''
			#q=''
			#if 1:
			#	#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
			#	q= "SELECT %s FROM (%s) %s %s;\n" % (  cl, qry, ' ',orderby)
			#tab= string.join(from_t,'.')
			#sqfn=self.save_qry('spool_sql_%s' % shard_name,q)
			#pprint (q)
			#print sqfn
			#print self.login
			#sys.exit(1)
			connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			
			db_shell_path=self.get_db_shell_path()
		
			#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
			
			connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			#print connect_str
			#print db_shell_path
			#sys.exit(1);
			
			spConf=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','1','-f','"%s"' %  sqfn,'-e','"set rowdelimiters off;"']


			
			#print sqfn
			#pprint(spConf)
			#print ' '.join(spConf)
			#sys.exit(0)
		return spConf
	def get_query_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,sqfn)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		qry = 'SELECT * FROM (%s) %s' % (self.from_query[0].strip().strip(';').strip(), lim) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from
		status=None
	
		#from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		#from_t= list((from_schema, tempt))
		
		if not status:
			ft = field_term 
			lt = '' 

			ca=self.get_key2cols(r_from)
			#print ca
			#cl =  self. get_column_list_str(r_from,ft,lt)
			cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			#print cl
			#sys.exit(0)
			#print 
			llen=32767
			orderby=''
			#q=''
			#if 1:
			#	#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
			#	q= "SELECT %s FROM (%s) %s %s;\n" % (  cl, qry, ' ',orderby)
			#tab= string.join(from_t,'.')
			#sqfn=self.save_qry('spool_sql_%s' % shard_name,q)
			#pprint (q)
			#print sqfn
			#print self.login
			#sys.exit(1)
			connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			
			db_shell_path=self.get_db_shell_path()
		
			#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
			
			connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			#print connect_str
			#print db_shell_path
			#sys.exit(1);
			
			spConf=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','1','-f','"%s"' %  sqfn,'-e','"set rowdelimiters off;"']


			
			#print sqfn
			#pprint(spConf)
			#print ' '.join(spConf)
			#sys.exit(0)
		return spConf		
	def get_query_spool_config__(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,_)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=''
		#shard=shard_name.split('-')[1]
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		qry = 'SELECT * FROM (%s) %s' % (self.from_query[0].strip().strip(';').strip(), lim) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from
		status=None
	
		#from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		#from_t= list((from_schema, tempt))
		
		if not status:
			ft = field_term 
			lt = '' 

			ca=self.get_key2cols(r_from)
			#print ca
			#cl =  self. get_column_list_str(r_from,ft,lt)
			cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			#print cl
			#sys.exit(0)
			#print 
			llen=32767
			orderby=''
			q=''
			if 1:
				#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
				q= "SELECT %s FROM (%s) %s %s;\n" % (  cl, qry, ' ',orderby)
			#tab= string.join(from_t,'.')
			sqfn=self.save_qry('spool_sql_%s' % shard_name,q)
			#pprint (q)
			#print sqfn
			#print self.login
			#sys.exit(1)
			connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			
			db_shell_path=self.get_db_shell_path()
		
			#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
			
			connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			#print connect_str
			#print db_shell_path
			#sys.exit(1);
			
			spConf=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','1','-f','"%s"' %  sqfn,'-e','"set rowdelimiters off;"']


			
			#print sqfn
			#pprint(spConf)
			#print ' '.join(spConf)
			#sys.exit(0)
		return spConf		
	def get_key2cols(self,cols):
		out=[]
		for col in cols:
			#print col
			(cname, ctype, clength) = col
			#print (cname, clength, ctype)
			if ctype in ('DATE'):
				if self.args.nls_date_format:
					out.append( "TO_CHAR(%s,'%s') " % (cname,self.args.nls_date_format))
				else:
					out.append(  "%s  " % (cname))
			elif ctype in ('TIMESTAMP'):
				if self.args.nls_timestamp_format:
					out.append(  "TO_CHAR(%s,'%s') " % (cname,self.args.nls_timestamp_format))
				else:
					out.append(  "%s " % (cname))
			else:
				out.append(  "%s " % (cname))
		
		#sys.exit(0)
		#ca=self.ckey2cols(cols)
		#return "%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
		return out			
	def get_querylist_spool_config(self,from_pld):
		(field_term,limit)=(self.args.field_term,self.args.lame_duck)
		(shard_name, outfn,rowid_from,rowid_to, cols_from,sqfn)=from_pld
		#pprint(from_pld)
		#sys.exit(1)
		ptn=''
		qid=int(shard_name.split('-')[1])
		f = ""
		lim=''
		if limit:
			lim= 'AND ROWNUM<%d' % (limit+1)
		qry = 'SELECT * FROM (%s) %s' % (self.from_query[int(qid)].strip().strip(';').strip(), lim) 
		err=[]
		tab = None
		assert  len(self.login)>0, 'Source login is not set.'
		assert  len(qry)>0, 'Query is not set.'
		if_compress = False 
		r_from=cols_from
		status=None
	
		#from_schema=self.login.split('/')[0]
		tempt=self.get_temp_table_name()
		#from_t= list((from_schema, tempt))
		
		if not status:
			ft = field_term 
			lt = '' 

			ca=self.get_key2cols(r_from)
			#print ca
			#cl =  self. get_column_list_str(r_from,ft,lt)
			cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)
			#print cl
			#sys.exit(0)
			#print 
			llen=32767
			orderby=''
			#q=''
			#if 1:
			#	#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
			#	q= "SELECT %s FROM (%s) %s %s;\n" % (  cl, qry, ' ',orderby)
			#tab= string.join(from_t,'.')
			#sqfn=self.save_qry('spool_sql_%s' % shard_name,q)
			#pprint (q)
			#print sqfn
			#print self.login
			#sys.exit(1)
			connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			
			db_shell_path=self.get_db_shell_path()
		
			#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
			
			connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
			#print connect_str
			#print db_shell_path
			#sys.exit(1);
			
			spConf=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','1','-f','"%s"' %  sqfn,'-e','"set rowdelimiters off;"']


			
			#print sqfn
			#pprint(spConf)
			#print ' '.join(spConf)
			#sys.exit(0)
		return spConf	
		
	def get_querylist_spool_config_tt(self,from_pld):
		#pprint(from_pld)
		#(sqfn,header_line) = from_pld
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		#sys.exit(1)
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		#db_client_loc='%s\psql' % self.args.source_client_home.strip("'").strip('\\').strip('\\')
		#db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		connect_str= 'DSN=%s;UID=%s;PWD=%s' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
		
		db_shell_path=self.get_db_shell_path()
	
		#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
		
		connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (self.args.from_DSN_name, self.args.from_user,self.args.from_passwd)
		#print connect_str
		#print db_shell_path
		#sys.exit(1);
		
		spConf=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','2','-f',sqfn]


		
		#print sqfn
		#pprint(spConf)
		#print ' '.join(spConf)
		#sys.exit(0)
		return spConf
	def get_sharded_sql_0(self,cols_from,sql_query,rowid_from,rowid_to):	
		assert sql_query.upper().startswith('SELECT'), 'Cannot shard query. '
		from_to=''
		self.max_int=2147483647
		if not rowid_from and not rowid_to:
			from_to=''			
		else:
			if not rowid_from:		
				from_to=' FIRST %s ' % (rowid_to)
			else:			
				if rowid_to: 
					from_to=' ROWS %s TO %s ' % (rowid_from, rowid_to+rowid_from)
				else:
					from_to=' ROWS %s TO %s' % (rowid_from,  self.max_int)
		#print from_to			
		qry= ' '.join(('SELECT',from_to ,sql_query[6:]))
		#print qry
		#sys.exit(1)
		#qry='%s%s' % (sql_query,'' % (rowid_from))
		#if rowid_to:
		#	qry='%s%s' % (qry,' FETCH NEXT %s ROWS ONLY ' % (rowid_to))
		return qry	
	def get_sharded_sql(self,cols_from,sql_query,rowid_from,rowid_to):	
		assert sql_query.upper().startswith('SELECT'), 'Cannot shard query. '
		from_to=''
		self.max_int=2147483647
		if not rowid_from and not rowid_to:
			from_to=''			
		else:
			if not rowid_from:		
				from_to=' rn< %s ' % (rowid_to)
			else:			
				if rowid_to: 
					from_to=' rn BETWEEN %s AND %s ' % (rowid_from, rowid_to+rowid_from)
				else:
					from_to=' rn> %s ' % (rowid_from)
		#print from_to			
		#qry= ' '.join(('SELECT',from_to ,sql_query[6:]))
		qry= 'SELECT * FROM (%s) WHERE %s ' % (sql_query, from_to )
		#print qry
		#sys.exit(1)
		#qry='%s%s' % (sql_query,'' % (rowid_from))
		#if rowid_to:
		#	qry='%s%s' % (qry,' FETCH NEXT %s ROWS ONLY ' % (rowid_to))
		return qry		

		
	def get_sharded_sql2(self,sql_query,rowid_from,rowid_to, rc,outfn):
		sql_query=sql_query.strip().strip(';')
		from_to=''
		if not rowid_from and not rowid_to:
			from_to=''			
		else:
			if not rowid_from:		
				from_to=' TOP %s ' % (rowid_to)
			else:			
				if rowid_to: 
					from_to=' TOP %s START AT %s ' % (rowid_to+1, rowid_from-1)
				else:
					from_to=' TOP %s START AT %s' % (rc-rowid_from+1,  rowid_from-1)
		hdr=''
		if 0:
			if self.args.header:
				hdr=' WITH COLUMN NAMES'
			out=r"""SELECT %s * FROM (%s) t ORDER BY 1; 
	OUTPUT TO '%s' FORMAT ASCII DELIMITED BY '%s' QUOTE ''%s;
	""" % (from_to,sql_query.strip().strip(';'),os.path.normpath(outfn).replace("\\", "\\\\"),self.args.field_term, hdr)	
			#print out
			#sys.exit(0)
		return ''
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;
	def get_firstrow(self):
		return 0
	def set_payload(self,num_of_shards,toDb=None):
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
	def count_rows(self,query):
		self.log.info('Counting rows in source...')
		regexp=re.compile(r'ROW COUNT\:(\d+)\s+')
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:'||count(*) cnt from (%s);""" % query
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
		rc=int(r[0][0])
		self.log.info(rc)
		#print type(rc)
		#types.TupleType:
		assert rc, 'Source table is empty.'
		assert rc>0, 'Cannot get source record count. Exiting...'
		return rc
		self.log.info('Done.')
		
	def set_table_payload(self,num_of_shards):
		print ''
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		from_pld=[]	
		#check if table is partitioned
		#check if partition exists
		#(partitioned, temporary, valid) = self.get_table_info()		
		#assert partitioned in ('NO'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
		#assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
		#assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)
		#print 	is_partitioned
		#sys.exit(1)
		qry= 'SELECT * FROM %s ' % (self.args.from_table)
		#print qry
		#print 'test'
		#e(0)
		if 1: #num_of_shards>1:
			if self.lim:
				qry='SELECT * FROM %s WHERE ROWNUM<%s' % (self.args.from_table,self.args.lame_duck)
			#print self.lim
			
			#print qry
			#e(0)
			rc=self.count_rows(qry)
			#e(0)
			#print qry
			#print rc
			#sys.exit(0)
			#assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			
			#print qry
			(cols_from,status) = self.get_query_columns( qry)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			#globalStatus={}
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
			#print shards
			#sys.exit(1)
			for i in range(len(shards)):
				#sys.exit(1)
				#print shards
				#(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				(sid,rowid_from, rowid_to, _) = shards[i]
				#sql_query= 'SELECT * FROM %s t' % self.args.from_table
				qry=self.get_table_query(cols_from,self.args.from_table)
				#print qry
				#e(0)
				if num_of_shards>1:
				
					qry=self.get_sharded_sql(cols_from,qry,rowid_from,rowid_to)
					#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				#sys.exit(0)
				#e(0)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_table_%s.sql' % (sqdir,i)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				if self.toDb:
					outfn=self.toDb.get_out_fn(i)
				else:
					outfn=self.get_outfn(i)				
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,sqfn))

					#globalStatus[i]=(99, None)	
			#pprint (from_pld)
			#pprint(shards)
			#sys.exit(1)
		else:
			assert num_of_shards>0, 'Shard number should be greater than zero'
			qry='SELECT * FROM %s' % self.args.from_table
			#print qry
			(cols_from,status) = self.get_query_columns( qry)
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
	def get_query(self,cols_from,table):
		ft=self.args.field_term
		lt = '' 

		ca=self.get_key2cols(cols_from)
		#print ca
		#cl =  self. get_column_list_str(r_from,ft,lt)
		cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)		
		q=''
		if 1:
			#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
			q= "SELECT %s FROM %s " % ( cl, table)
		#print q
		#sys.exit(1)
		return q
	def get_table_query(self,cols_from,table):
		ft=self.args.field_term
		lt = '' 

		ca=self.get_key2cols(cols_from)
		#print ca
		#cl =  self. get_column_list_str(r_from,ft,lt)
		cl ="%s||'%s'" % (string.rstrip(string.join(ca,"||'%s'||\n " % ft),"||'%s'||\n " % ft),lt)		
		q=''
		lim=''
		if self.lim:
			lim= 'where rn<%s' % self.args.lame_duck
		if 1:
			#q= "\n set verbosity 2;set feedback 1;SELECT %s FROM (%s) %s %s;set verbosity 1;\n" % (  cl, qry, ' ',orderby)
			q= "SELECT * FROM (SELECT %s FROM (SELECT rownum rn, * FROM %s ) %s )" % (  cl, table, lim)
		#print q
		#sys.exit(1)
		return q		
	def set_query_payload(self,num_of_shards):
		print ''
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		from_pld=[]	
		#check if table is partitioned
		#check if partition exists
		#(partitioned, temporary, valid) = self.get_table_info()		
		#assert partitioned in ('NO'), 'Expecting "--from_partition" for partitioned table %s.' % self.args.from_table
		#assert temporary in ('N'), 'Cannot work with temporaty tables.' % self.args.from_table
		#assert valid in ('VALID'), 'Table %s status is %s.' % (self.args.from_table, valid)
		#print 	is_partitioned
		#sys.exit(1)
		q=self.from_query[0].strip().strip(';')
		#print q
		#e(0)
		if 1: #num_of_shards>1:
			
			#print rc
			#sys.exit(0)
			#assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			
				#print

			(cols_from,status) = self.get_query_columns( q)
			assert cols_from, 'Cannot fetch source query columns'
			q= 'SELECT ROWNUM rn, * FROM (%s)' % (q)
			lim=''
			#if self.args.lame_duck:
			#	lim= 'AND ROWNUM<%d' % (self.args.lame_duck+1)			
			if self.args.lame_duck:
				q='SELECT * FROM (%s) WHERE rn<%s' % ( q, self.args.lame_duck)
			#print qry
			#e(0)
			rc=self.count_rows(q)
			#print cols_from
			#globalStatus={}
			#print  rc, num_of_shards
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
			#print shards
			#sys.exit(1)
			for i in range(len(shards)):
				qry= q # 'SELECT ROWNUM rn, * FROM (%s)' % (q)
				#sys.exit(1)
				#print shards
				#(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				(sid,rowid_from, rowid_to, _) = shards[i]
				#sql_query= 'SELECT * FROM (%s)' % self.from_query[0].strip().strip(';')
				
				if num_of_shards>1:
					
					qry=self.get_sharded_sql(cols_from,qry,rowid_from,rowid_to)
					#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
				#print qry
				qry=self.get_query(cols_from,'(%s)' % qry)
				#print 
				#print qry
				#e(0)
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
				from_pld.append(('Shard-%d' % i,outfn,rowid_from,rowid_to,cols_from,sqfn))

					#globalStatus[i]=(99, None)	
			#pprint (from_pld)
			#pprint(shards)
			#sys.exit(1)

		return (shards,from_pld) 	
	def set_querylist_payload(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		from_pld=[]
		shards=[]
		qid=0
		
		for q in self.from_query:
			#qry= q #'SELECT ROWNUM rn, * FROM (%s)' % (q)
			q=q.strip().strip(';')
			#rc=self.count_rows(q)
			#print rc
			#sys.exit(0)
			#assert shards, 'Cannot create source table %s shards.' % self.from_table
			#print status
			#sys.exit(0)
			#qry='SELECT * FROM (%s)' % q
			#if self.lim:
			#	qry='SELECT %s * FROM (%s)' % (self.lim, q)
			#print qry
			
			(cols_from,status) = self.get_query_columns( q)
			assert cols_from, 'Cannot fetch source query columns'
			#print cols_from
			q= 'SELECT ROWNUM rn, * FROM (%s)' % (q)
			if self.args.lame_duck:
				q='SELECT * FROM (%s) WHERE rn<%s' % ( q, self.args.lame_duck)			
			if 1:
				#sys.exit(1)
				#print shards
				#(sid,rowid_from, rowid_to, _) =  shards[i].strip().split('||')
				#(sid,rowid_from, rowid_to, _) = shards[qid]
				#sql_query= 'SELECT * FROM (%s)' % q
				qry=self.get_query(cols_from,'(%s)' % q)
				sqdir= '%s\\sql' % self.datadir
				sqfn='%s\\spool_table_%s.sql' % (sqdir,qid)
				sqf = open(sqfn, "w")
				sqf.write(qry)
				sqf.close()
				#print qry
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
	def set_query_payload__(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		qry='SELECT * FROM (%s)' % self.from_query[0].strip().strip(';').strip()
		#print qry
		#sys.exit(1)
		(cols_from,status) = self.get_query_columns( qry)
		assert cols_from, 'Cannot fetch source query columns'
		from_pld=[]		
		#globalStatus={}
		from_pld=[]	
		if self.toDb:
			outfn=self.toDb.get_out_fn(0)
		else:
			outfn=self.get_outfn(0)		
		from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,None))
		#print from_pld
		#sys.exit(1)
		#shards=((0,0,0),)
		shards=['0||||||']
		return (shards,from_pld) 			
	def set_querylist_payload_tt(self):
		#options={'_PARTITION':pt}
		options={}
		#tab= ('QUERY' , self.get_temp_table_name())
		
		from_pld=[]
		shards=[]
		qid=0
		
		for q in self.from_query:
			qry='SELECT * FROM (%s)' % q.strip().strip(';').strip()
			#print qry
			#sys.exit(1)
			(cols_from,status) = self.get_query_columns(qry)
			assert cols_from, 'Cannot fetch source query columns'

	
			outfn=os.path.join(os.path.dirname(self.get_outfn(qid)), self.from_query_name[qid])
			from_pld.append(('Shard-%d' % qid,outfn,None,None,cols_from,None))
			shards.append('%s||||||' % qid)
			qid +=1
		return (shards,from_pld) 				
	def set_query_payload_tt(self, num_of_shards,toDb=None):
		
		sql_query =''
		if 0:
			assert os.path.isfile(self.query_sql_file), 'Query file %s is unreadable' % self.query_sql_file

			f = open(self.query_sql_file, 'r')

			sql_query= f.read()
			#sql_query=sql_query.replace('"',"'")
			#print sql_query
			f.close()
			#print sql_query
			#sys.exit(0)
			assert sql_query, 'Query is not set'	
		regexp=re.compile(r'\< ROW COUNT\:,\s+(\d+) \>', re.M|re.I)
		#ROW COUNT:, 12
		#self._pp['FROM_DB'] =self._pp['TO_DB']
		#assert from_db, 'TO_DB is not set.'
		#opt='set heading off  pagesize 0 serveroutput off feedback off echo off\n'
		#opt=''
		#q= 'SET NOCOUNT ON\nSET QUOTED_IDENTIFIER OFF\n%s' % qry
		q="""select 'ROW COUNT:' filter ,count(*) cnt from %s;""" % self.args.from_table.strip()
		#q= sql_query.strip().strip(';')
		#print q
		#sys.exit(1)
		fterm=self.field_term
		r=None
		err=None
		lqfn = self.save_qry('source_row_count',q)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		#regexp=re.compile(r'^(\d+) row', re.M|re.I)
		
		try:
			(r, status,sql_err) = self.do_query(self.log,self.login, None,regexp=regexp,query_file=lqfn, field_term=fterm)
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
		rc=int(r[0])
		#print rc
		#print type(rc)
		#types.TupleType:
		assert rc, 'Source table is empty.'
		assert rc>0, 'Cannot estimate query record count. Exiting...'
		if 0:
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
				outfn=self.get_outfn(i)
				#if 1: #num_of_shards>1:
				qry=self.get_sharded_sql(sql_query,rowid_from,rowid_to,rc,outfn)
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
	def set_table_payload_tt(self,num_of_shards):
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
			(shards, status)=self.get_tab_shards_dbms(self.log,num_of_shards, self.login, self.from_table.split('.'),options)
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
			outfn=self.get_outfn(0)			
			from_pld.append(('Shard-%d' % 0,outfn,None,None,cols_from,None))
			shards=['0||||||']
		return (shards,from_pld) 
		
	def get_inserted_count(self,cnt):
		return cnt
	def get_spool_file_shard(self,shard_name,outfn):
		return (shard_name,outfn, self.get_firstrow(),0)		
	def spool_source_data(self,outfn, spConf, env):
		(shard_name,from_pld,to_pld)=env
		(shard_name,outfn, rowid_from, rowid_to,cols_info,sqfn) = from_pld
		outf=open(outfn, "w")

		#pprint( spConf)
		#e(0)
		#sys.exit(0)
		cmd=  ' '.join(spConf)
		spConf=shlex.split(cmd)
		#print outfn
		p2 = Popen(spConf,stdin=PIPE,  stdout=outf , shell=True )# '-S',  stdin=p1.stdout,
		output, err = p2.communicate()
		#print output 
		#print err
		#sys.exit(0)
		regexp=re.compile(r'^(\d+)/\d+ row[s]? copied', re.M|re.I)
		grp=None
		out=[]
		status=p2.wait()
		#print status
		outf.close()
		if output:
			for o in output.split('\r'):
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
		cnt=-1
		if out:
			cnt=int(out[0])
		if err:
			self.log.error(err)
		#
		#print cnt
		
		return (cnt,status)
	
