import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_csv import CSV
import codecs, tempfile
from pprint import pprint
e=sys.exit
class FromCSV(CSV):
	"""CSV file"""
	def __init__(self,parent,log,input_files,skip_rows,datadir,conf):
		CSV.__init__(self,log, datadir)
		self.log=log
		self.ppl=parent
		self.input_files=[]
		self.input_file_names=[]
		self.num_of_lines={}
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.field_term=args.field_term
		self.skip_rows=skip_rows
		self.shard_size_kb=args.shard_size_kb
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		self.dirs=[]
		self.IF, self.ID =(False,  False)
		if hasattr(args, 'input_files') and args.input_files:
			assert not self.args.input_dirs, 'Set input_dirs or input_files but not both.'
			self.IF=True
			for input_file in args.input_files.split(','):
				os.chdir(self.conf.home)
				input_file=os.path.realpath(input_file)
				self.input_files.append(input_file)
				df = os.path.basename(input_file)
				self.input_file_names.append(df)	
			#print self.input_file
			#e(0)
		else:
			#print self.args.input_dir
			assert self.args.input_dirs, 'input_dir is not set.'
			self.ID=True
			import glob
			#pprint (self.args.input_dirs)
			self.dirs=[d.strip('"') for d in self.args.input_dirs.split(',')]
			#pprint(self.dirs)
			for dir in self.dirs:
				#print dir
				for df in os.listdir(dir):
					#print dir,df
					rp= os.path.realpath(os.path.join(dir, df))
					self.input_files.append(rp)
					self.input_file_names.append(df)	
		#print self.input_file
		#print self.input_file_name
		#pprint(self.input_files)
		#e(0)
		for inf in self.input_files:
			self.log.info('Counting lines in input file...')
			self.num_of_lines[inf]= self.count_lines(inf)
			if self.num_of_lines[inf]==0:
				self.num_of_lines[inf]= self.count_lines(inf)
			self.log.info('Done.')
			self.log.info('Estimated line count: %s' % self.num_of_lines[inf][0])		
		self.chunks =self.get_chunks()
		shards_needed = len(self.chunks)
		if shards_needed>conf.args.num_of_shards:
			self.log.warn('Overriding num_of_shards %s->%s.' % (self.args.num_of_shards, shards_needed))
			conf.args.num_of_shards=shards_needed
		#sys.exit(1)			
	def print_copy_details(self):
		src=''
		if self.IF:
			src = '\t\tinput file(s):\n%s' % '\n'.join(self.input_files)
		else:
			for did in range(len(self.dirs)):
				src = '%s\n\t\tinput dir (%d): %s' % (src,did+1, self.dirs[did])
		print """		
	From CSV:	
%s
		""" % (src)		

	def get_spool_config(self,from_pld):
		
		return self.input_files
	def get_spool_file_shard(self,shard_name,outfn):
		#pprint (self.shards)
		shard_id=int(shard_name.split('-')[1])
		if 1:
			for i in range(len(self.shards)):
				#print i
				#print shards[i]
				(sid,row_from, row_to, _) = self.shards[i]
				if shard_id==i:
					#print row_from, row_to
					return (shard_name,outfn, row_from, row_to)
					#from_pld.append(('Shard-%s' % i,self.input_file, row_from, row_to,self.field_term))
		self.log.warn('Shard id %s not found' % shard_id)
		return (shard_name,outfn, self.get_firstrow(),0)	
	def count_lines_pct(self,fn):
		#fn="u1/apps/smart/inbound/cpi/REFDATA_CPI.PSV"
		#start_time = time.time()

		#import os
		sample=self.args.shard_size_kb
		st = os.stat(fn)
		fsize=st.st_size
		#print fsize,sample


		f = open(fn)                  
		lines = 0
		buf_size = (fsize/100)*sample
		read_f = f.read # loop optimization
		#print "buf_size = ", buf_size
		buf = read_f(buf_size)
		lines = buf.count('\n')
		#print "Lines: %s " % lines
		#print "Lines count estimate: %d" % ((float(lines)/100)*100)
		f.close()
		return int((float(lines)/sample)*101)
	def count_lines(self,fn):
		buf_size=self.args.shard_size_kb*1024
		st = os.stat(fn)
		fsize=st.st_size
		if fsize<buf_size:
			buf_size=fsize
			
		#print fsize,buf_size


		f = open(fn)                  
		lines = 0
		#buf_size = (fsize/100)*sample
		read_f = f.read # loop optimization
		#print "buf_size = ", buf_size
		buf = read_f(buf_size)
		lines = buf.count('\n')
		#print "Lines: %s " % lines
		#print "Lines count estimate: %d" % ((float(lines)/100)*100)
		f.close()
		#print int((float(lines)*(fsize/float(buf_size)))*100)+1
		#print lines,buf_size
		#e(1)
		rc=int((float(lines)*(fsize/float(buf_size))))
		
		
		return (rc,lines)
	def get_firstrow(self):
		#print self.skip_rows
		if self.skip_rows:
			return self.skip_rows+1
		else:
			return 0

	def set_payload(self,num_of_shards,toDb=None):
		print ''
		#print self.QF
		#sys.exit(0)
		self.toDb=toDb

			
		if self.IF:
			return self.set_file_payload(num_of_shards)
		else:
			return self.set_filelist_payload(num_of_shards)
				
	def set_file_payload(self, num_of_shards):
		#print self.conf.args.num_of_shards
		#e(0)
		lame_duck=self.args.lame_duck
		self.shards=[]
		for sh in self.chunks:
			(s,sid,nos,rc,shard_size,ifn) =sh
			#print s,sid,nos,rc,shard_size

			if sid==(nos-1):
				to_row=0
				#print to_row,limit, limit<to_row
				from_row=shard_size*sid
				if sid==0:
					from_row=self.get_firstrow()
				if lame_duck:
					to_row=from_row+lame_duck
				#print from_row,sid	, sid==0				
				self.shards.append([s,from_row,to_row,ifn])
			elif sid==0:
				to_row=shard_size
				#print to_row,limit, limit<to_row
				if lame_duck and lame_duck<to_row:
					to_row=lame_duck
					#print to_row				
				self.shards.append([s,self.get_firstrow(),to_row,ifn])				
			else:
				to_row=shard_size
				#print to_row,limit, limit<to_row
				if lame_duck and lame_duck<to_row:
					to_row=lame_duck	
					#print to_row
				
				self.shards.append([s,shard_size*sid,shard_size*sid+to_row,ifn])
		self.from_pld=[]	
		#pprint(self.shards)
		#e(0)
		#print limit
		#sys.exit(1)
		for i in range(len(self.shards)):
			#print i
			#print shards[i]
			(sid,row_from, row_to, inf) = self.shards[i]
			if 1:
				self.from_pld.append(('Shard-%s' % i,inf, row_from, row_to,self.field_term))

		#pprint( from_pld)
		#print self.skip_rows
		if self.skip_rows:
			self.log.info('Skipping %s first rows.',self.skip_rows)
		#sys.exit(1)
		return (self.shards,self.from_pld) 	
	def get_chunks(self):
		out=[]
		nos=0
		sid=0
		for ifn in self.input_files:
			#print ifn
			rc,rc_per_shard=self.num_of_lines[ifn]
			
			nos =rc/rc_per_shard
			#print rc, rc_per_shard, nos
			for s in range(nos):
				out.append((sid, s,nos,rc,rc_per_shard,ifn))#print nos
				sid +=1
		#print nos
		
		#pprint(out)
		#e(0)
		return out
	def set_filelist_payload(self, num_of_shards):
		#sql_query =''
		#assert os.path.isfile(self.input_file), 'Input CSV file %s is unreadable' % self.input_file

		#inf=self.input_file[0]
		#assert os.path.isfile(inf), 'Input CSV file %s is unreadable' % inf

		#rc=self.num_of_lines[inf]
		#print num_of_rows
		#assert num_of_rows, 'Input file row estimate: %s' % num_of_rows
		#sys.exit(1)
		#assert rc, 'Input line count is 0(zero).'
		
		#shard_size=self.args.shard_size_kb 
		#print 'shard_size',shard_size,num_of_shards

		#assert shard_size>100 or num_of_shards==1, 'num_of_shards (%d) is too high for a given record count (%d)' % (num_of_shards,rc)
		#print shard_size
		#sys.exit(0)
		#nos= self.get_num_of_shards_needed()
		#pprint( nos)
		#num_of_shards=len(nos)
		#e(0)
		#if args.num_of_shards<>len(nos):
			#self.log.warn('Overriding num_of_shards %s->%s.' % (self.args.num_of_shards, len(nos)))
			#self.conf.args.num_of_shards=len(nos)
			
		#print self.conf.args.num_of_shards
		#e(0)
		lame_duck=self.args.lame_duck
		self.shards=[]

		

		for sh in self.chunks:
			(s,sid,nos,rc,shard_size,ifn) =sh
			#print s,sid,nos,rc,shard_size

			if sid==(nos-1):
				to_row=0
				#print to_row,lame_duck, limit<to_row
				from_row=shard_size*sid
				if sid==0:
					from_row=self.get_firstrow()				
				if lame_duck:
					to_row=from_row+lame_duck				
				self.shards.append([s,from_row,to_row,ifn])
			elif sid==0:
				to_row=shard_size
				#print to_row,limit, limit<to_row
				if lame_duck and lame_duck<to_row:
					to_row=lame_duck
					#print to_row				
				self.shards.append([s,self.get_firstrow(),to_row,ifn])				
			else:
				to_row=shard_size
				#print to_row,limit, limit<to_row
				if lame_duck and lame_duck<to_row:
					to_row=lame_duck	
					#print to_row
				
				self.shards.append([s,shard_size*sid,shard_size*sid+to_row,ifn])
		from_pld=[]	
		#pprint(self.shards)
		#print limit
		#e(0)
		for i in range(len(self.shards)):
			#print i
			#print shards[i]
			(sid,row_from, row_to, inf) = self.shards[i]
			if 1:
				from_pld.append(('Shard-%s' % i,inf, row_from, row_to,self.field_term))

		#pprint( from_pld)
		#print self.skip_rows
		if self.skip_rows>1:
			self.log.warn('Skipping CSV file header (%s rows)',self.skip_rows-1)
		
		#print len(self.shards)
		#e(0)
		return (self.shards,from_pld) 	

		
	def get_inserted_count(self,cnt):
		return cnt

	
