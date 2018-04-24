import sys
import datetime
import imp
from build_common import common_build
e=sys.exit
class build(common_build):
	"""CSV*Extractor."""
	def __init__(self,dmhome,for_dbs,from_dbs,to_dbs, app, regs, v, is_release,nor_t):
		self.for_dbs=for_dbs
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
	def build_and_release(self):
			
		(app_author, apptitle, appn)=self.app
		from_tst=[]
		tests=[]
		if not self.is_release:
			########
			from_tst,to_tst= self.nor_t
			from_db_tests,to_db_tests =None, None
			#if self.for_dbs:
			#	from_db_tests =['MYSQL_Table']
			#	to_db_tests=['MYSQL']
			########
		else:			
			if not self.from_dbs:
				from_tst=get_from_ALL()
			else:
				if 1:
					from_tst=self.get_from_dbs(self.from_dbs)
				else:
					#pprint(from_tst)
					#print self.test
					self.create_run_tests(self.from_dbs[0], self.to_dbs[0],  self.test, self.citi)
					from_tst= [x for x in self.test['FROM'].keys() if x.startswith('%s_' % self.from_dbs[0])]
					#e(0)
			if not self.to_dbs:
				to_tst=get_to_ALL()	
			else:
				#print self.to_dbs
				#e(0)
				to_tst=self.get_to_dbs(self.to_dbs)
			if self.for_dbs:
				from_db_tests = self.get_from_dbs(self.for_dbs)
				to_db_tests = self.get_to_dbs(self.for_dbs)
		if to_db_tests and from_db_tests:
			#print from_dbs[0],to_dbs[0]
			#e(0)
			if self.from_dbs[0]==self.to_dbs[0]:
				tests.append([from_db_tests,to_tst])
				tests.append([from_db_tests,to_tst])
			else:
				tests.append([from_db_tests,to_tst])
		else:
			tests.append([from_tst,to_tst])
		
		for rs in self.regs:
			relc=(rs, self.v, self.ts)
			self.save_release(relc,app_author,apptitle,appn,tests)
			self.append_release("getAppTitle = lambda: '%s for "+self.conf.dbs[self.from_dbs[0]] +"' % (apptitle)")	
			self.append_release("app_descr='Command line tool for CSV data extraction from "+self.conf.dbs[self.from_dbs[0]] +" database.'")			
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
				self.append_release("ucases=%s" % str(ucases))
				#print len(ucases)
				#e(0)
				exe_tests=self.create_exe_tests(rs,cmd,exefn)
				
				self.release_ucon(relc,exefn)
				#e(0)
				self.run_all_exe_tests(exe_tests,exefn)
				#e(0)
				self.release_exe(relc,exefn, ucases)
				print exefn
			else:
				cmd=[]
				ucases=self.set_tests(relc, cmd,to_tst,from_tst)
				py_tests=self.create_tests(rs,cmd)
				#print conf.release
