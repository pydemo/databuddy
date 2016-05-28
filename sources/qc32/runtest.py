import sys, os
import shlex
from pprint import pprint
from subprocess import Popen, PIPE
import datetime
import __builtin__
__builtin__.copy_vector = None
#import common.v101.config as conf 
import config.config as conf
import zipfile
from test.v101.test import run_test,   home, citi
import itertools
import shutil
import imp	
import release as rel 	
e=sys.exit

test={}
dmhome=os.path.dirname(os.path.realpath(__file__))
default_vector=None #'pgres2pgres'
prog=None

def set_prog(relc,is_release):
	global prog
	if is_release:
		prog=[get_exe_name(relc)] #[conf.appname]
	else:
		prog=['C:\Python27\python','datamule.py']
#set_prog()
def build_test(relc, t_from,t_to,cmd):
	global conf
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
		#elif 'Limit' in db_from and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
		#	print  '%s does not support limit' % conf.dbs[db_to.upper()]
		#elif ('Limit' in db_from and db_from.startswith('CSV')) and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
		#	print  '%s does not support limit' % conf.dbs[db_to.upper()]			
		elif ('CSV' in db_from and 'Limit' in db_from ) and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
			print  '%s does not support limit' % conf.dbs[db_to.upper()]			
		elif 'Skip' in db_from and db_to.upper() in ['INFORC','INFOR','SLITE','TTEN','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE']:				
			print  '%s does not support "skip header row"' % conf.dbs[db_to.upper()]
		elif  'KeepSpoolFile' in db_from and db_to.startswith('CSV'):
			print  'Extractor does not support "KeepSpoolFile"'
		else:
			paramkey_from=db_from.split('_')[0]
			paramkey_to=db_to.split('_')[0]
			if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
				i +=1
				if 'Sharded' in db_from or 'Parallel' in  db_from:
					if db_to in ('CSV_File'):
						print 'skipping test %s to %s"' % (db_from,db_to) 
						continue
					else:
						if 'Limit' in db_from:
							limit=int(db_from.split('Limit')[1])
							test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),3,			3,				'"|"',		limit,0,'','','')		
						else:	
							test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),3,			3,				'"|"',		0,0,'','','')		
				
				else:
					if 'Limit' in db_from:
						limit=int(db_from.split('Limit')[1])
						test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		limit,0,'','','')		
					else:
						if 'KeepSpoolFile' in db_from:
							test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,1,'','','')		
						else:
							test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,0,'','','')		
				#print db_from, db_to
				#prog=[get_exe_name(relc)]
				#print exe
				#e(0)
				print(dir(run_test))
				a=run_test(db_from, db_to, prog,  citi=citi)
				pprint(a)
				e(0)
				comment,command=run_test(db_from, db_to, prog,  citi=citi)
				cmd.append ((db_from, db_to,command,comment))

				#print i
def build_test_4dbs(relc, tests,cmd):
	global conf
	i=len(cmd)
	#print t_from
	#pprint( tests)
	#e(0)
	all=[]
	for t in tests:
		#print t
		t_from,t_to= t
		
		#pprint (t_to)
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
			#elif 'Limit' in db_from and db_to.upper() in ['SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
			#	print  '%s does not support limit' % conf.dbs[db_to.upper()]
			elif ('CSV' in db_from and 'Limit' in db_from ) and db_to.upper() in ['MYSQL', 'INFOB', 'MARIA','SYIQ', 'SYANY', 'SYASE','INFORC','INFOR','SLITE','TTEN','PGRES']:				
				print  '%s does not support limit' % conf.dbs[db_to.upper()]			
			elif 'Skip' in db_from and db_to.upper() in ['INFORC','INFOR','SLITE','TTEN','DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE']:				
				print  '%s does not support "skip header row"' % conf.dbs[db_to.upper()]
			elif  'KeepSpoolFile' in db_from and db_to.startswith('CSV'):
				print  'Extractor does not support "KeepSpoolFile"'
			else:
				paramkey_from=db_from.split('_')[0]
				paramkey_to=db_to.split('_')[0]
				if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
					i +=1
					if 'Sharded' in db_from or 'Parallel' in  db_from:
						if db_to in ('CSV_File'):
							print 'skipping test %s to %s"' % (db_from,db_to) 
							continue
						else:
							if 'Limit' in db_from:
								limit=int(db_from.split('Limit')[1])
								test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),3,			3,				'"|"',		limit,0,'','','')		
							else:	
								test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),3,			3,				'"|"',		0,0,'','','')		
					
					else:
						if 'Limit' in db_from:
							limit=int(db_from.split('Limit')[1])
							test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		limit,0,'','','')		
						else:
							if 'KeepSpoolFile' in db_from:
								test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,1,'','','')		
							else:
								test['core']=('%s2%s' % (paramkey_from.lower(),paramkey_to.lower()),1,			1,				'"|"',		0,0,'','','')		
					#print db_from, db_to
					#prog=[get_exe_name(relc)]
					#print exe
					#e(0)
					comment,command=run_test(db_from, db_to, prog,  citi=citi)
					#print db_from, db_to
					#e(0)
					test_key='%s:%s' % (db_from, db_to)
					if test_key in all:
						pass
					else:
						cmd.append ((db_from, db_to,command,comment))
						all.append(test_key)
					#print i

