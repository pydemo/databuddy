import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_sybasesqlanywhere import SybaseSQLAnywhere
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf
import config.config as conf 
class ToSybaseSQLAnywhere(SybaseSQLAnywhere):
	"""SybaseSQLAnywhere db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(args.to_user, args.to_passwd, args.to_db_name, args.to_db_server)
		SybaseSQLAnywhere.__init__(self,log,self.login,datadir,args) 
		self.to_table=self.args.to_table
		#print self.uargs.db
		self.uargs_db=self.uargs.target.target(self.log,datadir,self.login,self.conf,db,self.args.to_table)
		self.db=db
		if 0:
			self.log=log
			self.login=login
			#self.to_table=to_table
			#self.ss_user=ss_user
			#self.ss_passwd=ss_passwd
			#self.ss_db_name=ss_db_name
			#self.ss_db_server=ss_db_server
			self.field_term=args.field_term
			#self.wait_sec=int(args.wait_limit_sec)
			self.datadir=datadir
			self.tab_cols={}
			self.args=args

	def print_copy_details(self):		
		print """		
	To %s:	
		to db: %s
		to table: %s
		""" % (self.conf.dbs[self.db],'%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
	def set_payload(self,shard,num_of_shards, qname=None):
		#options={'_PARTITION':pt}
		return (self.login, self.to_table) 	
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

		load_qry = self.uargs_db.get_load_query(infile)
		#print (load_qry)
		#print to_table, shard_name, infile, row_from, row_to
		
		#sys.exit(0)
		lqfn = self.save_qry('load_query_%s' % shard_name, load_qry)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		regexp=re.compile(r'^(\d+) row', re.M|re.I)
		
		(r_int, status, err)=self.do_query(self.log,login, regexp=regexp, query=None,query_file=lqfn)
		ins_cnt=-1
		if not r_int:
			status=1
		else:
			ins_cnt = int(r_int[0][0])
		#sys.exit(0)
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size		
		return (r_int,status,err,ins_cnt,stat)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['LOADER']['SYANY'])
		if self.args.target_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['LOADER']['SYANY']
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to target loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc
	def get_load_config(self,to_pld):
				
		db_client_loc=self.get_db_client_loc()
		
		connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.to_user,self.args.to_passwd, self.args.to_db_name, self.args.to_db_server)
		loadConf=[ db_client_loc ,'-nogui','-c', connect_str]
		return loadConf		
	
	
	
