import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_timesten import TimesTen
import codecs, tempfile
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf
import shlex
e=sys.exit
class ToTimesTen(TimesTen):
	"""TimesTen db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(args.to_user, args.to_passwd, args.to_DSN_name)
		TimesTen.__init__(self,log, self.login,datadir,conf.args) 
		self.to_table=self.args.to_table
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
	To TimesTen:	
		to db: %s
		to table: %s
		""" % ('%s@%s' % (self.args.to_user,self.args.to_DSN_name),self.to_table)
	def set_payload(self,shard,num_of_shards,qname=None):
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
		#if self.args.skip_rows:
		#	skip='SKIP %d' % self.args.skip_rows
		#load_qry ="""COPY %s FROM '%s' DELIMITER '%s' CSV %s""" % (to_table, infile.replace('\\\\','\\').replace('\\','\\\\'),self.args.field_term,hdr)
		#print self.args.skip_rows
		#load_qry ="""INPUT INTO "%s" DELIMITED BY '%s' FROM '%s' %s;\nexit;\n""" % (to_table, self.args.field_term,infile.replace('\\\\','\\').replace('\\','\\\\'),skip)
		#print (load_qry)
		#print to_table, shard_name, infile, row_from, row_to
		
		#sys.exit(0)
		#lqfn = self.save_qry('load_query_%s' % shard_name, load_qry)
		
		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		regexp=re.compile(r'(\d+) row[s]? inserted', re.M|re.I)
		#print ' '.join(loadConf)
		#"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttBulkCp.exe" -i -dformat YYYY-MM-DD -tsformat YYYY-MM-DD HH24.MI.SS.FF -s ^| -Q 0 -F 100  -connstr "UID=TERRY;PWD=secret;DSN=my_ttdb;" TERRY.Persons_pipe_datetime_1 "c:\Python27\csvloader_1237\test\v101\data\tt_shard_0.data"
		
		
		#print 	self.get_db_shell_path()
		#spConf=shlex.split(' '.join(loadConf)) 
		#pprint(loadConf)
		#e(0)
		p2 = Popen(loadConf,stdin=PIPE,  stdout=PIPE , shell=True )# '-S',  stdin=p1.stdout,
		output, err = p2.communicate()
		#print output
		#print err
		grp=None
		out=[]
		status=p2.wait()
		for o in output.split('\r'):
		#while output:
			#output = p2.stdout.readline()
			#pprint(o)
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
		if err:
			self.log.error(err)		
		cnt=int(out[0])
		#print cnt
		#sys.exit(0)
		#ins_cnt = int(r_int[0])
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
		return (out,status,err,cnt,stat)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['LOADER']['TTEN'])
		if self.args.target_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['LOADER']['TTEN']
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to target loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc
	def get_db_shell_path(self):
		if self.db_shell_path:
			return self.db_shell_path
		dbshell= os.path.basename(conf.dbtools['DBSHELL']['TTEN'])
		if self.args.target_client_home:
			self.db_shell_path=(r'%s\%s' % (self.args.target_client_home, dbshell)).strip("'").strip('\\').strip('\\')
		else:
			self.db_shell_path=conf.dbtools['DBSHELL']['TTEN']
			if not os.path.isfile(self.db_shell_path):
				self.log.warn('Path to source dbshell is not set. Defaulting to %' % dbshell)	
		return self.db_shell_path			
	def get_load_config(self,to_pld):
		#(shard_name,from_pld,to_pld)=payload
		#pprint( to_pld)
		#sys.exit(0)
		(login, to_table, shard_name,infile, row_from,row_to) =to_pld
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
		db_client_loc=self.get_db_client_loc()
		#spConf=[ db_client_loc ,'-U', self.args.from_user,'-d',self.args.from_db_name, '-h', self.args.from_db_server, '-f',sqfn]
		#connect_str= 'UID=%s;PWD=%s;DSN=%s;' % tuple(login, connect_str)
		#pprint(dir(self.uargs))
		#print self.uargs
		#self.uargs_db.get_load_config(db_loader_loc,shard_name,row_from, row_to,ctlfn,outfn,self.datadir)
		loadConf=self.uargs_db.get_load_config(db_client_loc,infile)
				
		#connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (self.args.to_user,self.args.to_passwd, self.args.to_db_name, self.args.to_db_server)
		#loadConf=[ db_client_loc ,'-nogui','-c', connect_str]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
