import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.pipeline import pipeline 
import codecs
from common.v101.exceptions import CopyVectorError
e=sys.exit
class spool_to_file(pipeline):
	"""Spool to File template."""
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
		from_ppl=None
		import all_spoolers as spoolers
		#db=source.upper()[:3]
		#spoolers.get_ppl(source)
		from_ppl=spoolers.get_ppl(source.upper()) #ppl[db]
		#print from_ppl
		assert from_ppl, 'Source pipeline is not set for "%s"' % source
		#self.toDb = to_ppl(log, datadir,self.conf,target.upper())


		if 0:
			if source.upper().startswith('ORA'):		
				from pipeline.v101.from_oracle import FromOracle as from_ppl
			else:
				from pipeline.v101.from_db import FromDb as from_ppl
			self.fromDb = from_ppl(log, datadir, self.conf,db=source.upper())
			
		if target.upper() in ('CSV'):
			from pipeline.v101.to_csv import ToCSV as to_ppl
			self.toDb = to_ppl(self,log, args.to_file, datadir, self.conf)
		elif target.upper() in ('JSON'):
			from pipeline.v101.to_json import ToJSON as to_ppl
			self.toDb = to_ppl(self,log, args.to_file, datadir, self.conf)			
		elif target.upper() in ('DDL'):
			from pipeline.v101.to_ddl import ToDDL as to_ppl
			self.toDb = to_ppl(self,log, args.to_file, datadir, self.conf)			
		else:
			raise CopyVectorError(vector)
		self.fromDb = from_ppl(self,log, datadir, self.conf,db=source.upper())

	def print_copy_details(self):	
		args=self.args
		print '#'*20
		msg={'CSV':"Performing CSV data extraction.",'JSON':"Performing JSON data extraction.",'DDL':"Performing DDL extraction."}
		print msg[self.target.upper()]
		#print self.fromDb
		self.fromDb.print_copy_details()
		#print self.fromDb.outfn
		self.toDb.print_copy_details(self.fromDb.outfn)
		print '#'*20 	
	def execute(self,logger,payload, ts):
		(shard_name,from_pld,to_pld)=payload
		(field_term, limit) =(self.args.field_term, self.args.lame_duck)
		#pprint (from_pld)
		(shard_name,outfn, rowid_from, rowid_to,cols_info, sqfn) =from_pld
		(to_file)=to_pld	
		#status=-1
		extracting={'CSV':'csv','JSON':'js','DDL': 'ddl'}
		if 1:
			#conf=self.fromDb.get_spool_config(payload,field_term,limit)
			if self.target.upper() in ['CSV']:
				conf=self.fromDb.get_spool_config(from_pld)
			if self.target.upper() in ['JSON']:
				conf=self.fromDb.get_spool_config(from_pld)				
			elif self.target.upper() in ['DDL']:
				#pprint(from_pld)
				conf=self.fromDb.get_ddl_extract_config(from_pld)
			else:
				assert self.target.upper() in self.conf.ff, '"%s" File format is not supported.' % self.target.upper()
			#outfn=self.spool_source_data(outfn,conf,payload)
			self.log.info('Extracting %s...' % extracting[self.target.upper()]) 
			(_,sid) =shard_name.split('-')
			#print outfn
			#e(0)
			#outfn= self.toDb.get_out_fn(sid)
			#print outfn	
			#sys.exit(0)
			#print self.conf.ff
			if self.target.upper() in ['CSV']:
				(ins_cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)
			elif self.target.upper() in ['JSON']:
				(ins_cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)				
			elif self.target.upper() in ['DDL']:
				(ins_cnt,status)=self.fromDb.spool_ddl(outfn,conf,payload)
			else:
				assert self.target.upper() in self.conf.ff, '"%s" File format is not supported.' % self.target.upper()
				
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
		#stat=-1
		#if status and status2:
		stat=-1
		#print outfn
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
			
		#print 'spooled %d B' % stat
		#print (stat,status,ins_cnt)
		return (stat,status,ins_cnt)
		