def create_tests0(dbs):
	cmd=[]

	if 'ALL' in dbs:
		t_from=get_from_ALL()	
		t_to=get_to_ALL()
		build_test(t_from,t_to,cmd)
	else:
		for db in dbs:
			t_from=get_from(db)
			t_to=get_to_ALL()
			build_test(t_from,t_to,cmd)
			
			t_from=get_from_ALL()
			t_to=[db]	
			build_test(t_from,t_to,cmd)	
	return cmd	
def zip_dir(zipname, dir_to_zip):
	dir_to_zip_len = len(dir_to_zip.rstrip(os.sep)) + 1
	with zipfile.ZipFile(zipname, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
		for dirname, subdirs, files in os.walk(dir_to_zip):
			#print dirname, subdirs, files
			#print dirname, '\\logs\\' in dirname
			if not '\\logs\\' in dirname:
				for filename in files:
					path = os.path.join(dirname, filename)
					entry = path[dir_to_zip_len:]
					zf.write(path, entry)	
	#e(0)
def exec_cmd(shcmd):
	print shcmd
	p = Popen(shcmd,  stdout=PIPE , shell=True ) # '-S',  stdin=p1.stdout,
	out, err = p.communicate()	
	print out
	print err
	if err:
		print 'ERROR:', err	
	return (out,err)
def build_exe (appn,src,distpath,relc):
	if os.path.isfile(src):
		(bin,version, rts) = relc 
		#compile
		#distpath = r'C:\Python27\dist1'
		

		
		
	
		pyloc={ '32':'C:\Python278',
				'64':'C:\Python27'}
		pyinst= os.path.join(pyloc[bin], r'Scripts\pyinstaller.exe')
		#print pyinst
		#sys.exit(1)
		cmd = r'%s -y %s -n %s -p %s --distpath %s --log-level DEBUG' % (pyinst, src,appn,dmhome,distpath)
		#print cmd
		cmd=cmd.replace('\\','\\\\')
		#cmd=r'C:\\Python278\\Scripts\\pyinstaller.exe -y C:\\Python27\\csvextractor_1235\\csvextractor.py --log-level DEBUG'
		#print cmd

		shcmd = shlex.split(cmd)
		#pprint(shcmd)


		exec_cmd(shcmd)

		#print distpath
		exe = get_exe_name(relc) #os.path.join(distpath,appn,'%s.%s' % (appn,conf.appex))
		#print exe
		return exe
def get_exe_name(relc):
	distpath=get_distpath(relc[0])
	appn=get_appn(relc)
	return os.path.join(distpath,appn,'%s.%s' % (appn,conf.appex))
def save_txt(exefn,opt,txtn):	
	exedir=os.path.dirname(exefn)
	fn = os.path.basename(exefn)
	cmd=[r'%s' % exefn]+opt
	#pprint(shlex.split(cmd))
	(out, err) = exec_cmd(cmd)
	#print out 
	#print err
	
	out=out.replace('\r\n','\n')
	fsave(os.path.join(exedir,'%s.txt' % txtn),'##\n##%s %s \n##\n%s' % (fn,' '.join(opt),out))
def get_txt(exefn,opt,txtn):	
	exedir=os.path.dirname(exefn)
	fn = os.path.basename(exefn)
	cmd=[r'%s' % exefn]+opt
	#pprint(shlex.split(cmd))
	(out, err) = exec_cmd(cmd)
	#print 'out',out 
	#print 'out',err
	#print 'fn',fn
	
	out=out.replace('\r\n','\n')
	print '##\n##%s %s \n' % (fn,' '.join(opt)),out
	#e(0)
	return ('##\n##%s %s \n' % (fn,' '.join(opt)),out)
def get_distpath(rs):
	return (os.sep).join(dmhome.split(os.sep)[:-1]+['%s_dist_%s\\%s' % (conf.appn,rs,rts.replace('/','.').replace(' ','_').replace(':','.'))])
def release(relc,exefn):
	pypath=(os.sep).join(dmhome.split(os.sep)[:-1])	
	
	if os.path.isfile(exefn):
		save_txt(exefn,['-h'],'HELP')
		save_txt(exefn,['-h','FEAT'],'FEATURES')
		save_txt(exefn,['-h','ALL'],'README')
		save_txt(exefn,['-h','ABOUT'],'ABOUT')
		#compress use cases
		exedir = os.path.dirname(exefn)
		ex_name='%sbit_tests' % (relc[0])
		uzipn= os.path.join(exedir,'%s.zip' % ex_name)
		print uzipn
		zipfrom=  get_test_dir(get_dir_from_ts(rts),relc[0]) #os.path.join(dmhome,'example%s' % relc[0])
		zip_dir(uzipn,zipfrom )
		
		#sys.exit(1)
		print 'compile ok'
		#compress
		#forapp=conf.dbs[conf.from_filter[0]]
		for fapp in conf.from_filter:
			forapp=conf.dbs[fapp]
			rel_appn = 'CSV-Extractor-for-%s-%sbit' % (forapp, relc[0])
			zipn= os.path.join(pypath,'Release','%s.zip' % rel_appn)
			print zipn
			distpath = get_distpath(relc[0])
			zip_dir(zipn,distpath )
			shutil.copyfile(uzipn,os.path.join(pypath,'Release','%s.zip' % ex_name))
		
	else:
		print 'no exe'	
def fsave(fn,text):
	f=open(fn,'w')
	f.write(text)
	f.close()	

def build(relc):	
	(bin,version, rts) = relc 

	global conf
	#conf=None
	#import __builtin__
	__builtin__.copy_vector = None
	#import common.v101.config as conf 
	conf.rel = reload(conf.rel)
	
		
	#print conf.appname
	#appn, appex = os.path.splitext(conf.appname)
	#appn='%s%s' % (appn,bin)
	assert conf.appn and conf.appex, 'App name ora app ext are not set [%s, %s]' % (conf.appn, conf.appex)
	dm=os.path.join(dmhome, 'datamule.py')
	if 0:
		scr_to= '%s.py' % conf.appn
		#print scr_to
		#backup if exists
		src_to_loc = os.path.join(dmhome, scr_to)
		if os.path.isfile(src_to_loc):
			print 'backing up %s' % scr_to
			bkp = os.path.join(dmhome,'release_backup',('%s_%s_%s_%s' % ((scr_to,)+relc)))
			#print bkp
			os.rename( src_to_loc,bkp)
		
		#os.copy(dm, src_to_loc)
		#import shutil
		shutil.copyfile(dm, src_to_loc)
	if 1:
		scr_to= 'datamule.py' 
		#print scr_to
		#backup if exists
		src_to_loc = os.path.join(dmhome, scr_to)
		if os.path.isfile(src_to_loc):
			print 'backing up %s' % scr_to
			bkp = os.path.join(dmhome,'release_backup',('%s_%s_%s_%s' % ((scr_to,)+relc)).replace('/','').replace(' ','').replace(':',''))
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
	distpath=get_distpath(relc[0])
	#print distpath
	#appn='%s%s.%s' % (conf.appn,relc[0],conf.appex)
	appn=get_appn(relc)
	exefn=build_exe(appn,dm,distpath,relc)
	return exefn
	#sys.exit(1)

	release(relc,exefn)
def get_appn(relc):
	return '%s%s' % (conf.appn,relc[0])
def get_test_dir(rts,reg):
	return os.path.join(dmhome,'test_%s' % conf.appn,rts,'%sbit' % reg)
def create_tests(reg,cmd,rts):
	out=[]
	test_dir = get_test_dir(rts,reg)
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
		if paramkey_to.upper() in conf.ff:
			action ='Extract'
		if paramkey_from.upper() in conf.ff:
			action ='Load'
		from_dbname=conf.dbs[paramkey_from.upper()].replace(' ','')
		to_dbname=conf.dbs[paramkey_to.upper()].replace(' ','')
		
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

def run_all_tests(cmd,rts):
	for c in cmd:
		#pprint (c)
		out=[]
		t_from, t_to, command = c

		#print command
		tname='%s.txt' % os.path.splitext(os.path.basename(command))[0]
		#print tname
		tldir=os.path.join(os.path.dirname(command),'test_log')
		if not os.path.isdir(tldir):
			os.makedirs(tldir)
		tlfile=os.path.join(tldir,tname)
		assert not os.path.isfile (tlfile), 'Test log already exists.\n%s' % tlfile
		#print tlfile
		#print 'Exists?' ,os.path.isfile (tlfile)
		print command
		p = Popen([command],  stdout=PIPE , stderr=PIPE, shell=True ) # '-S',  stdin=p1.stdout,
		out, err = p.communicate()	
		print out
		print err
		if err:
			print 'ERROR:', err
			#print error			
		status=p.wait()
		print status
		#sys.exit(1)
		#out, err = p.communicate()	
		tlog='\n'.join(out)
		#pprint(tlog)

		#print tlfile
		f=open( tlfile,'w')
		f.write(tlog)
		f.close()
		#sys.exit(1)

	

def get_dir_from_ts(ts):
	return ts.replace('/','').replace(' ','_').replace(':','')	
from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path, pattern, subst):
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
def run_all_exe_tests(cmd,rts,exefn):
	for c in cmd:
		print c
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
		#pprint( command)
		#e(0)
		p = Popen([command],  stdout=PIPE, stderr=PIPE) # '-S',  stdin=p1.stdout,
		out, err = p.communicate()	
		#print out
		#print err
		#e(0)
		#print err
		if err:
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
		replace(command, '198Morgan', 'test_pwd')
		#sys.exit(1)
