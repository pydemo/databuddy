import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.pipeline import pipeline 
#import common.v101.config as conf  
import config.config as conf
import codecs
from common.v101.exceptions import CopyVectorError
#datadir=''

import imp
import os
e=sys.exit
def load_from_file(filepath,expected_class):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)

	if hasattr(py_mod, expected_class):
		class_inst = getattr(py_mod, expected_class)

	return class_inst
		
class load_from_csv(pipeline):
	"""Load from CSV template"""
	def __init__(self,log,datadir,conf):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		pipeline.__init__(self,log, args)
		#self.fromDb=dbFrom
		#self.toDb=dbTo
		self.fromDb=None
		self.toDb=None
		self.log=log
		self.datadir=datadir
		
		self.field_term=args.field_term
		self.args=args
		
		self.Prepare()
	def Prepare(self):
		
		vector=self.args.copy_vector
		datadir=self.datadir
		log=self.log
		args=self.args
		#assert os.path.isfile(args.input_file), 'Missing input file %s' % args.input_file
		(source,target) = vector.split(self.conf._to)
		


		ppl={}
		if source.upper() in ('CSV'):
			 
			self.no_sharded_load(source,target)

			from pipeline.v101.from_csv import FromCSV as from_ppl
			self.fromDb = from_ppl(log,args.input_files,args.skip_rows,datadir,self.conf)
		else:
			raise CopyVectorError(vector)
		to_ppl=None
		db=target.upper()[:3]
		import all_loaders as loaders
		to_ppl=loaders.get_ppl(target.upper()) #ppl[db]
		self.toDb = to_ppl(log, datadir,self.conf,target.upper())

	def truncate_target(self):

		if self.fromDb.IF:			
			self.log.warn('Source is file.')
			#self.truncate_table()
		elif self.fromDb.ID:			
			self.log.warn('Source is dir.')
		
		self.toDb.truncate_target()		
		
	def no_sharded_load(self,from_db,to_db):
		if to_db.upper() in ('MARIA','MYSQL','INFOB'):
			assert self.args.num_of_shards==1, 'Sharded load from %s to %s is not supported.' % (from_db.upper(), to_db.upper())
	def print_copy_details(self):	
		args=self.args
		print '#'*20
		print "Performing data load."
		self.fromDb.print_copy_details()
		self.toDb.print_copy_details()

		print '#'*20 

	def set_payload_old(self):
		print ''
		args=self.args
		(num_of_shards,lame_duck) = (args.num_of_shards,args.lame_duck)
		assert self.datadir, 'datadir is not set'
		
		for inf in self.fromDb.input_file:

			#print num_of_rows
			#sys.exit(1)
			
			#num_of_lines=1450000
			(shards,from_pld) = self.fromDb.set_payload( num_of_shards)
			#pprint(from_pld)
			#sys.exit(0)
			
			nameList=[]		
			globalStatus={}
			
			#(to_db,to_table)
			for i in range(len(from_pld)):	
				to_pld=self.toDb.set_payload(i,num_of_shards)
				nameList.append(("Shard-%d" % i,from_pld[i],to_pld))
				globalStatus[i]=(-1, -1,-1)	
			#print (nameList)
			#pprint(nameList)
			#sys.exit(1)
		return (nameList,globalStatus) 		
	def spool_source_data(self,spConf, payload):
		return 0
	def get_load_config_old(self,payload):
		(shard_name,from_pld,to_pld)=payload
		#(shard_name, rowid_from, rowid_to,outfn,cols_info) =from_pld
		#(login, to_table)=to_pld	
		(shard_name, outfn, row_from,row_to,field_term) =from_pld	
		(login, to_table)=to_pld
		to_pld=list(to_pld)
		to_pld.append(row_from)
		to_pld.append(row_to)
		#print to_pld
		conf=self.toDb.get_load_config( to_pld)
		return conf
	def get_load_config(self,to_pld, file_shard):
		#(shard_name,from_pld,to_pld)=payload
		#(shard_name, rowid_from, rowid_to,outfn,cols_info) =from_pld
		#(login, to_table)=to_pld	
		#(shard_name, outfn, row_from,row_to,field_term) =from_pld	
		(shard_name, outfn,row_from, row_to)=file_shard

		(login, to_table)=to_pld
		to_pld=list(to_pld)
		to_pld.append(shard_name)
		to_pld.append(outfn)
		to_pld.append(row_from)
		to_pld.append(row_to)
		#print to_pld
		conf=self.toDb.get_load_config( to_pld)
		#pprint( to_pld)
		self.toDb.to_pld[int(shard_name.split('-')[1])]=to_pld
		#print int(shard_name.split('-')[1])
		#pprint(file_shard)
		#e(0)
		#sys.exit(0)
		
		return conf	
		
	def ckey2cols(self, col_key):
		return map(lambda x: x.split(':')[0],col_key)	
	def get_temp_token(self):
		temp_file_name=tempfile.mkstemp()[1].split('\\')[-1]
		return temp_file_name.strip('/tmp')			

	def get_temp_table_name(self):
		return 'TCL_%s' % self.get_temp_token()

	def	get_spool_config(self,payload,field_term,lame_duck):

		(shard_name,from_pld,to_pld)=payload
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		spConf=self.fromDb.get_spool_config(from_pld)
		#print self.fromDb
		#print self.fromDb.input_file
		#sys.exit(0)
		return spConf	
	def create_format_file(self,logger):
		out=[]
		err=[]
		fmtfn='%s\\to_fmt.fmt' % self.datadir
		#sys.exit(0)
		loadConf=['bcp', 'master.dbo.Persons_pipe2', 'format', 'nul', '-N', '-f', fmtfn,  '-U', 'sa',  '-P', '198Morgan', '-S', 'ALEX_BUZ-PC\SQLEXPRESS', '-T']
		p3 = Popen(loadConf, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		output=' '
		while output:
			output = p3.stdout.readline()
			#print output
			out.append(output)
		status=p3.wait()
		if status==0:
			logger.info('SQL*Loader status =%s' % status)
		if status!=0:
			logger.error('SQL*Loader status =%s' % status)
		if 1:
			
			error=' '
			while error:
				error = p3.stderr.readline()
				logger.error(error)
				err.append(error)
			status = p3.wait()
		return (fmtfn,out,status,err)		
	
	def execute(self,logger,payload, ts):
		(field_term,lame_duck) =(self.args.field_term,self.args.lame_duck) 
		#(shard_name,from_pld,to_pld)=payload
		#(shard_name, outfn) =from_pld[:2]
		(shard_name,from_pld,to_pld)=payload
		#(shard_name, rowid_from, rowid_to,outfn,cols_info) =from_pld
		#(login, to_table)=to_pld	
		(shard_name, outfn, row_from,row_to,field_term) =from_pld		
		#print(from_pld)
		#e(0)
		status=-1
		if 1:
			(shard_name,from_pld,to_pld)=payload
			#print shard_name
			#print 'from'*20
			#pprint(from_pld)
			#print 'to'*20
			#pprint(to_pld)
			#print '#'*20
			
			sconf=self.get_spool_config(payload,field_term,lame_duck)
			assert sconf, 'Spool config is not set.'
			
			status=self.spool_source_data(sconf,payload)
			#print status
			#outfn=conf
			#print conf
			#sys.exit(0)
			#print outfn
			stat=os.stat(outfn).st_size
			#print stat
			#self.log.info('CSV file size %d B' % stat)
			#sys.exit(0)
			file_shard=self.fromDb.get_spool_file_shard(shard_name,outfn)
			#print file_shard
			if 1:
				#pprint (payload)
				#first_row=self.fromDb.get_firstrow()
				#last_row=100
				lconf=self.get_load_config( to_pld,file_shard)
				
				#pprint(lconf)
				#e(0)
				#sys.exit(0)
				#print conf
				#sys.exit(0)
				#print payload
				#sys.exit(0)
				shard=shard_name.split('-')[1]
				#print shard
				self.log.info('Loading data...')
				(out,status,err,ins_cnt, spool_size)=self.toDb.load_data(logger,lconf,outfn,shard)
				#print err
				if (err and err[0]) or status:
					if err:
						print err
					self.log.error('Completed with errors.')
					#e(1)
				else:
					self.log.info('Done.')
				#print out,status,err,ins_cnt
				#sys.exit(1)
				#(out,status,err)=self.load_data(logger,conf)

		else:
			print 'Cannot fetch common columns.'

		#stat=os.stat(outfn).st_size
		#print 'spooled %d B' % stat
		#print ins_cnt	
		return (spool_size,status,ins_cnt)
		
	

	