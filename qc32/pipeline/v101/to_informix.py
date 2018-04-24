import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_informix import Informix
import codecs, tempfile
from pprint import pprint
import config.config as conf
#import common.v101.config as conf 
e=sys.exit
class ToInformix(Informix):
	"""Informix db"""
	def __init__(self,parent,log,datadir,conf,db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(args.to_user, args.to_passwd, args.to_db_name, args.to_db_server)
		Informix.__init__(self,log,self.login,datadir,self.args) 
		self.to_table=self.args.to_table
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
		""" % (conf.dbs[self.db],'%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
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

		#(r, status) = do_query(from_db, "%s%s"  % (opt,q),0,regexp)
		
		#os.environ['DB2CLP'] = 'DB20FADE'
		#os.environ['DB2INSTANCE'] = 'DB2'
		#os.environ['DB2PATH'] = r'C:\Program Files (x86)\IBM\SQLLIB_01'
		#cmd=r'db2.exe -f "%s" -z C:\\Python27\\data_mule_db2\\DB2UploadLog.txt' % sqfn
		#spConf=shlex.split(cmd) 

		#pprint (loadConf)
		#cmd = ' '.join(loadConf)
		#print cmd
		#sys.exit(0)

		#(dConf,lqfn)=(loadConf[:-1], loadConf[-1])
		#print loadConf,lqfn
		#sys.exit(0)
		#print lqfn
		lqfn=loadConf[2]
		#qry= (open(lqfn, 'r')).read()
		#sys.exit(0)
		loadConf[1]='-'
		#pprint (loadConf)
		
		#qry="CONNECT to '%s@%s2' user %s USING %s;\n%s" % (self.args.to_db_name, self.args.to_db_server, self.args.to_user, self.args.to_passwd,  qry)	
		#pprint(qry)
		print ' '.join(loadConf)
		#	e(0)
		p2 = Popen(loadConf,stdin=PIPE,  stdout=PIPE, stderr=PIPE)# '-S',  stdin=p1.stdout,
	
		#p2 = Popen(['cmd','/C',r'C:\Python27\data_mule_db2\run.bat'],stdin=PIPE,  stdout=PIPE, **kwargs )# '-S',  stdin=p1.stdout,
		err, output = p2.communicate()
		#print output 
		#print err
		#sys.exit(0)

		grp=None
		out=[]
		status=p2.wait()
		#sys.exit(0)
		regexp=re.compile(r'(\d+) row\(s\) loaded')
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
		#
		

		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size			
		return (output,status,err,ins_cnt, stat)	
	def get_db_client_loc(self):
		if self.db_client_loc:
			return self.db_client_loc
		loader= os.path.basename(conf.dbtools['LOADER'][self.db])
		if self.args.target_client_home:
			self.db_client_loc=(r'%s\%s' % (self.args.target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_loc=conf.dbtools['LOADER'][self.db]
			if not os.path.isfile(self.db_client_loc):
				self.log.warn('Path to target loader is not set. Defaulting to %' % loader)	
		return self.db_client_loc
	def get_sharded_sql(self,to_table,rowid_from,rowid_to, rc,infile):
		#sql_query=sql_query.strip().strip(';')
		from_to=''
		#print rowid_from,rowid_to
		#sys.exit(0)
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
		#if self.args.header:
		#	hdr=' WITH COLUMN NAMES'
	
		out=r"""
CONNECT to '%s@%s' user %s using '%s';
LOAD FROM "%s" DELIMITER '%s' INSERT INTO %s;
""" % (self.args.to_db_name, self.args.to_db_server, self.args.to_user, self.args.to_passwd,   os.path.normpath(infile),self.args.field_term,to_table.strip().strip(';'))	
		#print out
		#e(0)
		#sys.exit(0)
		return out
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
#SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;
		
	def get_load_config(self,to_pld):
		#(shard_name,from_pld,to_pld)=payload
		#pprint( to_pld)
		#sys.exit(0)
		#(infile, row_from, row_to,field_term) =from_pld
		
		(login, to_table, shard_name, infile, row_from, row_to)=to_pld
		#print infile
		#self.to_pld=to_pld
		#(to_user, _passwd, ss_db_name, ss_db_server)=login
		#(fmtfn,out,status,err)=self.create_format_file(self.log)
		#assert os.path.isfile(fmtfn), 'Format file does not exists'
		#shard=shard_name.split('-')[1]
		#ssert infile, 'Input CSV file is not set.'

				
		db_client_loc=self.get_db_client_loc()
		qry=self.uargs.target.get_load_query(infile)
		#e(0)
		#self.get_sharded_sql(to_table,row_from,row_to,-1,infile)
		#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
		#print qry
		#sys.exit(0)

		lqfn = self.save_qry('load_query_%s' % shard_name, qry)

		#loadConf=[ db_client_loc , '-f', lqfn, '-z' ,r'%s\\load_log.txt' % self.datadir]
		loadConf=[ db_client_loc , '%s@%s' % (self.args.to_db_name, self.args.to_db_server), lqfn]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
