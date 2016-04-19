import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_sybaseiq import SybaseIQ
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
class ToSybaseIQ(SybaseIQ):
	"""Sybase IQ db"""
	def __init__(self,parent,log,login,to_table,datadir,args):
		SybaseIQ.__init__(self,log,login,datadir,args) 
		self.to_table=to_table
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
	To Sybase IQ:	
		to db: %s
		to table: %s
		""" % ('%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
	def set_payload(self,shard,num_of_shards):
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

		skip=''
		if self.args.skip_rows:
			skip='SKIP %d' % self.args.skip_rows
		#load_qry ="""COPY %s FROM '%s' DELIMITER '%s' CSV %s""" % (to_table, infile.replace('\\\\','\\').replace('\\','\\\\'),self.args.field_term,hdr)
		#print self.args.skip_rows
		load_qry ="""INPUT INTO "%s" DELIMITED BY '%s' FROM '%s' %s;\nexit;\n""" % (to_table, self.args.field_term,infile.replace('\\\\','\\').replace('\\','\\\\'),skip)
		#print (load_qry)
		#print to_table, shard_name, infile, row_from, row_to
		
		#sys.exit(0)
		lqfn = self.save_qry('load_query_%s' % shard_name, load_qry)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		regexp=re.compile(r'^(\d+) row', re.M|re.I)
		
		(r_int, status, err)=self.do_query(self.log,login, regexp=regexp, query=None,query_file=lqfn)
		#print r_int
		#sys.exit(0)
		ins_cnt = int(r_int[0])
		#sys.exit(0)
		return (r_int,status,err,ins_cnt)	
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

				
		db_client_loc=self.get_db_client_loc()
		
		#print db_client_loc
		
		#sys.exit(0)
		
		#dbisql.com  
		#loadConf=[ client_loc ,'-u', self.args.to_user, '-p%s' % self.args.to_passwd,'-D',self.args.to_db_name, '-h', self.args.to_db_server]
		connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.to_user,self.args.to_passwd, self.args.to_db_name, self.args.to_db_server)
		loadConf=[ db_client_loc ,'-nogui','-c', connect_str]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