def release_ucon(relc,exefn):
	#ucon_dir
	reldir=os.path.dirname(exefn)
	ucon_to_dir=os.path.join(reldir,'config')
	#os.mkdir(ucon_to_dir)
	#assert os.path.isdir(ucon_to_dir), 'Ucon release dir does not exists\n%s' % ucon_to_dir
	#print get_distpath(relc[0])
	ucon_home=os.path.join(dmhome,'config')
	shutil.copytree(ucon_home,ucon_to_dir)
	#sys.exit(1)	
def release_exe(relc,exefn,ucases):
	pypath=(os.sep).join(dmhome.split(os.sep)[:-1])	
	exedir = os.path.dirname(exefn)
	rel_appn = conf.getExeTitle()
	rel_dir = conf.getAppTitle().replace(' ','-').replace('*','-')
	
	if os.path.isfile(exefn):

		save_txt(exefn,['-h'],'HELP')
		save_txt(exefn,['-h','FEAT'],'FEATURES')
		(hdr,code) =get_txt(exefn,['-h','ALL'],'README')
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
				fsave(os.path.join(ucdir,'%s.txt' % uc),ucbody)
			print out
		#print 'code'
		#print code
		#e(0)
		
		fsave(os.path.join(exedir,'%s.txt' % 'README'),'%s\n%s\n--USE CASES--\n\n%s\n%s\n%s' % (hdr,code,out1,out,bout))
		#e(0)
		save_txt(exefn,['-h','ABOUT'],'ABOUT')
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
		distpath = get_distpath(relc[0])
		print distpath
		#e(0)
		zip_dir(zipn,distpath )
		ghzipdir=os.path.join(pypath,'Release','GitHub',rel_dir)
		if not os.path.isdir(ghzipdir):
			os.makedirs(ghzipdir)
		zfile = zipfile.ZipFile(zipn)
		zfile.extractall(ghzipdir)
		#copy README
		appn=get_appn(relc)
		readme_from=os.path.join(ghzipdir,appn,'README.txt')
		readme_to=os.path.join(sfzipdir,'README.txt')
		assert os.path.isfile(readme_from), 'READE.txt does not exists at\n %s' % readme_from
		shutil.copyfile(readme_from,readme_to)
		shutil.copyfile(readme_from,os.path.join(ghzipdir,'README.txt'))
		#remove logs		
		#logs_dir=os.path.join(ghzipdir,appn,'logs')
		#assert os.path.isdir(logs_dir)
		#shutil.rmtree(logs_dir)
		#e(0)
		#shutil.copyfile(uzipn,os.path.join(pypath,'Release','%s.zip' % ex_name))

		
	else:
		print 'no exe'	
