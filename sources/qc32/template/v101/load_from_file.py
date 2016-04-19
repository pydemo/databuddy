import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.pipeline import pipeline 
import codecs
from common.v101.exceptions import CopyVectorError

class load_from_file(pipeline):
	"""Load from File template."""
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
		(self.source,self.target) = vector.split(self.conf._to)
		(source,target)= (self.source,self.target)
		
		assert source.upper() in self.conf.dbs, 'Data source %s is not supported'
		ppl={}
		to_ppl=None
		input_files=self.args.input_files
		if source.upper() in ('CSV'):
			from pipeline.v101.from_csv import FromCSV as from_ppl
			self.fromDb = from_ppl(self,log, input_files,self.args.skip_rows, datadir, self.conf)
		elif source.upper() in ('JSON'):
			from pipeline.v101.from_json import FromJSON as from_ppl
			self.fromDb = from_ppl(self,log, input_files, datadir, self.conf)			
		elif source.upper() in ('DDL'):
			from pipeline.v101.from_ddl import FromDDL as from_ppl
			self.fromDb = from_ppl(self,log, input_files,skip_rows, datadir, self.conf)			
		else:
			raise CopyVectorError(vector)
			
		import all_loaders as loaders
		#db=source.upper()[:3]
		#spoolers.get_ppl(source)
		to_ppl=loaders.get_ppl(target.upper()) #ppl[db]
		#print from_ppl
		assert to_ppl, 'Target pipeline is not set for "%s"' % source
		self.toDb = to_ppl(self,log, datadir,self.conf,target.upper())
		#self.fromDb = from_ppl(log, datadir, self.conf,db=source.upper())

		



	def print_copy_details(self):	
		args=self.args
		print '#'*20
		msg={'CSV':"Performing CSV data extraction.",'JSON':"Performing JSON data extraction.",'DDL':"Performing DDL extraction."}
		#print msg[self.source.upper()]
		#print self.fromDb
		self.fromDb.print_copy_details()
		self.toDb.print_copy_details()
		print '#'*20 	
	def execute(self,logger,payload, ts):
		(shard_name,from_pld,login_tab)=payload
		to_login, to_tab=login_tab
		(field_term, limit) =(self.args.field_term, self.args.lame_duck)
		#pprint (from_pld)
		#(shard_name,outfn, rowid_from, rowid_to,cols_info, sqfn) =from_pld
		(shard_name, outfn, row_from,row_to,field_term) =from_pld
		#(to_file)=to_pld	
		#status=-1
		extracting={'CSV':'csv','JSON':'js','DDL': 'ddl'}
		#sconf=self.get_spool_config(payload,field_term,lame_duck)
		#	assert sconf, 'Spool config is not set.'
			
			
		sconf=None
		if 1:
			#conf=self.fromDb.get_spool_config(payload,field_term,limit)
			if 1:
				if self.source.upper() in ['CSV']:
					sconf=self.fromDb.get_spool_config(payload)
				if self.source.upper() in ['JSON']:
					sconf=self.fromDb.get_spool_config(payload)				
				elif self.source.upper() in ['DDL']:
					#pprint(from_pld)
					sconf=self.fromDb.get_ddl_extract_config(from_pld)
				else:
					assert self.source.upper() in self.conf.ff, '"%s" File format is not supported.' % self.source.upper()
			assert sconf, 'Spool config is not set.'
			#outfn=self.spool_source_data(outfn,conf,payload)
			#self.log.info('Extrac to %s...' % extracting[self.target.upper()]) 
			#(_,sid) =shard_name.split('-')
			#outfn= self.toDb.get_out_fn(sid)
			#print outfn	
			#sys.exit(0)
			#print self.conf.ff
			#status=self.spool_source_data(sconf,payload)
			
			if self.target.upper() in ['CSV']:
				(ins_cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)
			elif self.target.upper() in ['JSON']:
				status=self.spool_source_data(sconf,payload)
				#(ins_cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)				
			elif self.target.upper() in ['DDL']:
				(ins_cnt,status)=self.fromDb.spool_ddl(outfn,conf,payload)
			else:
				assert self.source.upper() in self.conf.ff, '"%s" Source file format is not supported.' % self.target.upper()
			
			#self.log.info('Done.')
			#print outfn
			#stat=os.stat(outfn).st_size

			#print 'spooled %d B' % stat
			#print (ins_cnt,status)			
			#sys.exit(0)
			if 1:
				#pprint (payload)
				first_row=self.fromDb.get_firstrow()
				#(shard_name, outfn,row_from, row_to, field_term) = from_pld
				#login, to_table, shard_name,outfn,row_from, row_to 
				#print payload
				conf=self.toDb.get_load_config((to_login, to_tab, shard_name,outfn,row_from, row_to))
				#conf=self.toDb.get_load_config(field_term,first_row,payload,outfn)
				
				#print conf
				#sys.exit(0)
				#print payload
				#sys.exit(0)
				shard=payload[0].split('-')[1]
				#print shard
				self.log.info('Loading to %s...' % self.target.upper()) 
				(out,status,err,count,stat)=self.toDb.load_data(logger,conf,outfn,shard)
				#(out,status,err)=self.load_data(logger,conf)


		#stat=-1
		#if status and status2:
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
			
		#print 'spooled %d B' % stat
		#print (stat,status,count)
		return (stat,status,count)
		
