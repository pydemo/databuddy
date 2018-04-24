import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_mariadb import MariaDB
import codecs, tempfile
from pprint import pprint
import config.config as conf
#import common.v101.config as conf 
class ToMariaDB(MariaDB):
	"""MariaDB db"""
	def __init__(self,parent,log,datadir,conf, db):
		self.conf=conf
		self.args=conf.args		
		self.login=(self.args.to_user, self.args.to_passwd, self.args.to_db_name, self.args.to_db_server)

		MariaDB.__init__(self,log,self.login,datadir,args) 
		self.log=log
		#self.login=login
		self.to_table=self.args.to_table
		self.db=db
		#print self.db
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.field_term=args.field_term
		#self.wait_sec=int(args.wait_limit_sec)
		self.datadir=datadir
		self.tab_cols={}
		self.args=args
		self.to_pld={}
	def print_copy_details(self):		
		print """		
	To %s:	
		to db: %s
		to table: %s
		""" % (conf.dbs[self.db], '%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
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
		lr=''
		if row_to:
			lr=""",
	LASTROW = %s""" % row_to
		load_qry="""LOAD DATA  INFILE '%s' INTO TABLE %s
FIELDS OPTIONALLY ENCLOSED BY '"' TERMINATED BY '%s'
LINES TERMINATED BY '
';
SELECT ROW_COUNT();
""" % (infile.replace('\\\\','\\').replace('\\','\\\\'), to_table, self.args.field_term)
		#print (load_qry)
		#pprint (loadConf)
		os.environ['MYSQL_HOME'] = r'%s\data' % conf.dbclients[self.db][:-3]
		p2 = Popen(loadConf,stdin=PIPE,  stdout=PIPE)# '-S',  stdin=p1.stdout,
		output, err = p2.communicate(load_qry)
		#pprint(output)
		#print err
		if err:
			self.log.error(err)
		#sys.exit(0)
		status=p2.wait()
		ins_cnt = -1
		grp=None
		out=[]
		status=p2.wait()
		#sys.exit(0)
		regexp=re.compile(r'^(\d+)')
		for o in output.split('\r'):
		#while output:
			#output = p2.stdout.readline()
			#pprint(o.strip())
			#if o.strip():					
			#	logger.info( output.strip())
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
		ins_cnt=-1
		if out:
			ins_cnt=int(out[0])
		else:
			print output
			if err:
				self.log.error(err)
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
		return (output,status,err,ins_cnt,stat)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['LOADER'][self.db])
		if self.args.target_client_home:
			
			self.db_client_loc=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
			#print self.args.target_client_home
			#print 1,self.db_client_loc
		else:
			self.db_client_loc=conf.dbtools['LOADER'][self.db]
			
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


		
		loadConf=[ db_client_loc ,'-u', self.args.to_user, '-p%s' % self.args.to_passwd,'-D',self.args.to_db_name, '-h', self.args.to_db_server]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
