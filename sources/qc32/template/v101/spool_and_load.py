import re, types, string, sys,  time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.pipeline import pipeline  
import codecs
from common.v101.exceptions import CopyVectorError
import all_spoolers as spoolers
import errno
import os

#datadir=''
e=sys.exit
		
		
class spool_and_load(pipeline):
	"""Spool and load template."""
	def __init__(self,log,datadir,conf):
		self.fromDb=None
		self.toDb=None
		self.log=log
		self.datadir=datadir
		#pprint(dir(conf))
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.field_term=args.field_term
		self.args=args
		self.Prepare()
	def Prepare(self):
		vector=self.args.copy_vector
		log=self.log
		datadir=self.datadir
		args=self.args
		(source,target) = vector.split(self.conf._to)
		#print source,target
		#print source.upper() in ('ORA')
		from_ppl=None
		self.fromDb=None
		#db=source.upper()[:3]
		#spoolers.get_ppl(source)
		from_ppl=spoolers.get_ppl(source.upper()) #ppl[db]
		#print from_ppl
		assert from_ppl, 'Source pipeline is not set for "%s"' % source
		print self.conf.dbs.keys()
		if source.upper() in [x for x in self.conf.dbs.keys()]: # if x not in self.conf.dt]:		
			self.fromDb = from_ppl(self,log, datadir, self.conf,db=source.upper())	

		to_ppl=None
		#db=target.upper()[:3]
		import all_loaders as loaders
		to_ppl=loaders.get_ppl(target.upper()) #ppl[db]
		print to_ppl		
		self.toDb = to_ppl(self, log, datadir,self.conf,target.upper())	
		if not self.fromDb:
			self.fromDb = from_ppl(self,log, datadir, self.conf,db=source.upper())
	def print_copy_details(self):	
		args=self.args
		print '#'*20
		print "Performing data copy."
		self.fromDb.print_copy_details()
		self.toDb.print_copy_details()

		print '#'*20 
	#truncate_target
			
	def set_payload(self):				
		assert self.datadir, 'datadir is not set'
		(num_of_shards,limit) =(self.args.num_of_shards,self.args.lame_duck)
		
		(shards,from_pld) = self.fromDb.set_payload(num_of_shards)

		nameList=[]		
		globalStatus={}
		
		#(to_db,to_table)
		#pprint (from_pld)
		#from_pld[0][-2]
		#e(0)
		for i in range(len(from_pld)):
			qname=from_pld[i][-2]
			#e(0)
			print i,num_of_shards,qname
			to_pld=self.toDb.set_payload(i,num_of_shards,qname)
			nameList.append(("Shard-%d" % i,from_pld[i],to_pld))
			globalStatus[i]=(-1, -1,-1)	
		#pprint(nameList)
		#e(0)
		return (nameList,globalStatus) 		


	def remove_file(self,fn):
		"""		
		[name for name in dir(win32con) if name.startswith("FILE_ATTRIBUTE_")]
		"""
		
		eid=errno.EACCES
		while eid in (errno.EACCES,):
			try:
				import os
				#print 'removing', fn
				os.remove(fn)
				eid=0
			except OSError as e:
				#print 'ERROR:', e.errno
				eid=e.errno
				if eid in (errno.EACCES,):
					#print 'skipping'
					time.sleep(10)
				else:
					raise

		
	def	get_spool_config1(self,payload,field_term,limit):

		(shard_name,from_pld,to_pld)=payload
		#(rowid_from,rowid_to,ctlfn,from_db,from_tab,cols_from)=from_pld
		spConf=self.fromDb.get_spool_config(from_pld,field_term,limit)
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
		#sys.exit(0)
		self.toDb.to_pld[int(shard_name.split('-')[1])]=to_pld
		return conf	
	def execute(self,logger,payload, ts):
		(field_term,limit) =(self.args.field_term,self.args.lame_duck) 
		(shard_name,from_pld,to_pld)=payload
		#pprint(payload)
		#e(0)
		#sys.exit(0)
		(_,outfn) =from_pld[:2]
		(login, to_table)=to_pld
		status=-1
		if 1:
			conf=self.fromDb.get_spool_config(from_pld)
			#pprint(conf)
			#e(0)
			#sys.exit(1)
			
			#status=self.spool_source_data(outfn,conf,payload)
			self.log.info('Extracting data...')
			if os.path.isfile(outfn):
				os.remove(outfn)
			(cnt,status)=self.fromDb.spool_source_data(outfn,conf,payload)
			self.log.info('Done')
			#print cnt
			#sys.exit(1)
			#print outfn
			
			#stat=os.stat(outfn).st_size
			#print 'spooled %d B' % stat			
			#sys.exit(0)
			#print shard_name
			
			file_shard=self.fromDb.get_spool_file_shard(shard_name,outfn)
			#print file_shard
			#sys.exit(1)
			#assert not status, 'Spool exited with status "%s"' % status
			if cnt:
				#pprint (payload)
				#first_row=self.fromDb.get_firstrow()
				#conf=self.toDb.get_load_config(payload)
				conf=self.get_load_config(to_pld,file_shard)
				
				#pprint( conf)
				#e(0)
				#sys.exit(0)
				#print payload
				#sys.exit(0)
				shard=payload[0].split('-')[1]
				#print shard
				#(out,status,err,ins_cnt)=self.toDb.load_data(logger,conf,outfn,shard)
				self.log.info('Loading data...')
				(out,status,err,ins_cnt, spool_size)=self.toDb.load_data(logger,conf,outfn,shard)
				#print outfn
				self.log.info('Done')
				#(out,status,err)=self.load_data(logger,conf)
			else:
				self.log.info('bypassing load')
				spool_size=0
				ins_cnt=0
				#e(0)
		else:
			print 'Cannot fetch common columns.'

		#stat=os.stat(outfn).st_size
		#print 'spooled %d B' % stat
		#print self.args.keep_data_file
		if self.args.keep_data_file:
			self.log.info('keeping spool file.')
		else:
			if os.path.isfile(outfn):
				self.remove_file(outfn)
				#os.remove(outfn) 
			self.log.info('spool file deleted.')

		if cnt<0:
			cnt=ins_cnt
		return (spool_size,status,cnt)
		
	

	