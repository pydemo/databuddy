import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_postgresql import PostgreSQL
import codecs, tempfile
from pprint import pprint
e=sys.exit
class ToPostgreSQL(PostgreSQL):
	"""PostgreSQL db"""
	def __init__(self,parent,log,datadir,conf,db='PGRES'):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(self.args.to_user, self.args.to_passwd, self.args.to_db_name, self.args.to_db_server, self.args.target_port)
		PostgreSQL.__init__(self,log,datadir,self.login,conf)
		self.log=log
		#self.login=login
		self.to_table=self.args.to_table
		self.db=db
		#pprint(dir(conf))
		#e(0)
		#print conf
		
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.field_term=self.args.field_term
		#self.wait_sec=int(args.wait_limit_sec)
		self.datadir=datadir
		self.tab_cols={}
		#self.args=args
		self.to_pld={}
		self.db_client_dbshell =None
	def print_copy_details(self):	
		#pprint(dir(self.args))	
		print """		
	To %s:	
		to db: %s
		to table: %s
		""" % (self.db, '%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
	def set_payload(self,shard,num_of_shards, qname=None):
		#options={'_PARTITION':pt}
		return (self.login, self.to_table) 

	def get_db_client_dbshell(self):
		conf=self.conf
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(conf.dbtools['DBSHELL'][self.db])
		if self.args.target_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)	
		return self.db_client_dbshell		
	def get_inserted_count(self,cnt):
		return cnt
	def load_data(self,logger,loadConf,outfn,shard):
		out=[]
		err=[]
		#pprint (loadConf)
		#print shard
		#pprint(self.to_pld)
		
		
		#print shard
		#pprint(self.to_pld)
		(login, to_table, shard_name, infile, row_from, row_to)=self.to_pld[int(shard)]
		#(ss_user, ss_passwd, ss_db_name, ss_db_server)=login
		#(fmtfn,out,status,err)=self.create_format_file(self.log)
		#assert os.path.isfile(fmtfn), 'Format file does not exists'
		#shard=shard_name.split('-')[1]
		
		assert infile, 'Input CSV file is not set.'

		hdr=''
		if row_from or (hasattr(self.args, 'skip_header') and self.args.skip_header):
			hdr='HEADER'
		load_qry ="""COPY %s FROM '%s' WITH DELIMITER '%s' CSV %s""" % (to_table, infile.replace('\\\\','\\').replace('\\','\\\\'),self.args.field_term,hdr)
		#print (load_qry)
		#print to_table, shard_name, infile, row_from, row_to
		
		#sys.exit(0)
		lqfn = self.save_qry('load_query_%s' % shard_name, load_qry)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		regexp=re.compile(r'COPY\s+(\d+)', re.M|re.I)
		#print login
		#e(0)
		(r_int, status, err)=self.do_query(self.log,login, regexp=regexp, query=load_qry,query_file=None)
		#print r_int
		ins_cnt = int(r_int[0][0])
		#sys.exit(0)
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size		
		return (r_int,status,err,ins_cnt,stat)	
	def get_load_config(self,to_pld):
		#(shard_name,from_pld,to_pld)=payload
		#pprint( to_pld)
		#sys.exit(0)
		#(infile, row_from, row_to,field_term) =from_pld
		#(login, to_table, shard_name, infile, row_from, row_to)=to_pld
		#self.to_pld=to_pld
		#(to_user, _passwd, ss_db_name, ss_db_server)=login
		#(fmtfn,out,status,err)=self.create_format_file(self.log)
		#assert os.path.isfile(fmtfn), 'Format file does not exists'
		#shard=shard_name.split('-')[1]
		#ssert infile, 'Input CSV file is not set.'

		#db_client_loc='%s\psql' % self.args.postgres_client_home.strip("'").strip('\\').strip('\\')
		db_client_dbshell=self.get_db_client_dbshell()
		#loadConf=[ client_loc ,'-u', self.args.to_user, '-p%s' % self.args.to_passwd,'-D',self.args.to_db_name, '-h', self.args.to_db_server]
		loadConf=[ db_client_dbshell ,'-U', self.args.to_user,'-d',self.args.to_db_name, '-h', self.args.to_db_server]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
