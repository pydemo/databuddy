import types, re, os, sys
from subprocess import Popen, PIPE
from base import base 
import codecs, tempfile
#import common.v101.config as conf 
import zipfile
from pprint import pprint
import datetime
import shlex
import imp
import itertools
import __builtin__
import shutil
from tempfile import mkstemp
from shutil import move
from os import remove, close
import datetime
e=sys.exit
email_to='' #'ab95022@imcnam.ssmb.com' #'alex_buz@yahoo.com;alexbuzunov@gmail.com'
abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
log_dir=r'C:\Temp\qc_log'
#job_pre_etl=r'.\Scripts\job\delete_records.py'
shard_pre_etl='' #r'.\Scripts\delete_records.py'
time_stamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
keep_spool_file=1
#wide row support
column_buckets=2
loader_profile=''
with_loader_profile=r'"C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml"'
job_pre_etl='' #r'"C:\Python27\data_migrator_1239\config\etl\job_pre_etl.py"'
DeleteTargetRecs=r'".\etl_templates\Oracle\delete_target_recs\job_pre_etl.py"'
shard_pre_etl='' #r'"C:\Python27\data_migrator_1239\config\etl\shard_pre_etl.py"'
job_post_etl='' #r'"C:\Python27\data_migrator_1239\config\etl\job_post_etl.py"'
shard_post_etl='' #r'"C:\Python27\data_migrator_1239\config\etl\shard_post_etl.py"'
ask_to_truncate=0
#sqlloader_profile
#os.path.join(abspath,'user_log')
#print log_dir
if not os.path.isdir(log_dir):
	os.makedirs(log_dir)