def get_param (cmd, c):
	for i in cmd.split('\n'):
		#print i
		if i.startswith(c):
			#print i
			return i.split(' ')[1]
	#e(0)
	return -1
def get_tests_dir(exefn):
	return os.path.join(os.path.dirname(exefn),'tests')
def create_exe_tests(reg,cmd,rts,exefn):
	out=[]
	#exe_dir=os.path.dirname(exefn)
	

	#sys.exit(1)
	assert os.path.isfile(exefn), 'Executable file does not exists at\n %s' % exefn
	#	os.makedirs(test_dir) 
	for i in cmd:
		(db_from, db_to,c,cmt) = i
		#print i
		#sys.exit(1)
		paramkey_from=db_from.split('_')[0]
		paramkey_to=db_to.split('_')[0]
		from_to='%s_to_%s' % (conf.dbs[paramkey_from].replace(' ','').replace('*',''), conf.dbs[paramkey_to].replace(' ','').replace('*',''))
		test_dir =os.path.join(os.path.dirname(exefn),'tests',from_to)
		#print exe_dir
		if not os.path.isdir(test_dir):
			os.makedirs(test_dir)		
		#print paramkey_from
		action ='Copy'
		if paramkey_to.upper() in conf.ff:
			action ='Extract'
		if paramkey_from.upper() in conf.ff:
			action ='Load'
		from_dbname=conf.dbs[paramkey_from.upper()].replace(' ','')
		to_dbname=conf.dbs[paramkey_to.upper()].replace(' ','')
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
			dir="""Read each CSV file from a directory "%s".""" % get_param(c, '-I')
		if 'QueryDir' in db_from:
			dir="""Read each SQL query file from a directory "%s".""" % get_param(c, '-Q')
		if 'QueryFile' in db_from:
			dir="""Read SQL from a query file "%s".""" % get_param(c, '-q')  
		skip=action
		sharded=''
		#pprint(c)
		#e(0)
		nos=get_param(c,'-r')
		ps =get_param(c,'-o')
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
		descr ="%s %s %s into %s%s %s." % (skip, from_dbname,src,to_dbname,' '.join(db_to.split('_')[1:]), trg)
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

