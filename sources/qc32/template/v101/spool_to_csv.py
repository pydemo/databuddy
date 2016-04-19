import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.pipeline import pipeline 
import codecs
from common.v101.exceptions import CopyVectorError

class spool_to_csv(pipeline):
	"""Spool to CSV template."""
	def __init__(self,log,datadir,conf):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		pipeline.__init__(self,log, args)

		self.fromDb=None
		self.toDb=None
		self.log=log
		self.datadir=datadir
		
		self.field_term=self.args.field_term
		#self.Validate()
		self.Prepare()
	def Prepare(self):
		vector=self.args.copy_vector
		log=self.log
		args=self.args
		uconf=self.uargs
		datadir=self.datadir
		(source,target) = vector.split(self.conf._to)
		assert source.upper() in self.conf.dbs, 'Data source %s is not supported'
		ppl={}
		from_ppl=None
		import all_spoolers as spoolers
		#db=source.upper()[:3]
		#spoolers.get_ppl(source)
		from_ppl=spoolers.get_ppl(source.upper()) #ppl[db]
		#print from_ppl
		assert from_ppl, 'Source pipeline is not set for "%s"' % source
		#self.toDb = to_ppl(log, datadir,self.conf,target.upper())
		self.fromDb = from_ppl(log, datadir, self.conf,db=source.upper())

		
		if source.upper().startswith('ORA'):		
			from pipeline.v101.from_oracle import FromOracle as from_ppl
		self.fromDb = from_ppl(log, datadir, self.conf,db=source.upper())
		if 0:
			if source.upper() in ('ORA11G','EXAD','ORAXE'):
				from pipeline.v101.from_oracle import FromOracle as from_ppl
				self.fromDb = from_ppl(log, args.from_db, args.from_table, datadir, self.conf,db=source.upper())
			elif source.upper() in ('SSENT','SSEXP'):
				from pipeline.v101.from_sqlserver import FromSQLServer as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf,db=source.upper())
			elif source.upper() in ('PGRES'):
				from pipeline.v101.from_postgresql import FromPostgreSQL as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server,args.source_port)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf,db=source.upper())	
			elif source.upper() in ('SYANY','SYASE','SYIQ'):
				from pipeline.v101.from_sybasesqlanywhere import FromSybaseSQLAnywhere as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf,db=source.upper())
			elif source.upper() in ('TTEN'):
				from pipeline.v101.from_timesten import FromTimesTen as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_DSN_name)
				self.fromDb = from_ppl(log, self.from_db, args.from_table, datadir, self.conf,db=source.upper())
			elif source.upper() in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
				from pipeline.v101.from_db2udb import FromDb2UDB as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf, db=source.upper())
			elif source.upper() in ('INFOR','INFORC'):
				from pipeline.v101.from_informix import FromInformix as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf, db=source.upper())
			elif source.upper() in ('MYSQL','INFOB','MARIA'):
				from pipeline.v101.from_mysql import FromMysql as from_ppl
				self.from_db=(args.from_user, args.from_passwd, args.from_db_name, args.from_db_server)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir,  self.conf,db=source.upper())			
			elif source.upper() in ('SLITE'):
				from pipeline.v101.from_sqllite import FromSQLLite as from_ppl
				self.from_db=(args.from_db_name)
				self.fromDb = from_ppl(log, self.from_db, args.query_sql_file, datadir, self.conf, db=source.upper())				
			else:
				raise CopyVectorError(vector)
			
		if target.upper() in ('CSV'):
			from pipeline.v101.to_csv import ToCSV as to_ppl
			self.toDb = to_ppl(log, args.to_file, datadir, self.conf)
		else:
			raise CopyVectorError(vector)


	def print_copy_details(self):	
		args=self.args
		print '#'*20
		print "Performing data extraction."
		#print self.fromDb
		self.fromDb.print_copy_details()
		self.toDb.print_copy_details()
		print '#'*20 	
	def execute(self,logger,payload, ts):
		(shard_name,from_pld,to_pld)=payload
		(field_term, limit) =(self.args.field_term, self.args.lame_duck)
		#pprint (from_pld)
		(shard_name,outfn, rowid_from, rowid_to,cols_info, sqfn) =from_pld
		(to_file)=to_pld	
		#status=-1
		if 1:
			#conf=self.fromDb.get_spool_config(payload,field_term,limit)
			conf=self.fromDb.get_spool_config(from_pld)
			#outfn=self.spool_source_data(outfn,conf,payload)
			self.log.info('Extracting data...')
			(_,sid) =shard_name.split('-')
			outfn= self.toDb.get_out_fn(sid)
			#print outfn	
			#sys.exit(0)
			(ins_cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)
			self.log.info('Done.')
			#print outfn
			#stat=os.stat(outfn).st_size

			#print 'spooled %d B' % stat
			#print (ins_cnt,status)			
			#sys.exit(0)
			if 1:
				#pprint (payload)
				first_row=self.fromDb.get_firstrow()
				conf=self.toDb.get_load_config(field_term,first_row,payload,outfn)
				
				#print conf
				#sys.exit(0)
				#print payload
				#sys.exit(0)
				shard=payload[0].split('-')[1]
				#print shard
				(out,status2,err,_)=self.toDb.load_data(logger,conf,outfn,shard)
				#(out,status,err)=self.load_data(logger,conf)

		else:
			print 'Cannot fetch common columns.'

		stat=os.stat(outfn).st_size
		#print 'spooled %d B' % stat
		#print (stat,status,ins_cnt)
		return (stat,status,ins_cnt)
		
