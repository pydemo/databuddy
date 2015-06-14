#__builtin__ args
import sys, os
from pprint import pprint
from common.v101.base import base 
e=sys.exit
#
# Define your custom load query
#	
class common(base):
	"""Common Oracle methods"""
	def __init__(self,datadir,login,conf):
		self.datadir=datadir
		self.login=login
		self.conf=conf
		#self.db=db
		self.args=conf.args
		self.cr={} #code_release(self.conf, self.args)
		host_map_loc= self.args.host_map
		#print host_map_loc
		#self.hm = hmap.host_map(self.args.copy_vector.split(self.conf._to),host_map_loc,0)
	def do_query21(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|', column_type_info=False):
		f = ""
		#print conf
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
				
class target(common):
	"""Target Oracle methods"""
	def __init__(self,log,datadir,login,conf,db,to_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		self.conf=conf
		self.log=log
		self.db=db.upper()
		self.to_table=to_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir)
		#self.cr={} #code release
	def get_load_query(self, infile):
		global args
		skip=''
		if args.skip_rows:
			skip='SKIP %d' % args.skip_rows

		out ="""INPUT INTO "%s"  DELIMITED BY '%s'  FROM '%s' %s ;\nexit;\n""" % (args.to_table, args.field_term,infile,skip)
		#pprint(out)
		return out
			
class source(common):
	"""Source Oracle methods"""
	def __init__(self,log,datadir,login,conf,db,from_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		self.conf=conf
		self.log=log
		self.db=db
		self.from_table=from_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
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
	def get_table_columns(self, tab):
		#if self.tab_cols.has_key(tab_name):
		#	return self.tab_cols[tab_name]
		if 0:
			pass
		else:
			qry="""SELECT * FROM %s p """ % tab.strip().strip(';')
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
			