def	get_use_case(relc,cmd):		
		(db_from, db_to,c,cmt) = cmd
		(reg, v, ts) =relc
		rts=get_dir_from_ts(ts)
		test_dir = get_test_dir(rts,reg)
		#print i
		#sys.exit(1)
		paramkey_from=db_from.split('_')[0]
		paramkey_to=db_to.split('_')[0]
		#print paramkey_from
		action ='Copy'
		if paramkey_to.upper() in conf.ff:
			action ='Extract'
		if paramkey_from.upper() in conf.ff:
			action ='Load'
		from_dbname=conf.dbs[paramkey_from.upper()].replace(' ','')
		to_dbname=conf.dbs[paramkey_to.upper()].replace(' ','')
		title= '%s->%s' % (db_from,db_to) #'_'.join(db_from.split('_')[1:]))
		src='table1'
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
  """ % get_param(c, '-I')
		if 'QueryDir' in db_from:
			dir="""Read each SQL query file from a directory "%s".
  """ % get_param(c, '-Q')
		if 'QueryFile' in db_from:
			dir="""Read SQL from a query file "%s".
  """ % get_param(c, '-q')  
		skip=action
		sharded=''
		#pprint(c)
		#e(0)
		nos=get_param(c,'-r')
		ps =get_param(c,'-o')
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

def set_tests(relc, cmd, to_test, from_t):
	ucases={}
	if 0:
		cmd=create_tests('ALL')
	else:		 		

		#t_from=['CSV_File'] #get_from_ALL() #get_from(conf.from_filter[0]) 
		#['CSV_File', 'CSV_File_Limit10', 'CSV_FileSkip1', 'CSV_ShardedFile','CSV_ShardedFile_Limit10', 'CSV_ShardedFileSkip1','CSV_Dir', 'CSV_Dir_Limit10', 'CSV_DirSkip1', 'CSV_ShardedDir','CSV_ShardedDirSkip1']
		assert to_test, 'to_test is not set'
		#	#it's Pro
		#	to_test=conf.dbs.keys()
		t_to=to_test #conf.to_filter #['ORAXE'] #['CSV_Default', 'CSV_Dir','CSV_File']
		#'DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'
		#print t_to
		#print len(from_t)
		#e(0)
		if 1:
		#for to_t in t_to:
			#print t_from
			#print to_test
			#sys.exit(0)
			if 1: #not in ['DBTWS']:
				#build_test(relc, from_t,[to_t],cmd)
				build_test(relc, from_t,to_test,cmd)
			#print to_t,len(cmd)

	#e(0)
	#print len(cmd)
	#e(0)
	for c in cmd:
		#print c
		t_from, t_to, _,_ = c
		(paramkey_from,paramkey_to,title,(dir,sharded,descr), header)=get_use_case(relc,c)
		from_to='%s_to_%s' % (conf.dbs[paramkey_from].replace(' ','').replace('*',''), conf.dbs[paramkey_to].replace(' ','').replace('*',''))
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
def set_tests_4dbs(relc, cmd, tests):
	ucases={}
	build_test_4dbs(relc, tests,cmd)
	for c in cmd:
		#print c
		t_from, t_to, _,_ = c
		(paramkey_from,paramkey_to,title,(dir,sharded,descr), header)=get_use_case(relc,c)
		from_to='%s_to_%s' % (conf.dbs[paramkey_from].replace(' ','').replace('*',''), conf.dbs[paramkey_to].replace(' ','').replace('*',''))
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
	
def get_from_ALL():
	out=[]
	for db in ['MYSQL','CSV']: #['INFOR','DBTWS','SSEXP','SYANY','PGRES','TTEN','SLITE','SYASE','SSENT','MYSQL','MARIA','ORA']: #conf.dbs:
	#for db in ['INFOR', 'DBTAES','DBTES','DBTAWS','DBTWS','DBTE', 'DBTEC', 'DBTDE','SSEXP','SYANY','PGRES','TTEN','SLITE','SYASE','SSENT','MYSQL','MARIA','ORA','EXAD','ORAXE']: #conf.dbs:
		#'DBTAES','DBTES','DBTAWS','DBTWS','DBTE', 'DBTEC', 'DBTDE'
		#'DBTAES','ORA','ORAXE','EXAD', 'SSENT','SSEXP'
		#'INFOR','DBTWS','SSEXP','SYANY','PGRES','TTEN','SLITE','SYASE','SSENT','MYSQL','MARIA','ORA'
		#print db
		out= out+ get_from(db)
	#sys.exit()
	return out
def get_to_ALL():
	out=[]
	for db in ['MYSQL','CSV']: #return ['SLITE', 'MARIA', 'MYSQL','INFOB', 'INFOR','INFORC','TTEN','SYIQ','SYASE','SYANY', 'PGRES', 'DBTAES','DBTES','DBTAWS','DBTWS','DBTE', 'DBTEC', 'DBTDE','ORA','ORAXE','EXAD', 'SSENT','SSEXP', 'CSV_File','CSV_Dir','CSV_Default']
	#for db in ['INFOR', 'DBTAES','DBTES','DBTAWS','DBTWS','DBTE', 'DBTEC', 'DBTDE','SSEXP','SYANY','PGRES','TTEN','SLITE','SYASE','SSENT','MYSQL','MARIA','ORA','EXAD','ORAXE']: #conf.dbs:
		#'DBTAES','DBTES','DBTAWS','DBTWS','DBTE', 'DBTEC', 'DBTDE'
		#'DBTAES','ORA','ORAXE','EXAD', 'SSENT','SSEXP'
		#'INFOR','DBTWS','SSEXP','SYANY','PGRES','TTEN','SLITE','SYASE','SSENT','MYSQL','MARIA','ORA'
		#print db
		print db
		out= out+ get_to(db)
	#sys.exit()
	return out
	
def get_to(db):
	if db in ('CSV'):
		return ['CSV_Default', 'CSV_File','CSV_Dir']
	elif db in conf.dbs.keys():
		return [db]
	else:
		assert 1==2, 'get_to() is not defined for db: %s' % db	
def get_to_4dbs(dbs):
	out=[]
	pprint(dbs)
	for db in dbs:
		out=out+get_to(db)
	return out
def get_from(db):
	print db
	if db in ('MYSQL','MARIA','INFOB'):
		return ['%s_Table' % db, '%s_Table_Limit1000' % db, '%s_Table_KeepSpoolFile' % db,  '%s_Partition'  % db, '%s_Partition_Limit22'  % db, 
		'%s_Subpartition'  % db,'%s_Subpartition_Limit33'  % db,'%s_ShardedSubpartition'  % db, '%s_ShardedTable'  % db, '%s_ShardedPartition'  % db, 
		'%s_QueryFile'  % db,'%s_QueryFile_Limit100'  % db,'%s_QueryDir'  % db, '%s_QueryDir_Limit333'  % db, '%s_ShardedQuery'  % db]
		
	#if db in ('MARIA'):
	#	return ['MARIA_Table', 'MARIA_Partitioned', 'MARIA_SubPartitioned','MARIA_ShardedSubPartitioned', 'MARIA_ShardedTable', 'MARIA_ShardedPartitioned', 'MARIA_Query','MARIA_ShardedQuery']
	if db in ('ORA','EXAD'):
		return ['%s_TimestampTable' % db,'%s_TimezoneTable' % db,'%s_DateTable' % db, '%s_Table_Limit10' % db, '%s_Partition' % db, '%s_Partition_Limit10' % db, '%s_ShardedTable' % db, 
		'%s_ShardedPartition' % db,'%s_Subpartition' % db,'%s_Subpartition_Limit10' % db, '%s_ShardedSubpartition' % db,
		'%s_QueryFile' % db,'%s_QueryFile_Limit10' % db,'%s_QueryDir' % db,'%s_QueryDir_Limit10' % db, 
		'%s_Partition_KeepSpoolFile' % db,'%s_Table_KeepSpoolFile' % db,'%s_Subpartition_KeepSpoolFile' % db]
	if db in ('ORAXE'):
		return ['ORAXE_Table',  'ORAXE_ShardedTable', 'ORAXE_QueryFile','ORAXE_QueryDir','ORAXE_ParallelQueryDir']
	#if db in ('EXAD'):
	#	return ['EXAD_Table', 'EXAD_Partition', 'EXAD_ShardedTable', 'EXAD_ShardedPartition','EXAD_Subpartition', 'EXAD_ShardedSubpartition','EXAD_Query',]
	if db in ('CSV'):
		return ['CSV_File', 'CSV_File_Limit10', 'CSV_FileSkip1', 'CSV_ShardedFile','CSV_ShardedFile_Limit10', 'CSV_ShardedFileSkip1','CSV_Dir', 'CSV_Dir_Limit10', 'CSV_DirSkip1', 'CSV_ShardedDir','CSV_ShardedDirSkip1']
		
		
	if db in ('SSEXP'):
		return ['SSEXP_QueryFile','SSEXP_QueryFile_Limit15','SSEXP_QueryDir','SSEXP_QueryDir_Limit25','SSENT_QueryDir_Limit25', 'SSEXP_ShardedQueryFile', 'SSEXP_Table','SSEXP_Table_Limit10', 'SSEXP_ShardedTable','SSEXP_ShardedTable_Limit50']
		
		
	if db in ('SSENT'):
		return ['SSENT_QueryFile','SSENT_QueryDir', 'SSENT_QueryFile_Limit15', 'SSENT_ShardedQueryFile', 'SSENT_Table','SSENT_Table_Limit10', 
		'SSENT_ShardedTable','SSENT_ShardedTable_Limit50', 'SSENT_Partition','SSENT_Partition_Limit20', 'SSENT_ShardedPartition']
	if db in ('SLITE'):
		return ['SLITE_Table','SLITE_ShardedTable','SLITE_QueryFile','SLITE_ShardedQueryFile','SLITE_QueryDir','SLITE_ParallelQueryDir']	
	if db in ('INFOR','INFORC'):
		return ['%s_Table' % db,'%s_Table_Limit15' % db,'%s_ShardedTable' % db,'%s_ShardedTable_Limit66' % db,  '%s_QueryFile' % db,'%s_QueryFile_Limit20' % db,
		'%s_ShardedQueryFile' % db,'%s_ShardedQueryFile_Limit55' % db,  '%s_QueryDir' % db,'%s_QueryDir_Limit25' % db,
		'%s_ParallelQueryDir' % db, '%s_ParallelQueryDir_Limit30' % db ]	

	if db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
		return ['%s_Partition' % db,'%s_Partition_Limit30' % db,  '%s_ShardedPartition' % db, '%s_ShardedPartition_Limit50' % db, 
		'%s_Table' % db,'%s_Table_Limit20' % db,   '%s_ShardedTable' % db, '%s_ShardedTable_Limit65' % db,  
		'%s_QueryFile' % db,'%s_QueryFile_Limit10' % db, '%s_ShardedQueryFile' % db,
		'%s_QueryDir' % db,'%s_QueryDir_Limit10' % db,'%s_ParallelQueryDir' % db,'%s_ParallelQueryDir_Limit10' % db ]
		
	if db in ('SYASE'):
		#return ['SYASE_Query']
		return ['SYASE_QueryFile','SYASE_QueryFile_Limit10', 'SYASE_ShardedQueryFile','SYASE_QueryDir', 'SYASE_QueryDir_Limit15',
		'SYASE_ParallelQueryDir', 'SYASE_ParallelQueryDir_Limit14', 'SYASE_Table','SYASE_Table_Limit22', 'SYASE_ShardedTable']	

		
	if db in ('PGRES'):
		return ['PGRES_ShardedPartition', 'PGRES_ShardedTable', 'PGRES_ShardedQueryFile', 'PGRES_QueryFile','PGRES_QueryFile_Limit11','PGRES_ParallelQueryDir',
		'PGRES_QueryDir','PGRES_QueryDir_Limit12','PGRES_Table','PGRES_Table_Limit15','PGRES_Partition','PGRES_Partition_Limit33']	



	if db in ('TTEN'):
		return ['TTEN_Table', 'TTEN_ShardedTable_Limit40','TTEN_ParallelQueryDir_Limit30','TTEN_Table_Limit20', 'TTEN_ShardedTable',
		'TTEN_QueryFile','TTEN_QueryFile_Limit15','TTEN_ShardedQueryFile','TTEN_QueryDir','TTEN_QueryDir_Limit25','TTEN_ParallelQueryDir']	
	if db in ('SYANY'):
		return ['SYANY_QueryFile','SYANY_ShardedQueryFile','SYANY_QueryDir','SYANY_ParallelQueryDir','SYANY_Table','SYANY_ShardedTable']	
	if db in ('SYIQ'):
		#return ['SYIQ_Query']			
		return ['SYIQ_QueryFile','SYIQ_ShardedQueryFile','SYIQ_QueryDir','SYIQ_ParallelQueryDir','SYIQ_Table','SYIQ_ShardedTable']	
	else:
		assert 1==2, 'get_from() is not defined for db: %s' % db
		
def get_from_4dbs(dbs):
	out=[]
	for db in dbs:
		out=out+ get_from(db)
	return out
		
def build_and_release_1to1(from_tests,to_tests, app_, regs, is_release):
	global rts
	(app_author, apptitle, appn)=app_
	from_t=[]
	for f_t in from_tests:
		from_tst=[f_t]
		if not f_t:
			#conf.to_filter=None
			#from_tst=None
			from_t=get_from_ALL()
		else:
			from_t=get_from(f_t)
			#pprint(from_t)
			#e(0)
			########
			if not is_release:
				from_t=['MYSQL_Table']
			########
		for to_t in to_tests:
			to_tst=[to_t]
			
			if not to_t:
				#conf.to_filter=None
				to_tst=get_to_ALL()	
			else:
				to_tst=get_to(to_t)
				########
				if not is_release:
					to_tst=['MYSQL']
				########
			#print to_tst
			#e(0)
			ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
			rts=get_dir_from_ts(ts)		
			for rs in regs:
				relc=(rs, '1.23.9', ts)
				save_release(relc, to_tst,from_tst,is_release,app_author,apptitle,appn)
				imp.reload(rel)
				imp.reload(conf)
				
				#if (is_release,app_author,apptitle,from_tst) == (conf.release,conf.app_author,conf.apptitle,conf.from_filter):
				#	pass
				#else:
				#	e(0)
				conf.setreg(rs)
				set_prog(relc,is_release)
				#print rs
				#print f_t, to_t
				#print conf.release,conf.app_author,conf.apptitle,conf.from_filter
				#print is_release,app_author,apptitle,from_tst
				if 1:
					if is_release:
						exefn= build(relc)
						#e(0)
						cmd=[]
						ucases=set_tests(relc,cmd,to_tst,from_t)
						#ucases=build_test_4dbs(relc, from_t,to_test,cmd)
						#pprint(ucases)
						#print len(ucases)
						#print ucases.keys()
						#e(0)
						tests=create_exe_tests(rs,cmd,rts,exefn)
						#pprint(tests)
						#e(0)
						release_ucon(relc,exefn)
						run_all_exe_tests(tests,rts,exefn)
						release_exe(relc,exefn, ucases)
						print exefn
					else:
						cmd=[]
						ucases=set_tests(relc, cmd,to_tst,from_t)
						tests=create_tests(rs,cmd,rts)
						print conf.release
				#e(0)
def build_and_release_4dbs(for_dbs,from_dbs,to_dbs, app, regs, v, is_release,nor_t):
	#global rts
	ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	rts=get_dir_from_ts(ts)	
	(app_author, apptitle, appn)=app
	from_tst=[]
	tests=[]
	if not is_release:
		########
		from_tst,to_tst= nor_t
		from_db_tests,to_db_tests =None, None
		if for_dbs:
			from_db_tests =['MYSQL_Table']
			to_db_tests=['MYSQL']
		########
	else:			
		if not from_dbs:
			from_tst=get_from_ALL()
		else:
			from_tst=get_from_4dbs(from_dbs)
		pprint(to_dbs)	
		if not to_dbs:
			to_tst=get_to_ALL()	
		else:
			to_tst=get_to_4dbs(to_dbs)
		if for_dbs:
			from_db_tests = get_from_4dbs(for_dbs)
			to_db_tests = get_to_4dbs(for_dbs)
	if to_db_tests and from_db_tests:
		#print from_dbs[0],to_dbs[0]
		#e(0)
		if from_dbs[0]==to_dbs[0]:
			tests.append([from_db_tests,to_tst])
			tests.append([from_db_tests,to_tst])
		else:
			tests.append([from_db_tests,to_tst])
	else:
		tests.append([from_tst,to_tst])
	ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	rts=get_dir_from_ts(ts)		
	for rs in regs:
		relc=(rs, v, ts)
		save_release_4dbs(relc,for_dbs,from_dbs, to_dbs,is_release,app_author,apptitle,appn,tests)
		#(relc,for_dbs,from_dbs, to_dbs,is_release,app_author,apptitle,appn,tests):
		imp.reload(rel)
		imp.reload(conf)
		
		conf.setreg(rs)
		set_prog(relc,is_release)
		#e(0)

		if is_release:
			exefn= build(relc)
			#e(0)
			cmd=[]
			ucases=set_tests_4dbs(relc,cmd,tests)
			#print ucases
			#e(0)
			exe_tests=create_exe_tests(rs,cmd,rts,exefn)
			
			release_ucon(relc,exefn)
			#e(0)
			run_all_exe_tests(exe_tests,rts,exefn)
			#e(0)
			release_exe(relc,exefn, ucases)
			print exefn
		else:
			cmd=[]
			ucases=set_tests(relc, cmd,to_tst,from_tst)
			py_tests=create_tests(rs,cmd,rts)
			print conf.release

def save_release(relc,to_filter,from_filter,is_release,app_author,apptitle,appn):
	bin,version, rts = relc
	relcfg="""# release setup
