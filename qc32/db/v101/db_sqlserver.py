import types, re, os, dbi
import sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
from pprint import pprint
e=sys.exit
class SQLServer(base):
	"""SQLServer db"""
	def __init__(self,log,login ,datadir,args):
		base.__init__(self, log)
		self.log=log
		self.login=login
		#(self.ss_user, self.ss_passwd, self.ss_db_name, self.ss_db_server) = login
		#self.ss_user=ss_user
		#self.ss_passwd=ss_passwd
		#self.ss_db_name=ss_db_name
		#self.ss_db_server=ss_db_server
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		self.to_pld={}
		self.db_client_loc=None	
		self.db_client_dbshell=None	
		self.db_client_loader=None
		self.dbg=0
		if args.debug_level:
			self.dbg=int(args.debug_level)		
	
	def get_spool_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		#if not os.path.isdir(datdir):
		#	os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)	
		
	def get_date_format(self):
		nls_df = NLS_DATE_FORMAT
		if not nls_df:
			nls_df = 'DD-MON-RR HH.MI.SS AM'
		nls_tf = NLS_TIMESTAMP_FORMAT
		if not nls_tf:
			nls_tf = 'DD-MON-RR HH.MI.SSXFF AM'	
		return ('DD/MM/RRRR','DD/MM/RRRR HH.MI.SSXFF AM')

		
	def get_log_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		if not os.path.isdir(datdir):
			os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)
	def get_spool_fn(self,dir,ext,tab):
		fexists=0
		if 0: #self.is_set('OUTPUT_FILE'):
			outf = self._pp['OUTPUT_FILE']
			if os.path.isfile(outf):
				fexists=1
				#self._logger.warn('OUTPUT_FILE does not exists.')
			return (outf	,fexists)
				
			
		datdir= '%s/%s' % ('logs',dir)
		gzfn=None
		#if not os.path.isdir(datdir):
		#	os.mkdir(datdir) 	
		#if self.p_if('IF_COMPRESSED_SPOOL'):
		#	ext='gz'
		gzfn = '%s/%s.%s.%s' % (datdir,'test_worker',tab,ext)
		if 0: #self.is_set('PARTITION'):
			gzfn = '%s/%s.%s.%s.%s' % (datdir,self._pp['WORKER_NAME'],tab,self._pp['PARTITION'],ext)
		return (gzfn,fexists)		

	def ckey2cols(self, col_key):
		return map(lambda x: x.split(':')[0],col_key)
	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
		

	def do_query2(self, login, query, query_file=None, regexp=None, grp=None, spset=''):
		f = ""
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(login)>0, 'Default login is not set.'
		show=False
		if type(login) == types.TupleType:
			to_tab=login[1]
			login=login[0]
			#query = string.replace ()
			#sys.exit(1)
		else:
			pass
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''

			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q = "%s\n%s\n%s" % ( spset,opt,query)
				#q = "%s" % ( query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q,'<'
			p1 = Popen(['echo', q.replace('\n','')], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				while output:
					output = p1.stdout.readline()
					print output
				sys.exit(0)
			p2 = Popen([ 'sqlplus', "-S", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE)
			output=' '
			status=0
			while output:
				output = string.replace(p2.stdout.readline(),'SQL>','')
				#print output
				#err.append(output)
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
						#print output,
						self._logger.info(output.rstrip())	
				if errpos>-1:
					self._logger.error(output.rstrip())	
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

	def get_ctl_filler(self, to_tab, r_int, dpl_mode, term):
		(line_term,field_term) =term
		part = ''
		if 0:
			if self.is_set('PARTITION'):
				if self._pp.has_key('TO_PARTITION'):
					to_part = self._pp.get('TO_PARTITION')
					if to_part:
						part = 'PARTITIOn (%s)' % to_part
					else:
						pass
				else:
					part = 'PARTITION (%s)' % self.p('PARTITION')
			unrec = ''
			if self.p_if('IF_UNRECOVERABLE'):
				unrec = 'UNRECOVERABLE'	
		unrec = 'UNRECOVERABLE'				
		tmpl="""%s
	LOAD DATA
	INFILE '-' "str '%s\n'"
	%s
	INTO TABLE %s %s
	FIELDS TERMINATED BY '%s'
	TRAILING NULLCOLS
	(C_FILLER FILLER,
	 %s)""" % (unrec,line_term,dpl_mode,to_tab, part, field_term, ','.join(r_int))
		#pprint(tmpl)
		#pprint(r_int)
		#sys.exit(1)
		return tmpl	

	def save_ctl(self, to_table,shard):
		ptn=''
		sptn=''
		cols = self.get_table_columns(to_table)
		dpl_mode='APPEND'
		line_term=''
		ctl=self.get_ctl(to_table,cols,dpl_mode,(line_term,'|'))

		ctlfn= '%s/%s%s%s.ctl' % (self.ctldir,to_table, "%s%s" % (ptn,sptn),shard)


		f = codecs.open(ctlfn, 'w',"utf-8")
		status = f.write(unicode(ctl))

		if status!= None:
			self._logger.error('Cannot write to %s.' % ctlfn)
		f.close()
		return 	ctlfn	
	
	def get_ctl(self, to_tab, r_int, dpl_mode, term):
		(line_term,field_term) =term
		part = ''
		if 0:
			if self.is_set('PARTITION'):
				if self._pp.has_key('TO_PARTITION'):
					to_part = self._pp.get('TO_PARTITION')
					if to_part:
						part = 'PARTITIOn (%s)' % to_part
					else:
						pass
				else:
					part = 'PARTITION (%s)' % self.p('PARTITION')
			unrec = ''
			if self.p_if('IF_UNRECOVERABLE'):
				unrec = 'UNRECOVERABLE'	
		unrec = 'UNRECOVERABLE'	#INFILE '-' "str '%s\n'"			
		tmpl="""%s
	LOAD DATA
	%s
	INTO TABLE %s %s
	FIELDS TERMINATED BY '%s'
	TRAILING NULLCOLS
	(%s)""" % (unrec,dpl_mode,to_tab, part, field_term, ','.join(r_int))
		#pprint(tmpl)
		#pprint(r_int)
		#sys.exit(1)
		return tmpl
	def get_query_columns(self,log,login,  qry):
		self.log.info('Fetching query columns...')

		regexp=re.compile(r'([\w\d\|\_\@\#\$]+)')
		qry='SELECT * FROM (%s) t WHERE 1=2' % qry
		#print qry
		#sys.exit(0)
		qfn=self.save_qry('get_query_columns',qry)
		(r, status,err)=self.do_query(log,login, query=None,query_file=qfn,regexp=regexp,with_col_names=True)

		#assert not status, 'Table %s doesn\'t exist in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login))
		assert len(r), 'Cannot fetch table %s columns.' % t
		self.log.info('Done.')
		return (r[0][0].split('|'),status)
	def get_table_columns(self,log,login,  tab):
		self.log.info('Fetching table columns...')

		regexp=re.compile(r'([\w\d\|\_\@\#\$]+)')
		qry='SELECT * FROM %s t WHERE 1=2' % tab
		#print qry
		#sys.exit(0)
		qfn=self.save_qry('get_table_columns',qry)
		(r, status,err)=self.do_query(log,login, query=None,query_file=qfn,regexp=regexp,with_col_names=True)

		assert not status, 'Table %s doesn\'t exist in %s.' % ('.'.join(t), re.sub('\/(.*)\@', '/***@', login))
		assert len(r), 'Cannot fetch table %s columns.' % t
		self.log.info('Done.')
		return (r[0][0].split('|'),status)	
	def do_query_old(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
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
			#p1 = Popen(['print',  q], stdout=PIPE,stderr=PIPE)
			output=' '
			status=0
			if 0:
				while output:
					output = string.replace(p1.stdout.readline(),'SQL>','')
					#print output
				return ([],0)				
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				db_client_dbshell= self.get_db_client_dbshell()
				#print db_client_dbshell
				conf=[ 'sqlcmd','-h','-1','-Q',q,'-s',field_term,'-W','-U', ss_user, '-P', ss_passwd,'-d',ss_db_name, '-S', ss_db_server]
				#print(q)
				#print ' '.join(conf)
				#print ss_db_server
				
				#sys.exit(1)
				
				p2 = Popen(conf,stdin=PIPE,  stdout=PIPE , stderr=PIPE ) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				output=' '
				status=0
				er='none.'
							
				while output:
					output = p2.stdout.readline()
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

				er='none.'
				if 1:
					while er:
						er = p2.stderr.readline()
						if er.strip():
							logger.error(er)				
				status=p2.wait()
				
				#print "====================", out,status
				return (out,status)	

	def do_query(self,logger,login, query, query_file=None, regexp=None, grp=None, spset='',field_term='|', with_col_names=False):
		f = ""
		(ss_user,ss_passwd, ss_db_name, ss_db_server)=login
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
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q =  query # "%s\n%s\n%s" % ( spset,opt,query)

			output=' '
			status=0
			if 0:
				while output:
					output = string.replace(p1.stdout.readline(),'SQL>','')
					#print output
				return ([],0)				
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				db_client_dbshell= self.get_db_client_dbshell()
				#print db_client_dbshell
				cfg=[]
				if with_col_names:
					cfg=[ r'%s' % db_client_dbshell,'-h','1','-s','^%s' % field_term,'-W','-U', ss_user, '-P', ss_passwd,'-d',ss_db_name, '-S', ss_db_server]
				else:
					cfg=[ r'%s' % db_client_dbshell,'-h','-1','-s','^%s' % field_term,'-W','-U', ss_user, '-P', ss_passwd,'-d',ss_db_name, '-S', ss_db_server]
				#print(cfg)
				#print ' '.join(cfg)
				p2 = Popen(cfg,stdin=PIPE,  stdout=PIPE, shell=True ) # '-S',  stdin=p1.stdout,
				(output, err) = (None, None)
				if query_file:
					#print query_file
					q=file(query_file).read()
					#print q
					output, err = p2.communicate(q)
				else:
					output, err = p2.communicate(q)
				#print output
				#print err
				#e(0)
				grp=None
				out=[]
				status=p2.wait()
				#sys.exit(0)
				if err:
					print '#'*60
					print '#'*60				
					print output
					self.log.error(err)
					print '#'*60
					print '#'*60				
					
				for o in output.split('\r'):
					if regexp:
						#print regexp, o
						#pprint(dir(re))
						m = re.match(regexp, o.strip()) 
						#print m
						if m:
							if grp:
								out.append(m.group(grp))
							else:
								groups=m.groups()
								if groups:
									#print 'groups', groups
									out.append(groups)
												
					
				#print out
				#if query_file:
				#	sys.exit(1)					
				#sys.exit(0)
				return (out,status,err)	
				