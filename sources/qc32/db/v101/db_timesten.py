import types, re, os, sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
from pprint import pprint
import shlex
e=sys.exit
class TimesTen(base):
	"""TimesTen db"""
	def __init__(self,log,login,datadir,args):
		base.__init__(self, log)
		self.log=log
		self.login=login
		
		self.field_term=args.field_term
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		self.to_pld={}
		self.db_client_loc=None	
		self.db_shell_path=None		
		#self.ctldir='%s/sqlloader' % self.datadir
		
		#if not os.path.isdir(self.ctldir):
		#	os.makedirs(self.ctldir) 
		self.dbg=0
		if args.debug_level:
			self.dbg=int(args.debug_level)	
	

	def get_query_columns_0(self, qry):
		#if self.tab_cols.has_key(tab_name):
		#	return self.tab_cols[tab_name]
		if 0:
			pass
		else:
			qry="""set columnlabels on echo off feedback off serveroutput  off timing off\nSELECT * FROM (%s) p WHERE 1=2;""" % qry.strip().strip(';')
			#print qry
			#sys.exit(0)
			cqfn=self.save_qry('get_query_columns',qry)
			#print cqfn
			(r_int, status,err)=self.do_query(self.log,self.login, query=None,query_file=cqfn)
			#pprint(r_int)
			
			#cols =  r_int[0].split('\t')
			#print r_int
			#sys.exit(0)
			return (r_int,status)
			
	def get_query_columns(self, qry):
		#if self.tab_cols.has_key(tab_name):
		#	return self.tab_cols[tab_name]
		if 0:
			pass
		else:
			qry="""set columnlabels on echo off feedback off serveroutput  off timing off\ndesc %s;""" % qry.strip().strip(';')
			#print qry
			#sys.exit(0)
			cqfn=self.save_qry('get_query_columns',qry)
			#print cqfn
			regexp=regexp=re.compile(r'\s+([\w]+)\s+([\w]+)(.*)\s+')
			(r_int, status,err)=self.do_query(self.log,self.login, regexp=regexp,query=None,query_file=cqfn)
			#pprint(r_int)
			
			#cols =  r_int[0].split('\t')
			#print r_int
			#sys.exit(0)
			cols=[':'.join(x) for x in r_int]
			#print cols
			#e(0)
			return (r_int,status)	
			
	def do_query(self,logger,login, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
		f = ""
		(db_user,db_passwd, db_DSN)=login
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(login)>0, 'Default login is not set.'
		show=False
		#field_term='|'
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''
			if 0: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				assert os.path.isfile(query_file),'Query file %s is missing' % query_file
			#	q = "%s%s" % ( query_file,'show warnings;')
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:
				q =  query # "%s\n%s\n%s" % ( spset,opt,query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q
			#sys.exit(0)
			#p1 = Popen(['C:\\Python27\\data_mule_mysql\\spool_test.sql'], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				pass
			else: #,'-q','"%s"' % q
				db_shell_path=self.get_db_shell_path()
				
				connect_str= '"DSN=%s;UID=%s;PWD=%s"' % (db_DSN, db_user,db_passwd)
				
				cfg=['"%s"' % db_shell_path, '-connstr',connect_str,'-v','1']
				if query_file:
					cfg=cfg+ ['-f', r'"%s"' % query_file]	
					q=''					
				#conf=[ pgloc ,'-U', self.args.from_user,'-d',self.args.from_db_name]
				#pprint(conf)
				#print q 
				#sys.exit(0)
				#print regexp
				#print login
				#raise
				#set PGPASSWORD=self.args.from_passwd
				#os.environ['PGPASSWORD'] = pg_passwd
				#q='exit;'
				#q='select count(*) from Persons_pipe_datetime;'
				#print q
				#select 'ROW COUNT:' filter ,count(*) cnt from (SELECT * FROM     Persons_pipe_datetime) as t;
				#pprint (cfg)
				cmd=  ' '.join(cfg)
				if 0:
					cmd=  ' '.join(cfg)
					#print cmd
					#			
					#print q
					lexer=shlex.shlex(cmd)
					lexer.quotes = '"'
					lexer.whitespace_split = True
					lexer.commenters = ''
					cmdList = list(lexer)
				
				cmdList=shlex.split(cmd)
				#pprint(cmdList)
				#sys.exit(1)
				p2 = Popen(cmdList,stdin=PIPE,  stdout=PIPE,  shell=True) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				#out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				#print q
				#if not query_file:				
				output, err = p2.communicate("set rowdelimiters off;%s\n; exit;\n" % q)
				#pprint( output)
				#sys.exit(1)
				#select table_name, column_name from SYS.ALL_COL_PRIVS where table_name=upper('Persons_pipe_datetime')
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				#output=' '
				status=0
				er='none.'
				#print type(out)
				#pprint(out.split('\n'))
				#pstatus=p2.wait()
				#sys.exit(1)
				#pprint (os.sep) 
				#sys.exit(1)
				if err:
					if 'Warning: Using a password on the' in err:
						logger.warn(err)
					else:
						logger.error(err)							
					
				
				if regexp:
					for o in output.split('\n'):
					#while output:
						#output = p2.stdout.readline()
						#print '---',o

						#print regexp, o
						#pprint(dir(re))
						m = re.match(regexp, o) 
						#print m
						if m:
							if grp:
								out.append(m.group(grp))
							else:
								groups=m.groups()
								if groups:
									#if groups[0]:
										#print 'groups', groups
									out.append(groups)
				else:
					 out =output.split(os.sep)

				pstatus=p2.wait()

				#print out,status+pstatus, err
				#print out
				#sys.exit(1)
				return (out,status, err)	
				
	def do_query2(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|', column_type_info=False):
		f = ""
		(ss_user,ss_passwd, ss_db_name, ss_db_server)=conf
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(conf)>0, 'Default login is not set.'
		show=False
		#field_term='|'
		if 1:			
			#from subprocess import Popen, PIPE
			#q=''
			opt=''
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			#if query_file:
			#	q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			#else:		

			#	q =  query # "%s\n%s\n%s" % ( spset,opt,query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q
			#sys.exit(0)
			#p1 = Popen(['C:\\Python27\\data_mule_mysql\\spool_test.sql'], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				pass
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				#pprint(q)
				#print ss_db_server
				mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
				conf=[ mysqlloc ,'-u', ss_user, '-p%s' % ss_passwd,'-D',ss_db_name, '-h', ss_db_server]
				if column_type_info:
					conf.append('--column-type-info')
					
				#pprint(conf)
				#print regexp
				
				#sys.exit(1)
				p2 = Popen(conf,stdin=PIPE,  stdout=PIPE, stderr=PIPE  ) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				#out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				#print query
				(output, err) = (None, None)
				if query_file:
					#print 'query_file:',query_file
					output, err = p2.communicate(file(query_file).read())
					#print output, err
				else:
					#print 'query'
					output, err = p2.communicate(query)
				if err:
					if 'Warning: Using a password on the' in err:
						logger.warn(err)
					else:
						logger.error(err)
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				#output=' '
				status=0
				er='none.'
				#print type(out)
				#pprint(out.split('\n'))
				#pprint( output)
				#sys.exit(1)
				if regexp:
					for o in output.split('\n'):
					#while output:
						#output = p2.stdout.readline()
						#print output
						if o.strip():					
							logger.info( output.strip())

						if 1:
							
							m = re.match(regexp, o) 
							#print m
							if m:
								if grp:
									out.append(m.group(grp))
								else:
									groups=m.groups()
									if groups:
										if groups[0]:
											#print 'groups', groups
											out.append(groups[0])
									#self._logger.info(output.rstrip())
								#else out.append(m.group(grp))
						else:
							
							out.append(output)
							if show:
								print output.strip()
								#self._logger.info(output.rstrip())	
						if errpos>-1:
							#self._logger.error(output.rstrip())	
							status=1					
						#errpos=output.find('ERROR') 
						#print  output.find('2COLUMN.')
						if output.find('COLUMN.')==-1:
							errpos=output.find('ERROR ')
							#print "%s, %s ,%s" % (errpos, output, output.find('COLUMN.'))
							if errpos>-1:
								status=1
								
								#self._logger.error(output.rstrip())	
				else:
					out=output.strip().split('\n')
				pstatus=p2.wait()

				if int(status)+int(pstatus)>0:
					print 'error', status,pstatus
					#self._logger.error(string.join(err,'\n'))	
				if status!=0:
					return (err,status)
				#print "====================", out,status
				return (out,status+pstatus)		

				
	def do_query_spool(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
		f = ""
		(ss_user,ss_passwd, ss_db_name, ss_db_server)=conf
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(conf)>0, 'Default login is not set.'
		show=False
		#field_term='|'
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q =  query # "%s\n%s\n%s" % ( spset,opt,query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q
			#sys.exit(0)
			#p1 = Popen(['C:\\Python27\\data_mule_mysql\\spool_test.sql'], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				pass
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				#pprint(q)
				#print ss_db_server
				mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
				conf=[ mysqlloc ,'-u', ss_user, '-p%s' % ss_passwd,'-D',ss_db_name, '-h', ss_db_server]
				#pprint(conf)
				#sys.exit(1)
				p2 = Popen(conf,stdin=PIPE,  stdout=PIPE  ) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				#print out
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				output=' '
				status=0
				er='none.'
				if 1:
					while er:
						er = p2.stderr.readline()
						if er.strip():
							
							if 'Warning: Using a password on the' in er:
								logger.warn(er)
							else:
								logger.error(er)
							
				while output:
					output = p2.stdout.readline()
					#print output
					if output.strip():					
						logger.info( output.strip())
					if 1:
						if regexp:
							#print regexp
							m = re.match(regexp, output) 
							if m:
								if grp:
									out.append(m.group(grp))
								else:
									groups=m.groups()
									if groups:
										if groups[0]:
											out.append(groups)
									#self._logger.info(output.rstrip())
								#else out.append(m.group(grp))
						else:
							out.append(output)
							if show:
								print output.strip()
								#self._logger.info(output.rstrip())	
						if errpos>-1:
							#self._logger.error(output.rstrip())	
							status=1					
						#errpos=output.find('ERROR') 
						#print  output.find('2COLUMN.')
						if output.find('COLUMN.')==-1:
							errpos=output.find('ERROR ')
							#print "%s, %s ,%s" % (errpos, output, output.find('COLUMN.'))
							if errpos>-1:
								status=1
								
								#self._logger.error(output.rstrip())	
				
				pstatus=p2.wait()
				#print 'status:', pstatus
				er='none.'
				if pstatus:
					while er:
						er = p2.stderr.readline()
						if er:
							print 'P2-ERROR: ',er
					
				if int(status)+int(pstatus)>0:
					print 'error', status,pstatus
					#self._logger.error(string.join(err,'\n'))	
				if status!=0:
					return (err,status)
				#print "====================", out,status
				return (out,status+pstatus)					