bin='%s'
version='%s'
ts='%s'
to_filter=%s
from_filter=%s
release=%s
app_author='%s'
apptitle='%s'
appn='%s'
""" % (bin,version, rts,to_filter,from_filter,is_release,app_author,apptitle,appn)
	print relcfg
	fn=os.path.join(dmhome,'release.py')
	fsave(fn,relcfg)
	os.remove(os.path.join(dmhome,'release.pyc'))
	import py_compile
	py_compile.compile('release.py')
	print 'release saved'
def save_release_4dbs(relc,for_dbs,from_dbs, to_dbs,is_release,app_author,apptitle,appn,tests):
	bin,version, rts = relc
	relcfg="""# release setup
bin='%s'
version='%s'
ts='%s'
for_dbs=%s
from_dbs=%s
to_dbs=%s
release=%s
app_author='%s'
apptitle='%s'
appn='%s'
tests=%s
""" % (bin,version, rts,for_dbs,from_dbs,to_dbs,is_release,app_author,apptitle,appn,tests)
	print relcfg
	fn=os.path.join(dmhome,'release.py')
	fsave(fn,relcfg)
	os.remove(os.path.join(dmhome,'release.pyc'))
	import py_compile
	py_compile.compile('release.py')
	print 'release saved'	
	#(bin,version, rts) = relc 
def run_all(for_dbs,app,regs, is_release):
	#print from_tests,to_tests
	for db in for_dbs :	
		if db not in ['CSV']:
			from_tests,to_tests=([db],[db])
			print from_tests,to_tests
			ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
			rts=get_dir_from_ts(ts)	
			#e(0)
			#from_tests,to_tests=(['SSEXP'],['CSV'])	
			build_and_release_1to1(from_tests,to_tests, app,regs,is_release) #,['32'])
			#e(0)
def run_all_4db_remove(for_dbs,dbs_from,dbs_to,app,regs, is_release):
	#print from_tests,to_tests
	if 1:
	#for db in for_dbs :	
		if 1:
		#if db not in ['CSV']:
			from_tests,to_tests=([db,'CSV'],[db,'CSV'])
			print from_tests,to_tests
			ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
			rts=get_dir_from_ts(ts)	
			#e(0)
			#from_tests,to_tests=(['SSEXP'],['CSV'])	
			build_and_release_4db(from_tests,to_tests, app,regs,is_release) #,['32'])
			#e(0)
def run_1to1(app,regs,is_release):
	#(author,title,short ) =app
	run_all(  ['MYSQL','MARIA','INFOB']  	,app,regs,is_release)
	#e(0)
	run_all(  ['DBTAES','DBTES','DBTAWS','DBTWS','DBTE','DBTEC','DBTDE']  ,app,regs,is_release)
	run_all(  ['ORA','ORAXE','EXAD']  		,app,regs,is_release)
	run_all(  ['SYASE','SYANY','SYIQ']  	,app,regs,is_release)
	run_all(  ['SSEXP','SSENT']  			,app,regs,is_release)
	run_all(  ['INFOR','INFORC'] 			,app,regs,is_release)
	run_all(  ['SYASE','SYANY','SYIQ']  	,app,regs,is_release)
	run_all(  ['PGRES']+['TTEN']+['SLITE']  ,app,regs,is_release)
	
if __name__=='__main__':
	cmd=[]
	ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	rts=get_dir_from_ts(ts)

	to_tests=['MYSQL','MARIA','INFOB']
	to_tests=['DBTAES','DBTES','DBTAWS','DBTWS','DBTE','DBTEC','DBTDE'] 
	to_tests=['MYSQL','MARIA','INFOB']
	to_tests=['PGRES']

	from_tests,to_tests = (None,None)	
	app_author, apptitle, appn = ('Alex Buzunov', "CSV*Extractor", 	'csvextractor')
	app_author, apptitle, appn = ('Alex Buzunov', "QueryCopy", 		'qc')
	if 0:
		app = ('Alex Buzunov', "DataMigrator", 'dm')
		#run_all(for_dbs=['MYSQL'],app=app, regs=['32'],is_release=True)
		#build_and_release_4dbs(for_dbs,from_dbs,to_dbs, app, regs, v, is_release)
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=conf.dbs.keys(),to_dbs=conf.dbs.keys(),app=app, regs=['64','32'],v=('1.23.9'),is_release=True,nor_t=(['PGRES_TimestampTable'],['CSV_File']))
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=['PGRES'],to_dbs=['PGRES'],app=app, regs=['32'],v=('1.23.9'),is_release=False,nor_t=(['ORA_TimezoneTable_KeepSpoolFile'],['PGRES']))
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=['PGRES'],to_dbs=['PGRES'],app=app, regs=['32'],v=('1.23.9'),is_release=False,nor_t=(['PGRES_Table'],['CSV_File']))
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=['PGRES'],to_dbs=['PGRES'],app=app, regs=['32'],v=('1.23.9'),is_release=False,nor_t=(['CSV_TimezoneFile'],['ORA']))
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=['PGRES'],to_dbs=['PGRES'],app=app, regs=['32'],v=('1.23.9'),is_release=False,nor_t=(['PGRES_TimestampTable'],['CSV_File']))
		build_and_release_4dbs(for_dbs=['CSV'],from_dbs=['CSV'],to_dbs=['PGRES'],app=app, regs=['64','32'],v=('1.23.9'),is_release=True,nor_t=(['ORA_QueryDir'],['PGRES']))
		#build_and_release_4dbs(for_dbs=['ORA'],from_dbs=['ORA'],to_dbs=['PGRES'],app=app, regs=['32'],v=('1.23.9'),is_release=False,nor_t=(['ORA_TimestampQueryDir'],['CSV_Dir']))
	else:
		#app = ('Alex Buzunov', "TableCopy", 'tc')
		#run_1to1(app,regs=['64', '32'],is_release=True)
		
		app = ('Alex Buzunov', "QueryCopy", 'qc')
		run_1to1(app,regs=[ '32'],is_release=True)
		e(0)
		app = ('Alex Buzunov', "DataPipe", 'dp')
		run_1to1(app,regs=['64', '32'],is_release=True)
		
	

	
