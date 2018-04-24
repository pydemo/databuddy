import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_db2udb import Db2UDB
import codecs, tempfile
from pprint import pprint
import config.config as conf
#import common.v101.config as conf 
e=sys.exit
class ToDb2UDB(Db2UDB):
	"""Sybase ASE db"""
	def __init__(self,parent,log,datadir,conf, db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.login=(conf.args.to_user, conf.args.to_passwd, conf.args.to_db_name, conf.args.to_db_server)
		Db2UDB.__init__(self,log,self.login, datadir, conf.args) 
		
		self.to_table=self.args.to_table
		self.db=db	
		self.etl=self.uargs.target.target(datadir,self.login,self.conf,db,self.args.to_table)
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
		(login, to_table, shard_name, infile, row_from, row_to)=self.to_pld[int(shard)]
		assert infile, 'Input CSV file is not set.'
		regexp=re.compile(r'^Number of rows committed\s+=\s+(\d+)', re.M|re.I)
		os.environ['DB2CLP'] = 'DB20FADE'
		os.environ['DB2INSTANCE'] = 'DB2'
		os.environ['DB2PATH'] = r'C:\Program Files (x86)\IBM\SQLLIB_01'
		cmd = ' '.join(loadConf)
		print cmd
		p2 = Popen(loadConf,stdin=PIPE,  stdout=PIPE, shell=True)# '-S',  stdin=p1.stdout,
	
		output, error = p2.communicate()
		print output
		print error
		if error:
			self.log.err(error)
		err=[]
		grp=None
		out=[]
		status=p2.wait()
		for o in output.split(os.linesep):
			if o.startswith ('Number of rows rejected     ='):
				rcnt=int(o.split('Number of rows rejected     =')[1].strip())
				print rcnt
				if rcnt:
					print o
					err.append(o)

			if regexp:
				m = re.match(regexp, o.strip()) 
				if m:
					if grp:
						out.append(m.group(grp))
					else:
						groups=m.groups()
						if groups:
							out.append(groups)
											
		ins_cnt=int(out[0][0])
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

		hdr=''
		#if self.args.header:
		#	hdr=' WITH COLUMN NAMES'
		#print self.login
		#e(0)

		#pprint (dir(self.args))
		out=self.etl.get_load_query(os.path.normpath(infile).replace("\\", "\\\\"))
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
		qry=self.get_sharded_sql(to_table,row_from,row_to,-1,infile)
		#	#qry=get_sharded_sql(sql_query,rowid_from,rowid_to)
		#print qry
		#sys.exit(0)

		lqfn = self.save_qry('load_query_%s' % shard_name, qry)

		loadConf=[ db_client_loc , '-f', lqfn, '-z' ,r'%s\\load_log.txt' % self.datadir]
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		return loadConf		
	