#log_dir=''
job_name='qc_job'
default_spool_dir=  r'C:\tmp\TEST_default_spool'
class common_build(base):
	"""commin build methods."""
	def __init__(self):		
		pass
	def create_exe_tests(self, reg,cmd,exefn):
		out=[]
		#exe_dir=os.path.dirname(exefn)
		
		#print len(cmd)
		#e(0)
		#sys.exit(1)
		assert os.path.isfile(exefn), 'Executable file does not exists at\n %s' % exefn
		#	os.makedirs(test_dir) 
		for i in cmd:
			(db_from, db_to,c,cmt) = i
			#print i
			#sys.exit(1)
			paramkey_from=db_from.split('_')[0]
			paramkey_to=db_to.split('_')[0]
			from_to='%s_to_%s' % (self.conf.dbs[paramkey_from].replace(' ','').replace('*',''), self.conf.dbs[paramkey_to].replace(' ','').replace('*',''))
			test_dir =os.path.join(os.path.dirname(exefn),'tests',from_to)
			#print exe_dir
			if not os.path.isdir(test_dir):
				os.makedirs(test_dir)		
			#print paramkey_from
			action ='Copy'
			if paramkey_to.upper() in self.conf.ff:
				action ='Extract'
			if paramkey_from.upper() in self.conf.ff:
				action ='Load'
			from_dbname=self.conf.dbs[paramkey_from.upper()].replace(' ','')
			to_dbname=self.conf.dbs[paramkey_to.upper()].replace(' ','')
			title= '%s_%s' % (from_dbname,' '.join(db_from.split('_')[1:]))
			src='table'
			trg='table'
			if  from_dbname in ['CSV']:
				src='file'
			if db_to.startswith('CSV'):
				trg= 'location'
			#if db_to.endswith('Dir'):
			#	trg= 'dir'			
				#trg= 'file'
			elif 'Partition' in db_from:
				src='partition'
				if 'Sharded' in db_from:
					src='sharded partition'
			elif 'Subpartition' in db_from:
				src='sub-partition'
				if 'Sharded' in db_from:
					src='sharded sub-partition'	
			elif 'Query' in db_from:
				src='query results'
			print db_from
			print src
			#e(0)
			dir =''
			if 'Dir' in db_from:
				dir="""Read each CSV file from a directory "%s".""" % self.get_param(c, '-I')
			if 'QueryDir' in db_from:
				dir="""Read each SQL query file from a directory "%s".""" % self.get_param(c, '-Q')
			if 'QueryFile' in db_from:
				dir="""Read SQL from a query file "%s".""" % self.get_param(c, '-q')  
			skip=action
			sharded=''
			#pprint(c)
			#e(0)
			nos=self.get_param(c,'-r')
			ps =self.get_param(c,'-o')
			if 'ShardedFile' in db_from:
				sharded = """Break input CSV file into %s logical partitions (-r[--num_of_shards] %s) 
	::				and run loader process on each shard in thread pool (-o[--pool_size] %s).
	::				""" % (nos,nos,ps)
			if 'ShardedDir' in db_from:
				sharded = """Break input CSV files into logical partitions (shards) and run loader 
	::				process on each shard in thread pool (-o[--pool_size] %s)
	::				""" % (ps)

			if 'Skip' in db_from:
				skip = 'Skip %s rows and %s' % (db_from.split('Skip')[1],action.lower()) 
			if 'Limit' in db_from:
				skip = '%s only %s rows from' % (skip, db_from.split('Limit')[1]) 
			descr ="%s %s %s into %s%s." % (skip, from_dbname,src,to_dbname,' '.join(db_to.split('_')[1:]))
			fname=("%s %s_%s into %s%s" % (action,from_dbname,' '.join(db_from.split('_')[1:]),to_dbname,' '.join(db_to.split('_')[1:]))).replace(' ','_')
			#print title
			#print fname
			scr=r'%s\%s.bat' % (test_dir,fname)
			print ''
			print scr
			f=open( scr,'w')
			cmt='\n::	'.join(cmt)
			header="""::Test name: %s
	::Description:	%s%s%s
	::Arguments:
	::	%s	
	"""	 %  (title,dir,sharded,descr,cmt)
			f.write('%s\n%s' % (header,c))
			f.close()
			out.append((db_from,db_to,scr))
		return out	
	def build_test_dbs2(self, relc, tests,cmd):
		global conf
		i=len(cmd)
		all=[]
		print tests.keys()
		#e(0)
		args_api={}
		for t in tests:
			if not args_api.has_key(t):
				args_api[t]=[]
			
			print t
			#t_from,t_to= t
			#print t_from,t_to
			for element in tests[t]:
				
				print ''
				(db_from, db_to) = element
				
				#print (db_from, db_to)
				#e(0)
				if ('CSV_Sharded' in db_from and db_to in ('SYIQ', 'SYANY', 'SYASE', 'INFORC','INFOR','SLITE','TTEN','MARIA','MYSQL','INFOB','PGRES','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE' )):
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
				elif db_from.startswith('CSV')  and db_to.startswith('CSV') :
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
				elif db_from.endswith('Dir')  and db_to.endswith('File') :
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)			
				elif db_from.startswith('SSEXP')  and db_from.lower().endswith('partition') :
					print 'SQL Server Express does not support partitions'	
				#elif 'Limit' in db_from and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
				#	print  '%s does not support limit' % conf.dbs[db_to.upper()]
				elif ('CSV' in db_from and 'Limit' in db_from ) and db_to.upper() in ['MYSQL', 'INFOB', 'MARIA','SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
					print  '%s does not support limit' % conf.dbs[db_to.upper()]			
				elif 'Skip' in db_from and db_to.upper() in ['INFORC','INFOR','SLITE','TTEN','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE']:				
					print  '%s does not support "skip header row"' % conf.dbs[db_to.upper()]
				elif  'KeepSpoolFile' in db_from and db_to.startswith('CSV'):
					print  'Extractor does not support "KeepSpoolFile"'
				elif  'Header' in db_from and (not db_to.startswith('CSV')):
					print  'Header tests are CSV bound.'					
				else:
					if db_to.startswith('ORA'):
						loader_profile=with_loader_profile
					else:
						loader_profile=''
						
					paramkey_from=db_from.split('_')[0]
					paramkey_to=db_to.split('_')[0]

					if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
						i +=1
						if 1:
							b=['%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,keep_spool_file,0,0,ask_to_truncate,0,email_to,log_dir,'',job_name,time_stamp,'',job_pre_etl,'','','',loader_profile,'','','']
							
							if 'Sharded' in db_from or 'Parallel' in  db_from:
								if db_to in ('CSV_File'):
									print 'skipping test %s to %s"' % (db_from,db_to) 
									continue
								b[1]=b[2]=3
							if 'Limit' in db_from:
								limit=int(db_from.split('Limit')[1])
								b[4]=limit
							if 'KeepSpoolFile' in db_from:
								b[5]=1
							if 'Validate' in db_from or 'Validate' in db_to:
								b[6]=1	
							if 'TruncateTarget' in db_from or 'TruncateTarget' in db_to:
								b[7]=1
								b[8]=1
							if 'AskToTruncate' in db_from or 'AskToTruncate' in db_to:
								b[8]=1	
							if 'Email' in db_from or 'Email' in db_to:
								b[10]=email_to
							if 'JobName' in db_from or 'JobName' in db_to:
								b[13]='FROM_%s_TO_%s' % (db_from, db_to)	
							if not paramkey_from.upper().startswith('CSV'): 
								#setting default_spool_dir
								b[12]=default_spool_dir
							#if 'QueryDir' in db_from:
							#	b[15]=job_pre_etl
							if 'WithWideRows' in db_from:
								b[15]=column_buckets
							if 'DeleteTargetRecs' in db_to:
								b[16]=DeleteTargetRecs

								
							if 'WithLoaderProfile' in db_to:
								b[20]=with_loader_profile
								
							self.test['core']=b
							
						
							
						self.create_run_tests(db_from, db_to,  self.test, self.citi)
						(comment,command,(from_to,api,default_api))=self.run_test(db_from, db_to, self.prog, self.test,  citi=self.citi)
						#print db_from, db_to
						#print comment,command
						#print api,default_api
						if not args_api[t]:
							args_api[t]={'default':default_api}
						else:
							args_api[t]['.'.join(from_to)]=api
						#args_api[t].append(api)
						#e(0)
						test_key='%s:%s' % (db_from, db_to)
						if test_key in all:
							pass
						else:
							cmd.append ((db_from, db_to,command,comment))
							all.append(test_key)
			home=os.path.dirname(os.path.realpath(__file__))
			source,target=t.split('->')
			pprint (args_api.keys())
			for k,v in args_api.items():
				print k
				#pprint(v.keys())
			api_dirname= os.path.join(home,'args_api')
			
			
			
			py_name='%s-%s.py' % (source,target)
			dirname= os.path.join(api_dirname,source)
			fname= os.path.join(dirname,py_name)
			if not os.path.isdir(api_dirname):
				os.makedirs(api_dirname)
				f=open(os.path.join(dirname,'__init__.py'),'w')
				f.write('# Dummy file to make this directory a package.	')
				f.close()
				
			if not os.path.isdir(dirname):
				os.makedirs(dirname)
			f=open( fname,'w')
			f.write('#do not change\naa=%s' % str(args_api[t]))
			f.close()
			api_todir=os.path.join(r'C:\Users\alex_buz\Documents\GitHub\DataBuddy','args_api',source)
			if not os.path.isdir(api_todir):
				os.makedirs(api_todir)
			api_tofile= os.path.join(api_todir, py_name)
			if os.path.isfile(api_tofile):
				print 'api file exists'
				os.remove(api_tofile)
			shutil.copyfile(fname,api_tofile)
		
		#e(0)
						
	def build_test_dbs(self, relc, tests,cmd):
		global conf
		i=len(cmd)
		all=[]
		#rint tests
		#e(0)
		for t in tests:
			t_from,t_to= t
			#print t_from,t_to
			for element in itertools.product(t_from,t_to):
				print ''
				(db_from, db_to) = element
				
				#print (db_from, db_to)
				#e(0)
				if ('CSV_Sharded' in db_from and db_to in ('SYIQ', 'SYANY', 'SYASE', 'INFORC','INFOR','SLITE','TTEN','MARIA','MYSQL','INFOB','PGRES','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE' )):
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
				elif db_from.startswith('CSV')  and db_to.startswith('CSV') :
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
				elif db_from.endswith('Dir')  and db_to.endswith('File') :
					print 'Sharded load from %s to %s is not supported' % (db_from, db_to)			
				elif db_from.startswith('SSEXP')  and db_from.lower().endswith('partition') :
					print 'SQL Server Express does not support partitions'	
				#elif 'Limit' in db_from and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
				#	print  '%s does not support limit' % conf.dbs[db_to.upper()]
				elif ('CSV' in db_from and 'Limit' in db_from ) and db_to.upper() in ['MYSQL', 'INFOB', 'MARIA','SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
					print  '%s does not support limit' % conf.dbs[db_to.upper()]			
				elif 'Skip' in db_from and db_to.upper() in ['INFORC','INFOR','SLITE','TTEN','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE']:				
					print  '%s does not support "skip header row"' % conf.dbs[db_to.upper()]
				elif  'KeepSpoolFile' in db_from and db_to.startswith('CSV'):
					print  'Extractor does not support "KeepSpoolFile"'
				else:
					if db_to.startswith('ORA'):
						loader_profile=with_loader_profile
					else:
						loader_profile=''				
					paramkey_from=db_from.split('_')[0]
					paramkey_to=db_to.split('_')[0]
					if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
						i +=1
						if 1:
							b=['%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,keep_spool_file,0,0,ask_to_truncate,0,email_to,log_dir,'',job_name,time_stamp,'',job_pre_etl,'','','',loader_profile,'','','']
							if 'Sharded' in db_from or 'Parallel' in  db_from:
								if db_to in ('CSV_File'):
									print 'skipping test %s to %s"' % (db_from,db_to) 
									continue
								b[1]=b[2]=3
							if 'Limit' in db_from:
								limit=int(db_from.split('Limit')[1])
								b[4]=limit
							if 'KeepSpoolFile' in db_from:
								b[5]=1
							if 'Validate' in db_from or 'Validate' in db_to:
								b[6]=1	
							if 'TruncateTarget' in db_from or 'TruncateTarget' in db_to:
								b[7]=1
							if 'AskToTruncate' in db_from or 'AskToTruncate' in db_to:
								b[8]=1
							if 'Email' in db_from or 'Email' in db_to:
								b[10]=email_to							
							if 'JobName' in db_from or 'JobName' in db_to:
								b[13]='FROM_%s_TO_%s' % (db_from, db_to)
							if not paramkey_from.upper().startswith('CSV'): 
								#setting default_spool_dir
								b[12]=default_spool_dir	
							#if 'QueryDir' in db_from:
							#	b[15]=job_pre_etl
							if 'WithWideRows' in db_from:
								b[15]=column_buckets
							if 'DeleteTargetRecs' in db_to:
								b[16]=DeleteTargetRecs								
							if 'WithLoaderProfile' in db_to:
								b[20]=with_loader_profile								
							self.test['core']=b
							
	
						self.create_run_tests(db_from, db_to,  self.test, self.citi)
						(comment,command,(from_to,api,default_api))=self.run_test(db_from, db_to, self.prog, self.test,  citi=self.citi)
						#print db_from, db_to
						#e(0)
						test_key='%s:%s' % (db_from, db_to)
						if test_key in all:
							pass
						else:
							cmd.append ((db_from, db_to,command,comment))
							all.append(test_key)
						#print i
	def set_tests_dbs2(self, relc, cmd, tests):
		ucases={}
		self.build_test_dbs2(relc, tests,cmd)
		for c in cmd:
			#print c
			t_from, t_to, _,_ = c
			(paramkey_from,paramkey_to,title,(dir,sharded,descr), header)=self.get_use_case(relc,c)
			from_to='%s_to_%s' % (self.conf.dbs[paramkey_from].replace(' ','').replace('*',''), self.conf.dbs[paramkey_to].replace(' ','').replace('*',''))
			uckey='%s_to_%s' % (t_from, t_to)
			if not ucases.has_key(from_to):
				ucases[from_to]={}
			ucases[from_to][uckey] = (paramkey_from,paramkey_to,(dir,sharded,descr), header.replace('198Morgan','test_pwd'))
		#pprint (ucases)
		#e(0)
		scr=r'all_tests.bat'
		f=open( scr,'w')
		for i in cmd:
			(db_from, db_to,c, cmt) = i
			cmt='\n::	'.join(cmt)
			header="""
	::Test vector: From %s to %s
	::	Arguments:
	::		%s	
	"""	 % (db_from, db_to, cmt)	

			f.write('%s\n%s' % (header,c))
		f.close()	
		return ucases					
	def set_tests_dbs(self, relc, cmd, tests):
		ucases={}
		self.build_test_dbs(relc, tests,cmd)
		for c in cmd:
			#print c
			t_from, t_to, _,_ = c
			(paramkey_from,paramkey_to,title,(dir,sharded,descr), header)=self.get_use_case(relc,c)
			from_to='%s_to_%s' % (self.conf.dbs[paramkey_from].replace(' ','').replace('*',''), self.conf.dbs[paramkey_to].replace(' ','').replace('*',''))
			uckey='%s_to_%s' % (t_from, t_to)
			if not ucases.has_key(from_to):
				ucases[from_to]={}
			ucases[from_to][uckey] = (paramkey_from,paramkey_to,(dir,sharded,descr), header.replace('198Morgan','test_pwd'))
		#pprint (ucases)
		#e(0)
		scr=r'all_tests.bat'
		f=open( scr,'w')
		for i in cmd:
			(db_from, db_to,c, cmt) = i
			cmt='\n::	'.join(cmt)
			header="""
	::Test vector: From %s to %s
	::	Arguments:
	::		%s	
	"""	 % (db_from, db_to, cmt)	

			f.write('%s\n%s' % (header,c))
		f.close()	
		return ucases
	def release_ucon(self,relc,exefn):
		#ucon_dir
		reldir=os.path.dirname(exefn)
		ucon_to_dir=os.path.join(reldir,'config')
		ucon_home=os.path.join(self.dmhome,'config')
		shutil.copytree(ucon_home,ucon_to_dir)
		#sys.exit(1)	
	def release_exe(self,relc,exefn,ucases):
		pypath=(os.sep).join(self.dmhome.split(os.sep)[:-1])	
		exedir = os.path.dirname(exefn)
		rel_appn = self.rel.getExeTitle()
		rel_dir = self.rel.getAppTitle().replace(' ','-').replace('*','-')
		
		if os.path.isfile(exefn):

			self.save_txt(exefn,['-h'],'HELP')
			self.save_txt(exefn,['-h','FEAT'],'FEATURES')
			self.save_txt(exefn,['-h','USE'],'USECASES')
			(hdr,code) =self.get_txt(exefn,['-h','ALL'],'README')
			print hdr
			i=1
			#
			bout='\n--DETAILS--'
			out1=''
			print len(ucases)
			uck=ucases.keys()
			for u in sorted(uck):
				out1='%s%d. %s. %s use cases.\n' % (out1,i,u, len(ucases[u]))
				i +=1
			i=1
			out=''
			for from_to in sorted(uck):
				print from_to
				out =  '%s\n%s: %d use case(s) available:\n' % (out, from_to,len(ucases[from_to]))
				pprint (ucases[from_to].keys())
				for uc in sorted(ucases[from_to].keys()):
				
					(paramkey_from,paramkey_to,(dir,sharded,descr), ucbody) = ucases[from_to][uc]
					#from_to='%s_to_%s' % (conf.dbs[paramkey_from].replace(' ','').replace('*',''), conf.dbs[paramkey_to].replace(' ','').replace('*',''))
					ucdir =os.path.join(exedir,'usecases',from_to)
					print ucdir
					if not os.path.isdir(ucdir):
						#print ucdir
						#e(0)
						os.makedirs(ucdir)
					out= out+ ('\n%d. %s - %s%s%s' %(i, uc,dir,sharded,descr)).replace('::','')
					bout = bout+ '\n\n-USE-CASE # %d\n' % i + ucbody
					#print ucbody
					i +=1
					self.fsave(os.path.join(ucdir,'%s.txt' % uc),ucbody)
				print out
			#print 'code'
			#print code
			#e(0)
			
			self.fsave(os.path.join(exedir,'%s.txt' % 'README'),'%s\n%s\n--USE CASES--\n\n%s\n%s\n%s' % (hdr,code,out1,out,bout))
			#e(0)
			self.save_txt(exefn,['-h','ABOUT'],'ABOUT')
			#compress usecases
			
			#ex_name='%sbit_tests' % (relc[0])
			#uzipn= os.path.join(exedir,'%s.zip' % ex_name)
			#print uzipn
			#zipfrom=  get_test_dir(get_dir_from_ts(rts),relc[0]) #os.path.join(dmhome,'example%s' % relc[0])
			#zip_dir(uzipn,zipfrom )
			
			#sys.exit(1)
			print 'compile ok'
			#compress
			sfzipdir=os.path.join(pypath,'Release','SourceForge',rel_dir)
			if not os.path.isdir(sfzipdir):
				os.makedirs(sfzipdir)		

			zipn= os.path.join(sfzipdir,'%s.zip' % rel_appn.replace(' ','-').replace('*','-'))
			print zipn
			distpath = self.get_distpath(relc[0])
			print distpath
			#e(0)
			self.zip_dir(zipn,distpath )
			ghzipdir=os.path.join(pypath,'Release','GitHub',rel_dir)
			if not os.path.isdir(ghzipdir):
				os.makedirs(ghzipdir)
			zfile = zipfile.ZipFile(zipn)
			zfile.extractall(ghzipdir)
			#copy README
			appn=self.get_appn(relc)
			readme_from=os.path.join(ghzipdir,appn,'README.txt')
			readme_to=os.path.join(sfzipdir,'README.txt')
			assert os.path.isfile(readme_from), 'READE.txt does not exists at\n %s' % readme_from
			shutil.copyfile(readme_from,readme_to)
			shutil.copyfile(readme_from,os.path.join(ghzipdir,'README.txt'))


			
		else:
			print 'no exe'	
	def replace(self,file_path, pattern, subst):
		#Create temp file
		fh, abs_path = mkstemp()
		new_file = open(abs_path,'w')
		old_file = open(file_path)
		for line in old_file:
			new_file.write(line.replace(pattern, subst))
		#close temp file
		new_file.close()
		close(fh)
		old_file.close()
		#Remove original file
		remove(file_path)
		
		#Move new file
		shutil.copyfile(abs_path, file_path)	
	def run_all_exe_tests(self,cmd,exefn):
		for c in cmd:
			#print c
			#e(0)
			out=[]
			t_from, t_to, command = c
			
			paramkey_from=t_from.split('_')[0]
			paramkey_to=t_to.split('_')[0]	
			#print paramkey_from, paramkey_to		
			#e(0)		
			#print command
			#sys.exit(1)
			#print command
			#e(0)
			tname='%s.txt' % os.path.splitext(os.path.basename(command))[0]
			#print tname
			#from_to ='%s_to_%s' % (conf.dbs[paramkey_from].replace(' ','').replace('*',''), conf.dbs[paramkey_to].replace(' ','').replace('*',''))
			tldir=os.path.join(os.path.dirname(command),'test_log')
			if not os.path.isdir(tldir):
				os.makedirs(tldir)
			tlfile=os.path.join(tldir,tname)
			assert not os.path.isfile (tlfile), 'Test log already exists.\n%s' % tlfile
			#print tlfile
			#print 'Exists?' ,os.path.isfile (tlfile)
			print '-'*80
			#print os.path.dirname(exefn)
			#os.environ['PATH'] = '%s;%s' % (os.environ['PATH'],os.path.dirname(os.path.dirname(exefn)))
			pprint( command)
			#e(0)
			p = Popen([command],  stdout=PIPE, stderr=PIPE) # '-S',  stdin=p1.stdout,
			out, err = p.communicate()	
			print out
			#print err
			#e(0)
			#print err
			if err:
				#print out
				print err		
			status=p.wait()
			
			#print status
			#e(0)
			#sys.exit(1)
			#out, err = p.communicate()	
			#tlog='\n'.join(out)
			#pprint(tlog)
			out=out.replace('\r\n','\n')
			if err:
				err=err.replace('\r\n','\n')
			#pprint (out)
			#print tlfile
			f=open( tlfile,'w')
			f.write(out)
			f.write(err)
			f.close()
			#print command
			#self.replace(command, '198Morgan', 'test_pwd')
			#sys.exit(1)
			#break
			#c:\Python27\data_migrator_1239>echo y  | c:\Python27\qc_dist_32\20141222_171742\qc32\qc32.exe -w ora2csv -o 1 -r 1 -t "|" -l 10 -Q c:\Python27\data_migrator_1239\test\v101\query\query_dir_ora -f SCOTT/tiger2@orcl -e "YYYY/MM/DD" -m "YYYY-MM-DD-HH24.MI.SS.FF" -O "YYYY-MM-DD-HH24:MI:SS.FF" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -g c:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryDir_Limit10.data			

	def create_tests(self, reg,cmd):
		out=[]
		test_dir = self.get_test_dir(reg)
		#print test_dir
		#sys.exit(1)
		if not os.path.isdir(test_dir):
			os.makedirs(test_dir) 
		for i in cmd:
			(db_from, db_to,c,cmt) = i
			#print i
			#sys.exit(1)
			paramkey_from=db_from.split('_')[0]
			paramkey_to=db_to.split('_')[0]
			#print paramkey_from
			action ='Copy'
			if paramkey_to.upper() in self.conf.ff:
				action ='Extract'
			if paramkey_from.upper() in self.conf.ff:
				action ='Load'
			from_dbname=self.conf.dbs[paramkey_from.upper()].replace(' ','')
			to_dbname=self.conf.dbs[paramkey_to.upper()].replace(' ','')
			
			title ="%s %s_%s data to %s%s" % (action,from_dbname,' '.join(db_from.split('_')[1:]),to_dbname,' '.join(db_to.split('_')[1:]))
			fname=title.replace(' ','_')
			#print title
			#print fname
			scr=r'%s\%s.bat' % (test_dir,fname)
			print ''
			print scr
			cmt='\n::	'.join(cmt)
			header="""
	::Test: %s
	::Arguments:
	::		%s	
	"""	 %  (title,cmt)
			f=open( scr,'w')
			f.write('%s%s' % (header,c))
			f.close()
			out.append((db_from,db_to,scr))
			print '%s%s' % (header,c)
			
		return out
	
	def	get_use_case(self,relc,cmd):		
			(db_from, db_to,c,cmt) = cmd
			(reg, v, ts) =relc
			#print cmd
			#e(0)
			#rts=self.get_dir_from_ts(ts)
			test_dir = self.get_test_dir(reg)
			#print i
			#sys.exit(1)
			paramkey_from=db_from.split('_')[0]
			paramkey_to=db_to.split('_')[0]
			#print paramkey_from
			action ='Copy'
			if paramkey_to.upper() in self.conf.ff:
				action ='Extract'
			if paramkey_from.upper() in self.conf.ff:
				action ='Load'
			from_dbname=self.conf.dbs[paramkey_from.upper()].replace(' ','')
			to_dbname=self.conf.dbs[paramkey_to.upper()].replace(' ','')
			title= '%s_to_%s' % (db_from,db_to) #'_'.join(db_from.split('_')[1:]))
			src='table'
			trg='table'
			if  from_dbname in ['CSV']:
				src='file'
			if db_to.startswith('CSV'):
				trg= 'location'
			#if db_to.endswith('Dir'):
			#	trg= 'dir'			
				#trg= 'file'
			if 'Partition' in db_from:
				src='partition'
				if 'Sharded' in db_from:
					src='sharded partition'
			elif 'Subpartition' in db_from:
				src='sub-partition'
				if 'Sharded' in db_from:
					src='sharded sub-partition'	
			elif 'Query' in db_from:
				src='query results'
			print db_from
			print src
			#e(0)
			dir =''
			if 'Dir' in db_from:
				dir="""Read each CSV file from a directory "%s".
	  """ % self.get_param(c, '-I')
			if 'QueryDir' in db_from:
				dir="""Read each SQL query file from a directory "%s".
	  """ % self.get_param(c, '-Q')
			if 'QueryFile' in db_from:
				dir="""Read SQL from a query file "%s".
	  """ % self.get_param(c, '-q')  
			skip=action
			sharded=''
			#pprint(c)
			#e(0)
			nos=self.get_param(c,'-r')
			ps =self.get_param(c,'-o')
			proc='copy'
			if 'CSV' in db_to:
				proc='extract'
			elif 'CSV' in db_from:
				proc='load'
			if 'Sharded' in db_from:
				sharded = """Break input %s into %s logical shards (-r[--num_of_shards] %s) 
	  and run %s process on each shard in thread pool (-o[--pool_size] %s).
	  """ % (src, nos,nos,proc,ps)
	 
			if 'ShardedFile' in db_from:
				sharded = """Break input CSV file into %s logical partitions (-r[--num_of_shards] %s) 
	  and run %s process on each shard in thread pool (-o[--pool_size] %s).
	  """ % (nos,nos,proc,ps)
			if 'ShardedDir' in db_from:
				sharded = """Break input CSV files into logical partitions (shards) and run %s 
	  process on each shard in thread pool (-o[--pool_size] %s)
	  """ % (proc,ps)

			if 'Skip' in db_from:
				skip = 'Skip %s rows and %s' % (db_from.split('Skip')[1],action.lower()) 
			if 'Limit' in db_from:
				skip = '%s only %s rows from' % (skip, db_from.split('Limit')[1]) 
			descr ="%s %s %s into %s %s %s." % (skip, from_dbname,src,to_dbname,' '.join(db_to.split('_')[1:]), trg)
			print db_from
			print db_to
			print descr
			#e(0)
			fname=("%s %s_%s into %s%s" % (action,from_dbname,' '.join(db_from.split('_')[1:]),to_dbname,' '.join(db_to.split('_')[1:]))).replace(' ','_')
			#print title
			#print fname
			scr=r'%s\%s.bat' % (test_dir,fname)
			#print ''
			#print scr
			#f=open( scr,'w')
			cmt='\n  '.join(cmt)
			#print repr(os.linesep)
			#pprint (c.split(os.linesep))
			#e(0)
			header="""Use case name: %s
Description:  %s%s%s
Arguments:
  %s	
Example: 
  %s"""	 %  (title,dir,sharded,descr,cmt, '\n  '.join(c.split("""\n""")))
			return (paramkey_from,paramkey_to, title,(dir,sharded,descr), header)				
	def set_tests(self, relc, cmd, to_test, from_t):
		ucases={}
		
		assert to_test, 'to_test is not set'
		t_to=to_test #conf.to_filter #['ORAXE'] #['CSV_Default', 'CSV_Dir','CSV_File']
		self.build_test(relc, from_t,to_test,cmd)
		assert cmd, 'cmd is not set for %s->%s' % (from_t,to_test)
		for c in cmd:
			#print c
			t_from, t_to, _,_ = c
			(paramkey_from,paramkey_to,title,(dir,sharded,descr), header)=self.get_use_case(relc,c)
			from_to='%s_to_%s' % (self.conf.dbs[paramkey_from].replace(' ','').replace('*',''), self.conf.dbs[paramkey_to].replace(' ','').replace('*',''))
			uckey='%s_to_%s' % (t_from, t_to)
			if not ucases.has_key(from_to):
				ucases[from_to]={}
			ucases[from_to][uckey] = (paramkey_from,paramkey_to,(dir,sharded,descr), header.replace('198Morgan','test_pwd'))
		#pprint (ucases)
		#e(0)
		scr=r'all_tests.bat'
		f=open( scr,'w')
		for i in cmd:
			(db_from, db_to,c, cmt) = i
			cmt='\n::	'.join(cmt)
			header="""
::Test vector: From %s to %s
::	Arguments:
::		%s	
"""	 % (db_from, db_to, cmt)	
		#print cmd
		#e(0)
		f.write('%s\n%s' % (header,c))
		f.close()	
		return ucases
	def build_exe (self, appn,src,distpath,relc):
		if os.path.isfile(src):
			(bin,version, ts) = relc 
			#compile
			#distpath = r'C:\Python27\dist1'
			

			
			
		
			pyloc={ '32':'C:\Python278',
					'64':'C:\Python27'}
			pyinst= os.path.join(pyloc[bin], r'Scripts\pyinstaller.exe')
			#print pyinst
			#sys.exit(1)
			cmd = r'%s -y %s -n %s -p %s --distpath %s --log-level DEBUG' % (pyinst, src,appn,self.dmhome,distpath)
			#print cmd
			cmd=cmd.replace('\\','\\\\')
			#cmd=r'C:\\Python278\\Scripts\\pyinstaller.exe -y C:\\Python27\\csvextractor_1235\\csvextractor.py --log-level DEBUG'
			#print cmd

			shcmd = shlex.split(cmd)
			#pprint(shcmd)


			self.exec_cmd(shcmd)

			#print distpath
			exe = self.get_exe_name(relc) #os.path.join(distpath,appn,'%s.%s' % (appn,conf.appex))
			#print exe
			return exe
		
	def build_project(self, relc):	
		(bin,version, ts) = relc 

		#global conf
		#conf=None
		#import __builtin__
		__builtin__.copy_vector = None
		#import common.v101.config as conf 
		self.conf.rel = reload(self.conf.rel)
		
			
		#print conf.appname
		#appn, appex = os.path.splitext(conf.appname)
		#appn='%s%s' % (appn,bin)
		assert self.conf.appn and self.conf.appex, 'App name ora app ext are not set [%s, %s]' % (self.conf.appn, self.conf.appex)
		dm=os.path.join(self.dmhome, 'datamule.py')
		if 0:
			scr_to= '%s.py' % self.conf.appn
			#print scr_to
			#backup if exists
			src_to_loc = os.path.join(self.dmhome, scr_to)
			if os.path.isfile(src_to_loc):
				print 'backing up %s' % scr_to
				bkp = os.path.join(self.dmhome,'release_backup',('%s_%s_%s_%s' % ((scr_to,)+relc)))
				#print bkp
				os.rename( src_to_loc,bkp)
			
			#os.copy(dm, src_to_loc)
			#import shutil
			shutil.copyfile(dm, src_to_loc)
		if 1:
			scr_to= 'datamule.py' 
			#print scr_to
			#backup if exists
			src_to_loc = os.path.join(self.dmhome, scr_to)
			if os.path.isfile(src_to_loc):
				print 'backing up %s' % scr_to
				bkp = os.path.join(self.dmhome,'release_backup',('%s_%s_%s_%s' % ((scr_to,)+relc)).replace('/','').replace(' ','').replace(':',''))
				#print bkp
				
				shutil.copyfile(src_to_loc,bkp)

				#os.rename( src_to_loc,bkp)
			else:
				#print src_to_loc
				print 'no file'
			#os.copy(dm, src_to_loc)
			#import shutil
			#shutil.copyfile(dm, src_to_loc)
			#py_ho

		#print src_to_loc
		#sys.exit(1)
		distpath=self.get_distpath(relc[0])
		#print distpath
		#appn='%s%s.%s' % (conf.appn,relc[0],conf.appex)
		appn=self.get_appn(relc)
		exefn=self.build_exe(appn,dm,distpath,relc)
		return exefn
		#sys.exit(1)

		release(relc,exefn)
	
	def build_test(self, relc, t_from,t_to,cmd):
		#global conf
		i=len(cmd)
		#print t_from
		#print t_to
		#e(0)
		for element in itertools.product(t_from,t_to):
			print ''
			(db_from, db_to) = element
			#print (db_from, db_to)
			#sys.exit(0)
			if ('CSV_Sharded' in db_from and db_to in ('SYIQ', 'SYANY', 'SYASE', 'INFORC','INFOR','SLITE','TTEN','MARIA','MYSQL','INFOB','PGRES','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE' )):
				print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
			elif db_from.startswith('CSV')  and db_to.startswith('CSV') :
				print 'Sharded load from %s to %s is not supported' % (db_from, db_to)
			elif db_from.endswith('Dir')  and db_to.endswith('File') :
				print 'Sharded load from %s to %s is not supported' % (db_from, db_to)			
			elif db_from.startswith('SSEXP')  and db_from.lower().endswith('partition') :
				print 'SQL Server Express does not support partitions'	
			elif ('CSV' in db_from and 'Limit' in db_from ) and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
				print  '%s does not support limit' % self.conf.dbs[db_to.upper()]			
			elif 'Skip' in db_from and db_to.upper() in ['INFORC','INFOR','SLITE','TTEN','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE']:				
				print  '%s does not support "skip header row"' % self.conf.dbs[db_to.upper()]
			elif  'KeepSpoolFile' in db_from and db_to.startswith('CSV'):
				print  'Extractor does not support "KeepSpoolFile"'
			else:
				if db_to.startswith('ORA'):
					loader_profile=with_loader_profile
				else:
					loader_profile=''
				paramkey_from=db_from.split('_')[0]
				paramkey_to=db_to.split('_')[0]
				if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
					i +=1
					if 1:
						b=['%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,keep_spool_file,0,0,ask_to_truncate,0,email_to, log_dir,'',job_name,time_stamp,'',job_pre_etl,'','','',loader_profile,'','','']
						if 'Sharded' in db_from or 'Parallel' in  db_from:
							if db_to in ('CSV_File'):
								print 'skipping test %s to %s"' % (db_from,db_to) 
								continue
							b[1]=b[2]=3
						if 'Limit' in db_from:
							limit=int(db_from.split('Limit')[1])
							b[4]=limit
						if 'KeepSpoolFile' in db_from:
							b[5]=1
						if 'Validate' in db_from or 'Validate' in db_to:
							b[6]=1	
						if 'TruncateTarget' in db_from or 'TruncateTarget' in db_to:
							b[7]=1
						if 'AskToTruncate' in db_from or 'AskToTruncate' in db_to:
							b[8]=1	
						if 'Email' in db_from or 'Email' in db_to:
							b[10]=email_to	
						if 'JobName' in db_from or 'JobName' in db_to:
							b[13]='FROM_%s_TO_%s' % (db_from, db_to)	
						if not paramkey_from.upper().startswith('CSV'): 
							#setting default_spool_dir
							b[12]=default_spool_dir	
						#if 'QueryDir' in db_from:
						#	b[15]=job_pre_etl
						if 'WithWideRows' in db_from:
							b[15]=column_buckets	
						if 'DeleteTargetRecs' in db_to:
							b[16]=DeleteTargetRecs							
						if 'WithLoaderProfile' in db_to:
							b[20]=with_loader_profile							
						self.test['core']=b
						#pprint (b)
						#print 'AskToTruncate' in db_from or 'AskToTruncate' in db_to
					#print db_from, db_to
					#prog=[get_exe_name(relc)]
					#print exe
					#e(0)
					self.create_run_tests(db_from, db_to,  self.test, self.citi)
					(comment,command,(from_to,api,default_api))=self.run_test(db_from, db_to, self.prog, self.test, citi=self.citi)
					cmd.append ((db_from, db_to,command,comment))