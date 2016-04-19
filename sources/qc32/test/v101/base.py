import tempfile
import py_compile
import os, sys
import zipfile
from subprocess import Popen, PIPE
e=sys.exit

class base(object):
	"""Test"""
	def __init__(self):
		self.ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	def get_dir_from_ts(self, ts):
		return ts.replace('/','').replace(' ','_').replace(':','')
	def save_file(self,fn, txt):
		f = open(fn, "w")
		f.write(txt)
		f.close()
	def get_temp_token(self):
		temp_file_name=tempfile.mkstemp()[1].split('\\')[-1]
		return temp_file_name.strip('/tmp')	
	def fsave(self, fn,text):
		f=open(fn,'w')
		f.write(text)
		f.close()		

	def append_release(self,code):
		
		fn=os.path.join(self.dmhome,'release.py')
		f=open(fn,'a')
		f.write('%s\n' % code)
		f.close()
		os.remove(os.path.join(self.dmhome,'release.pyc'))
		
		py_compile.compile('release.py')
		print 'release changed'	
		#(bin,version, rts) = relc 	
		#e(0)
	def set_prog(self,relc):
		#global prog
		if self.is_release:
			self.prog=[self.get_exe_name(relc)]
		else:
			self.prog=['C:\Python27\python','datamule.py']
	def get_exe_name(self,relc):
		distpath=self.get_distpath(relc[0])
		appn=self.get_appn(relc)
		return os.path.join(distpath,appn,'%s.%s' % (appn,conf.appex))
	def get_distpath(self,rs):
		return (os.sep).join(dmhome.split(os.sep)[:-1]+['%s_dist_%s\\%s' % (conf.appn,rs,self.rts.replace('/','.').replace(' ','_').replace(':','.'))])
	def get_appn(self,relc):
		return '%s%s' % (conf.appn,relc[0])
	def get_test_dir(self, reg):
		return os.path.join(self.dmhome,'test_%s' % self.conf.appn,self.rts,'%sbit' % reg)
	def get_param (self, cmd, c):
		for i in cmd.split('\n'):
			#print i
			if i.startswith(c):
				#print i
				return i.split(' ')[1]
		#e(0)
		return -1
	def get_tests_dir(self, exefn):
		return os.path.join(os.path.dirname(exefn),'tests')
	
	def get_from_dbs(self, dbs):
		out=[]
		for db in dbs:
			out=out+ self.get_from(db)
		return out

	def get_from(self, db):
		print db
		if db in ('MYSQL','MARIA','INFOB'):
			return ['%s_Table' % db, '%s_Table_Limit1000' % db, '%s_Table_KeepSpoolFile' % db,  '%s_Partition'  % db, '%s_Partition_Limit22'  % db, 
			'%s_Subpartition'  % db,'%s_Subpartition_Limit33'  % db,'%s_ShardedSubpartition'  % db, '%s_ShardedTable'  % db, '%s_ShardedPartition'  % db, 
			'%s_QueryFile'  % db,'%s_QueryFile_Limit100'  % db,'%s_QueryDir'  % db, '%s_QueryDir_Limit333'  % db, '%s_ShardedQuery'  % db]
			
		#if db in ('MARIA'):
		#	return ['MARIA_Table', 'MARIA_Partitioned', 'MARIA_SubPartitioned','MARIA_ShardedSubPartitioned', 'MARIA_ShardedTable', 'MARIA_ShardedPartitioned', 'MARIA_Query','MARIA_ShardedQuery']
		if db in ('ORA11G','EXAD'):
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
	def get_to(self, db):
		if db in ('CSV'):
			return ['CSV_Default', 'CSV_File','CSV_Dir']
		elif db in self.conf.dbs.keys():
			return [db]
		else:
			assert 1==2, 'get_to() is not defined for db: %s' % db	
	def get_to_dbs(self,dbs):
		out=[]
		for db in dbs:
			out=out+self.get_to(db)
		return out	
	def get_distpath(self, rs):
		return (os.sep).join(self.dmhome.split(os.sep)[:-1]+['%s_dist_%s\\%s' % (self.conf.appn,rs,self.rts.replace('/','.').replace(' ','_').replace(':','.'))])	
	def get_appn(self, relc):
		return '%s%s' % (self.conf.appn,relc[0])	
	def get_exe_name(self, relc):
		distpath=self.get_distpath(relc[0])
		appn=self.get_appn(relc)
		return os.path.join(distpath,appn,'%s.%s' % (appn,self.conf.appex))	
	def zip_dir(self, zipname, dir_to_zip):
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
	def exec_cmd(self, shcmd):
		print shcmd
		p = Popen(shcmd,  stdout=PIPE , shell=True ) # '-S',  stdin=p1.stdout,
		out, err = p.communicate()	
		print out
		print err
		if err:
			print 'ERROR:', err	
		return (out,err)
	def save_txt(self,exefn,opt,txtn):	
		exedir=os.path.dirname(exefn)
		fn = os.path.basename(exefn)
		cmd=[r'%s' % exefn]+opt
		#pprint(shlex.split(cmd))
		(out, err) = self.exec_cmd(cmd)
		#print out 
		#print err
		
		out=out.replace('\r\n','\n')
		self.fsave(os.path.join(exedir,'%s.txt' % txtn),'##\n##%s %s \n##\n%s' % (fn,' '.join(opt),out))
	def get_txt(self, exefn,opt,txtn):	
		exedir=os.path.dirname(exefn)
		fn = os.path.basename(exefn)
		cmd=[r'%s' % exefn]+opt
		#pprint(shlex.split(cmd))
		(out, err) = self.exec_cmd(cmd)
		#print 'out',out 
		#print 'out',err
		#print 'fn',fn
		
		out=out.replace('\r\n','\n')
		print '##\n##%s %s \n' % (fn,' '.join(opt)),out
		#e(0)
		return ('##\n##%s %s \n' % (fn,' '.join(opt)),out)	
	def get_distpath(self,rs):
		return (os.sep).join(self.dmhome.split(os.sep)[:-1]+['%s_dist_%s\\%s' % (self.conf.appn,rs,self.rts.replace('/','.').replace(' ','_').replace(':','.'))])
	def zip_dir(self, zipname, dir_to_zip):
		dir_to_zip_len = len(dir_to_zip.rstrip(os.sep)) + 1
		with zipfile.ZipFile(zipname, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
			for dirname, subdirs, files in os.walk(dir_to_zip):
				if not '\\logs\\' in dirname:
					for filename in files:
						path = os.path.join(dirname, filename)
						entry = path[dir_to_zip_len:]
						zf.write(path, entry)	
		#e(0)