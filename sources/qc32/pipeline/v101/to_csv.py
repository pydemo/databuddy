import types, re, os, sys
from subprocess import Popen, PIPE
from db.v101.db_csv import CSV
import codecs, tempfile
from pprint import pprint
e=sys.exit
#import config.common as uconf 
class ToCSV(CSV):
	"""CSV"""
	def __init__(self,parent,log,to_file,datadir, conf):
		self.log=log
		self.to_file=to_file
		#print conf.uargs
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		self.datadir=datadir
		self.tab_cols={}
		self.to_pld={}
		self.out={}
		(self.F, self.D) = (False, False)
		if self.args.to_file:
			#print 1
			assert not self.args.to_dir, 'You cannot set to_file if to_dir is set.'
			assert self.args.num_of_shards<2, 'You cannot export to single file if num_of_shards>1.'
			self.F=True
			
		elif self.args.to_dir:
			#print 2
			assert not self.args.to_file, 'You cannot set to_dir if to_file is set.'
			self.D=True
		else:
			#default
			#print 3
			if 0:
				assert self.args.num_of_shards>0, 'num_of_shards has to be set to a value greater than 0.'
				if self.args.num_of_shards==1:
					self.F=True
					self.args.to_file= self.uargs.to_file
					#print self.args.to_file
				elif self.args.num_of_shards>1:
					self.D=True
					self.args.to_dir= self.uargs.to_dir
		#print self.F, self.D
		#e(0)
		
		#return uconf.to_file
	def print_copy_details(self,outfn=None):
		
		flist=''
		if outfn:
			if self.F:
				flist= '	%s' % 	outfn[0] #self.get_out_fn(0)
			else:
				
				for sid in range(self.args.num_of_shards):
					flist +='	%s\n' % outfn[sid] #self.get_out_fn(sid)
		else:
			if self.F:
				flist= '	%s' % 	self.get_out_fn(0)
			else:
				
				for sid in range(self.args.num_of_shards):
					flist +='	%s\n' % self.get_out_fn(sid)		
		print """		
To CSV:
	%s
""" % flist.strip() #(self.to_file)
	
	def set_payload(self,shard,num_of_shards):
		#options={'_PARTITION':pt}
		
		return (self.to_file) 
	def get_out_fn(self, sid):
		out=(None,None)
		#global args.to_dir is not set
		#print self.D
		if self.F:
			if self.args.to_file:
				out= (0,self.args.to_file)
			else:
				out= (1,self.uargs.to_file)
				
		elif self.D:
			
			outdir=None
			if self.args.to_dir:
				outdir = self.args.to_dir
			else:
				outdir = self.uargs.to_dir
			#assert outdir, 'Cannot create default '
			#print outdir
			#sys.exit(1)
			#if outdir:
			#print 1
			if self.args.num_of_shards>1:
				#print self.uargs.to_file
				(fn,ext) = fileName, fileExtension = os.path.splitext(os.path.basename(self.uargs.to_file)) 
				if hasattr(self.args, 'query_sql_dir') and self.args.query_sql_dir:
					qnames=os.listdir(args.query_sql_dir)
					(qn,_) = fileName, fileExtension = os.path.splitext(qnames[int(sid)])
					out= (2,os.path.join(outdir,'%s_%s%s' % (fn,qn,ext)))
				else:
					out= (3,os.path.join(outdir,'%s.Shard-%s%s' % (fn,sid,ext)))
				#print outdir
				#print outfn
				#print 11
			else:	
				#print outdir
				#print self.args.to_dir
				out= (4,os.path.join(outdir,os.path.basename(self.uargs.to_file)))
				#print 12
		else:
			pass
			#return None
		#pprint (out )
		#sys.exit(1)
		#print out
		#print self.uargs.to_file
		#e(0)
		self.out[sid]=out
		return out[1]
	def get_load_config(self,field_term,first_row,payload,outfn):
		(shard_name,from_pld,to_pld)=payload
		#(login, to_table)=to_pld
		#print payload
		return None		
	def get_inserted_count(self,cnt):
		return cnt
	def load_data(self,logger,loadConf,outfn,shard):
		return (0,0,0,0)
	

	
