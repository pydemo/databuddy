import types, re, os, sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
from pprint import pprint
class Mysql(base):
	"""SQLServer db"""
	def __init__(self,log,ss_user, ss_passwd, ss_db_name, ss_db_server,datadir):
		base.__init__(self, log)
		self.log=log
		self.ss_user=ss_user
		self.ss_passwd=ss_passwd
		self.ss_db_name=ss_db_name
		self.ss_db_server=ss_db_server
		self.datadir=datadir
		self.tab_cols={}
		self.ctldir='%s/sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir) 
	

	def get_query_columns(self, qry):
		#if self.tab_cols.has_key(tab_name):
		#	return self.tab_cols[tab_name]
		if 0:
			pass
		else:
			qry="""SELECT * FROM (%s) p WHERE 1=2;""" % qry.strip().strip(';')
			#print qry
			#sys.exit(0)
			cqfn=self.save_qry('get_query_columns',qry)
			#print cqfn
			(r_int, status)=self.do_query2(self.log,self.login, query=None,query_file=cqfn,column_type_info=True)
			#pprint(r_int)
			
			cols =  r_int[0].split('\t')
			#print cols
			#sys.exit(0)
			return cols
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

	def do_query(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
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
			if 0: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				q = "%s%s" % ( query_file,'show warnings;')
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
				conf=[ mysqlloc ,'-u', ss_user, '-p%s' % ss_passwd,'-D',ss_db_name, '-h', ss_db_server,'-N', '-B']
				#pprint(conf)
				#print regexp
				
				#sys.exit(1)
				p2 = Popen(conf,stdin=PIPE,  stdout=PIPE, stderr=PIPE) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				#out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				
				output, err = p2.communicate(q)
				#print out
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				#output=' '
				status=0
				er='none.'
				#print type(out)
				#pprint(out.split('\n'))
				#sys.exit(1)

				if err:
					if 'Warning: Using a password on the' in err:
						logger.warn(err)
					else:
						logger.error(err)							
							
				for o in output.split('\n'):
				#while output:
					#output = p2.stdout.readline()
					#print output
					#if o.strip():					
					#	logger.info( output.strip())
					if 1:
						if regexp:
							#print regexp, o
							
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
							#if show:
							#	print output.strip()
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
				#output, err = p2.communicate('show warnings;')
				#print output, err
				pstatus=p2.wait()

				if int(status)+int(pstatus)>0:
					print 'error', status,pstatus
					#self._logger.error(string.join(err,'\n'))	
				if status!=0:
					return (err,status)
				#print "====================", out,status
				return (out,status+pstatus, err)					
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