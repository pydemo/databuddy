import sys
import datetime
import imp
from build_common import common_build
from pprint import pprint
e=sys.exit

class build(common_build):
	"""db2db Data Migrator."""
	def __init__(self,dmhome,from_dbs,to_dbs, app, regs, v, is_release,nor_t):
		#self.for_dbs=for_dbs
		self.from_dbs=from_dbs
		self.to_dbs=to_dbs
		self.app=app
		self.regs=regs
		self.v=v
		self.is_release=is_release
		self.nor_t=nor_t
		self.dmhome=dmhome
		import __builtin__
		__builtin__.copy_vector = copy_vector
		import common.v101.config as conf
		self.conf=conf
		import release as rel 	
		self.rel=rel
		from test import run_test, create_run_tests,  home, citi
		
		self.test={}
		self.create_run_tests=create_run_tests
		self.run_test=run_test
		self.home=home
		self.citi=citi
		self.ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		self.rts=self.get_dir_from_ts(self.ts)
	def save_release(self,relc,app_author,apptitle,appn,tests,bname):
		bin,version, ts = relc
		incname = bname.replace('build_','include_')
		relcfg="""# release setup
free='#FreeUkraine #SaveUkraine #StopRussia #PutinKhuilo #CrimeaIsUkraine'
bin='%s'
version='%s'
ts='%s'
for_db=%s
from_to_dbs=%s
release=%s
app_author='%s'
apptitle='%s'
appn='%s'
appex='exe'
appname='%s'
tests=%s
ucases=None
import __builtin__
__builtin__.for_db = for_db
__builtin__.from_to_dbs=from_to_dbs
__builtin__.free=free
__builtin__.apptitle=apptitle
__builtin__.version=version
__builtin__.bin=bin
__builtin__.appname=appname
__builtin__.release=release
import test.v101.build_include.%s as inc
def get_ucases():
	return ucases
def show_default_help():
	inc.show_default_help(for_db, from_to_dbs,appname,dbs)
def supported(x):
	return inc.supported(x, for_db, from_to_dbs)
def getAppTitle():
	return inc.getAppTitle(for_db, apptitle,dbs)
def getExeTitle():
	return inc.getExeTitle(apptitle, for_db, bin, dbs)	
def show_help(cvarg,copy_vector,params):
	inc.show_help(for_db,from_to_dbs,dbs,cvarg,copy_vector,params,ucases)

""" % ( bin,version, ts,self.for_db,self.from_to_dbs,self.is_release,app_author,apptitle,appn, '%s%s.exe' % (appn,bin), tests,incname.split('.')[0])
		#print relcfg
		#e(0)
		fn=os.path.join(self.dmhome,'release.py')
		self.fsave(fn,relcfg)
		os.remove(os.path.join(self.dmhome,'release.pyc'))
		
		py_compile.compile('release.py')
		print 'release saved'	
		#(bin,version, rts) = relc 
		#e(0)		
	def build_and_release(self):
			
		(app_author, apptitle, appn)=self.app
		from_tst=[]
		tests=[]
		if not self.is_release:
			########
			from_db_tests,to_db_tests= self.nor_t
			#from_db_tests,to_db_tests =None, None
			#if self.for_dbs:
			#	from_db_tests =['MYSQL_Table']
			#	to_db_tests=['MYSQL']
			########
		else:			

			self.create_run_tests(self.from_dbs[0], self.to_dbs[0],  self.test, self.citi)
			from_db_tests= [x for x in self.test['FROM'].keys() if x.startswith('%s_' % self.from_dbs[0])]
			#from_db_tests = self.get_from_dbs(self.from_dbs)
			print from_db_tests
			
			to_db_tests =  [x for x in self.test['TO'].keys() if x.startswith('%s_' % self.to_dbs[0])]
			assert self.to_dbs, 'to_db_tests is not set' 
			assert self.from_dbs, 'from_db_tests is not set'
			#print to_db_tests, from_db_tests
			#e(0)
			#print from_dbs[0],to_dbs[0]
			#e(0)
			#if self.from_dbs[0]==self.to_dbs[0]:
			#	tests.append([from_db_tests,to_tst])
			#	tests.append([from_db_tests,to_tst])
			#else:
		tests.append([from_db_tests,to_db_tests])
		#print self.test['TO'].keys()
		#print to_db_tests
		#print tests
		
		#e(0)			
		#ts=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		#rts=self.get_dir_from_ts(ts)	
		#pprint(tests)
		#e(0)
		for rs in self.regs:
			relc=(rs, self.v, self.ts)
			self.save_release(relc,app_author,apptitle,appn,tests)
			self.append_release("getAppTitle = lambda: '"+self.conf.dbs[self.from_dbs[0]] +" to "+self.conf.dbs[self.to_dbs[0]] +" %s' % (apptitle)")	
			self.append_release("app_descr='Command line tool for "+self.conf.dbs[self.from_dbs[0]] +" data replication to "+self.conf.dbs[self.to_dbs[0]] +" database.'")			
			self.append_release("supported = lambda x : x[0] in from_dbs and x[1] in to_dbs ")				
			imp.reload(self.rel)
			imp.reload(self.conf)
			
			self.conf.setreg(rs)
			self.set_prog(relc)
			#e(0)

			if self.is_release:
				exefn= self.build_project(relc)
				#e(0)
				cmd=[]

				ucases=self.set_tests_dbs(relc,cmd,tests)
				
				#print len(ucases)
				#e(0)
				exe_tests=self.create_exe_tests(rs,cmd,exefn)
				
				self.release_ucon(relc,exefn)
				print 'after ru'
				#e(0)
				self.run_all_exe_tests(exe_tests,exefn)
				#e(0)
				self.release_exe(relc,exefn, ucases)
				print exefn
			else:
				cmd=[]
				#print to_db_tests,from_db_tests
				#e(0)
				ucases=self.set_tests(relc, cmd,to_db_tests,from_db_tests)
				py_tests=self.create_tests(rs,cmd)
				#print conf.release
				
