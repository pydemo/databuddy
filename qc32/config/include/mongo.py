#__builtin__ args
import sys, os
from pprint import pprint
from common.v101.base import base 
import re, types, os, codecs
from subprocess import Popen, PIPE,STDOUT
import yaml
e=sys.exit
import Crypto
#sys.modules['Crypto'] = crypto
import paramiko
import zipfile
import datetime
#from config.include.ssh_file import  SSHConnection
import shutil
import re
import pprint as pp
import errno
from common.v101.exceptions import RowCountError
import imp
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod
	
d=os.path.split(os.path.split(os.path.dirname( __file__))[0])[0]
#os.chdir(d)
#print '##########',os.getcwd()
#from include.v101.host_map import host_map as hmap
hmap=import_module(os.path.join(d,'include','v101','host_map.py'))
#hmap= hmap.host_map
class code_release(object):
	"""Code Release object"""
	def __init__(self,log,parent,conf, args, spConf, shard):
		self.log=log
		self.parent=parent
		self.conf=conf
		self.args=conf.args
		self.spConf=spConf
		home=self.conf.home
		self.log_dir=self.conf.datadir
		ts= self.conf.ts
		self.R=False #if remote exec
		self.S=False #if source 
		if self.parent.__class__.__name__ in ['source']:
			self.S=True
		assert self.parent.__class__.__name__ in ['source', 'target'], 'Uknown parent class "%s"' % self.parent.__class__.__name__ 
		self.shard=shard
		#print  'shard %s' % self.shard
		#e(0)
		self.out_dir=os.path.join(self.log_dir,'out',ts,'Shard-%s' % shard)
		#print self.out_dir
		#e(0)
		self.remote_login={}
		self.remote_user='default'
		
		if hasattr(self.args, 'host_map') and self.args.host_map:
			
			host_map_loc= self.args.host_map
			hm = hmap.host_map(self.args.copy_vector.split(self.conf._to),host_map_loc,shard)
			
			
			if hm.R:
				self.R=True
				self.remote_login=hm.host['login']
				self.remote_user=self.remote_login[1]
				self.remote_home='/tmp/qctest/%s' % self.remote_user
				remote_home=self.remote_home
				self.remote_home_ts='%s/%s/%s' % (self.remote_home,ts,'Shard-%s' % shard)
				self.result_file='%s/spool.data' % self.remote_home_ts
				if hasattr(self.args, 'to_file') and self.args.to_file:
					self.result_file	= self.args.to_file		
			
			#print self.R
			#e(0)

			if self.R:			
				
				if not os.path.isdir(self.out_dir):
					#os.makedirs(self.out_dir)
					try:
						os.makedirs(self.out_dir)
					except OSError as exc: 
						if exc.errno == errno.EEXIST and os.path.isdir(self.out_dir):
							pass
							
				self.in_dir=os.path.join(self.log_dir,'in') #,'Shard-%s' % shard)
				if not os.path.isdir(self.in_dir):
					#print self.in_dir
					#print os.path.isdir(self.in_dir)
					#e(0)
					#os.mkdir(self.in_dir)
										
					try:
						os.makedirs(self.in_dir)
					except OSError as exc: 
						if exc.errno == errno.EEXIST and os.path.isdir(self.in_dir):
							pass
							
				run_fname=os.path.join(self.out_dir,'run.sh')	
				
				if self.S:	
					
					#print self.result_file
					#e(0)
					#print self.parent.__class__.__name__
					local_spooler_sql = self.spConf[-1].strip('@')
					assert os.path.isfile(local_spooler_sql), 'Local spooler sql does not exists.'
					spooler_name = os.path.basename(local_spooler_sql)
					out_spooler_sql= os.path.join(self.out_dir,spooler_name)
					shutil.copyfile(local_spooler_sql,out_spooler_sql)
					
					#client.connect('192.168.15.47', username='oracle', password='oracle123')
					
					self.sql_file='%s/%s' % (self.remote_home_ts,spooler_name)
					result_name=os.path.splitext(spooler_name)[0]
					

				#if self.S:
					#print run_fname
					#assert not os.path.isfile(run_fname), 'local run.sh already exists.'
					spooldir=os.path.dirname(self.result_file)
					#print spooldir
					#e(0)
					#print self.result_file
					#print '-->',spooldir
					#e(0)
					run="""		
LOG_FILE=log.txt
SPOOL_FILE=spool.data
function log {
echo $1    | tee -a ${LOG_FILE}
}
#create spool dir
if [ -e "%s" ]
then
    log "spool dir exists"
else
	mkdir %s
fi

cd %s
. ./.from_ora_profile
NLS_DATE_FORMAT='%s'
export NLS_DATE_FORMAT
NLS_TIMESTAMP_FORMAT='%s'
export NLS_TIMESTAMP_FORMAT
NLS_TIMESTAMP_TZ_FORMAT='%s'
export NLS_TIMESTAMP_TZ_FORMAT
START=$(date +%%s.%%N)
dt=`date`
log "Spool started at $dt" 
$ORACLE_HOME/bin/sqlplus -S $1 <<EOF
SET TRIMSPOOL ON
SET TERMOUT OFF
spool %s
@%s
spool off
exit;
EOF
END=$(date +%%s.%%N)
DIFF=$(echo "$END - $START" | bc)
RC=`echo $?`
dt=`date`
log "Spool finished at $dt"
log "Spool retcode = $RC" 
log "Elapsed (spool): $DIFF sec"

if [[ $RC != 0 ]] ; then
	log " Script failed: RDBMS exit code : $RC  " 
	cat ${SPOOL_FILE}                   | tee -a ${LOG_FILE}
	#cat ${LOG_FILE} | mail -s "Script failed" alex_buz@yahoo.com
	exit 3
fi

					""" % (spooldir, spooldir, self.remote_home_ts, self.args.nls_date_format, self.args.nls_timestamp_format, self.args.nls_timestamp_tz_format,  self.result_file, self.sql_file)
				
					
					#print run
					#e()
					with open(run_fname, 'wb') as file_:
						file_.write(run.replace(r'\r\n',r'\n'))			
				if not self.S:
					assert os.path.isfile(run_fname), 'local run.sh does not exists.'	
					#pprint (self.spConf)
					ctl_file_loc=self.get_local_loc(self.spConf,'control')
					ctl_file=os.path.basename(ctl_file_loc)
					#print ctl_file
					#print ctl_file_loc
					#e(0)
					#ctl_file='%s_Shard-%s.ctl' % (self.args.to_table,self.shard)
					#ctl_file_loc=os.path.join(self.parent.ctldir,ctl_file)
					assert os.path.isfile(ctl_file_loc), 'CTL file "%s" does not exists.' % ctl_file
					out_ctl_file_loc =  os.path.join(self.out_dir,'sqlloader')
					out_ctl_file =  os.path.join(out_ctl_file_loc, ctl_file)
					if not os.path.isdir(out_ctl_file_loc):
						os.mkdir(out_ctl_file_loc)
					shutil.copyfile(ctl_file_loc,out_ctl_file)
					r_ctl_file_loc='%s/sqlloader/%s' % (self.remote_home_ts, ctl_file)
					fname, ext =  os.path.splitext(ctl_file)
					r_log_file_loc='%s/sqlloader/%s.log' % (self.remote_home_ts, fname)
					r_bad_file_loc='%s/sqlloader/%s.bad' % (self.remote_home_ts, fname)
					r_dsc_file_loc='%s/sqlloader/%s.dsc' % (self.remote_home_ts, fname)
					keep_data_file='rm %s' % self.result_file
					if hasattr(args, 'keep_data_file') and args.keep_data_file:
						keep_data_file = ''
					
					
					run="""		
ls -al %s
. ./.to_ora_profile
NLS_DATE_FORMAT='%s'
export NLS_DATE_FORMAT
NLS_TIMESTAMP_FORMAT='%s'
export NLS_TIMESTAMP_FORMAT
NLS_TIMESTAMP_TZ_FORMAT='%s'
export NLS_TIMESTAMP_TZ_FORMAT
dt=`date`
START=$(date +%%s.%%N)
log "Load started at $dt" 
$ORACLE_HOME/bin/sqlldr control=%s userid=$2 DATA=%s LOG=%s BAD=%s DISCARD=%s BINDSIZE=200010 ERRORS=10 SKIP_UNUSABLE_INDEXES=TRUE COLUMNARRAYROWS=10000 DIRECT=TRUE STREAMSIZE=500000 READSIZE=200000 MULTITHREADING=TRUE SKIP_INDEX_MAINTENANCE=TRUE PARALLEL=TRUE
RC=`echo $?`
END=$(date +%%s.%%N)
DIFF=$(echo "$END - $START" | bc)
log "Load finished at $dt"
log "Load retcode = $RC" 
log "Elapsed (load): $DIFF sec."
log "cleanup"
SIZE=`du -b %s | awk '{print $1}'`
log "Spool file size ${SIZE}b"
%s

					""" % (self.result_file, self.args.nls_date_format, self.args.nls_timestamp_format, self.args.nls_timestamp_tz_format, r_ctl_file_loc,self.result_file, r_log_file_loc,r_bad_file_loc,r_dsc_file_loc, self.result_file, keep_data_file)
					with open(run_fname, 'ab') as file_:
						file_.write(run.replace(r'\r\n',r'\n'))	
					#print run
					#e(0)
				self.op_file_from=os.path.join(self.out_dir,'.from_ora_profile')
				
				if self.S:
					#source tnsnames.ora
					#print self.parent.db_client_dbshell
					admin_loc= os.path.join(os.path.dirname(self.parent.db_client_dbshell)[:-3],'network','admin')
					#print admin_loc
					tns_loc= os.path.join(admin_loc,'tnsnames.ora')
					assert os.path.isfile(tns_loc),'"tnsnames.ora" file is missing for loader\n%s' % self.parent.db_client_dbshell
					out_tns_dir =  os.path.join(self.out_dir,'tnsnames_from')
					if not os.path.isdir(out_tns_dir):
						os.mkdir(out_tns_dir)
					#e(0)
					out_tns_loc=os.path.join(out_tns_dir,'tnsnames.ora')
					shutil.copyfile(tns_loc,out_tns_loc)
					ora_home='/tmp/home/oracle/app/oracle/product/12.1.0/dbhome_1'
					#print hm.mapping
					#e(0)
					#tns_admin ='/home/oracle/app/oracle/product/12.1.0/dbhome_1/network/admin'
					tns_admin ='%s/tnsnames_from' % (self.remote_home_ts)
					ora_profile="""
ORACLE_HOME=%s
export ORACLE_HOME
#LD_LIBRARY_PATH=$ORACLE_HOME/lib;
#export LD_LIBRARY_PATH
PATH=$PATH:$ORACLE_HOME/bin;
export PATH
TNS_ADMIN=%s
export TNS_ADMIN
					""" % (ora_home,tns_admin)
					with open(self.op_file_from, 'wb') as file_:
						file_.write(ora_profile.replace(r'\r\n',r'\n'))
					#pprint(ora_profile)
				self.op_file_to=os.path.join(self.out_dir,'.to_ora_profile')
				if (not self.S):
					#source tnsnames.ora
					#print self.parent.db_client_dbshell
					admin_loc= os.path.join(os.path.dirname(self.parent.db_client_dbshell)[:-3],'network','admin')
					#print admin_loc
					tns_loc= os.path.join(admin_loc,'tnsnames.ora')
					assert os.path.isfile(tns_loc),'"tnsnames.ora" file is missing for loader\n%s' % self.parent.db_client_dbshell
					out_tns_dir =  os.path.join(self.out_dir,'tnsnames_to')
					if not os.path.isdir(out_tns_dir):
						os.mkdir(out_tns_dir)
					#e(0)
					out_tns_loc=os.path.join(out_tns_dir,'tnsnames.ora')
					shutil.copyfile(tns_loc,out_tns_loc)
					ora_home='/tmp/home/oracle/app/oracle/product/12.1.0/dbhome_1'
					#tns_admin ='/home/oracle/app/oracle/product/12.1.0/dbhome_1/network/admin'
					tns_admin ='%s/tnsnames_to' % (self.remote_home_ts)
					ora_profile="""
ORACLE_HOME=%s
export ORACLE_HOME
#LD_LIBRARY_PATH=$ORACLE_HOME/lib;
#export LD_LIBRARY_PATH
PATH=$PATH:$ORACLE_HOME/bin;
export PATH
TNS_ADMIN=%s
export TNS_ADMIN
					""" % (ora_home,tns_admin)
					#pprint(ora_home)
					with open(self.op_file_to, 'wb') as file_:
						file_.write(ora_profile.replace(r'\r\n',r'\n'))	
	def zip(self, src, dst):
		zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
		abs_src = os.path.abspath(src)
		for dirname, subdirs, files in os.walk(src):
			for filename in files:
				absname = os.path.abspath(os.path.join(dirname, filename))
				arcname = 'qctest/%s/%s/Shard-%s/' % (self.remote_user,self.conf.ts,self.shard) + absname[len(abs_src) + 1:]
				#print 'zipping %s as %s' % (os.path.join(dirname, filename), arcname)
				zf.write(absname, arcname)
			#zf.write('/%s/Shard-%s' % (self.conf.ts,self.shard))
		zf.close()
	
	def get_local_loc(self, dict, start):
		for l in dict:
			if l.startswith(start):
				return  l.split('=')[1].strip('"')
	def get_dist_name(self):
		return '%s_%s_%s_dist' % (self.remote_user,self.conf.ts, self.shard)
	def release(self):
		path_from =os.path.join(self.log_dir,'out',self.conf.ts,'Shard-%s' % self.shard)
		self.conf.datadir
		fname_to=self.get_dist_name()
		path_to=os.path.join(self.log_dir,fname_to)
		#origin='%s.zip' % path_to
		dst='/tmp/%s.zip' % ( fname_to)
		#print path_to
		#print path_from
		assert os.path.isdir(path_from), 'path_from does not exists.'
		#assert os.path.isdir(path_from), 'path_from does not exists.'
		#print self.log_dir
		#e(0)
		self.zip(path_from, path_to)
		#e(0)
		#print self.remote_login
		assert self.remote_login, 'Remote login is not set.'
		
		(host, username, pw)=self.remote_login
		ssh=SSHConnection(host, username, pw)
		assert os.path.isfile('%s.zip' % path_to), 'path_to "%s" does not exists.' % ('%s.zip' % path_to)
		#print dst
		#e(0)
		ssh.put('%s.zip' % path_to, dst)	
		#e(0)
	def execute(self,db_login_from, db_login_to):
		"""execute remote command"""
		ssh_log_loc=os.path.join(self.log_dir,'ssh.log')
		paramiko.util.log_to_file(ssh_log_loc)
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		(host, username, pw)=self.remote_login
		client.connect(host, username=username, password=pw)

		ts=self.conf.ts
		fname_to=self.get_dist_name()
		dst='/tmp/%s.zip' % ( fname_to)
		
		from_zip='%s/%s_%s_log.zip' % (self.remote_home_ts,ts,self.shard)
		#format login for sqlldr
		user_pwd,conn =db_login_from.split('@')
		login_from= """%s@'"%s"'""" % (user_pwd, conn.strip("'").strip('"'))
		user_pwd,conn =db_login_to.split('@')
		login_to= """%s@'"%s"'""" % (user_pwd, conn.strip("'").strip('"'))
		
		#print db_login
		
		cmd="""
cd /tmp
unzip -o %s >/dev/null
cd %s
rm %s
cd %s
chmod +x ./run.sh
./run.sh %s %s
cd %s
zip %s  %s/log.txt %s/sqlloader -r	>/dev/null
echo "log at %s/log.txt"
echo "spool at %s"
		""" % (  dst,  self.remote_home, dst, self.remote_home_ts, login_from, login_to,self.remote_home_ts,from_zip,self.remote_home_ts,self.remote_home_ts,self.remote_home_ts, self.result_file)

		#print cmd
		#e(0)
		stdin, stdout, stderr = client.exec_command(cmd)

		line =' '
		out=[]
		while line:
			line= stdout.readline()
			out.append(line)
			print str(line)
		#print '-'*60
		line =' '
		while line:
			line= stderr.readline()
			print str(line)
		client.close()
		to_log_zip=os.path.join(self.in_dir,'%s_%s_log.zip' % (ts,self.shard))
		#import time
		#time.sleep(1)
		if 1:
			ssh=SSHConnection(host, username, pw)
			ssh.get(from_zip, to_log_zip)
			ssh.close()	
		return out

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
		self.hm = hmap.host_map(self.args.copy_vector.split(self.conf._to),host_map_loc,0)
			
	def get_table_columns(self,  tab_name):
		self.tab_cols[tab_name]=(self.args.to_column_names,[])
		return self.tab_cols[tab_name]

	def do_query(self,login, query, query_file=None, regexp=None, grp=None, spset='', qname=None):
		status=0
		out=[]
		assert  len(login)>0, 'Default login is not set.'
		show=False
		if type(login) == types.TupleType:
			to_tab=login[1]
			login=login[0]
		q=''
		opt=''
		db_client_dbshell= self.get_db_client_dbshell()		
		assert os.path.isfile(db_client_dbshell), 'Oracle sqlplus.exe does not exists at %s.' % db_client_dbshell
		if query_file:
			#q = "%s\n%s\n@%s" % ( spset,opt,query_file)			
			assert os.path.isfile(query_file), 'Query file does not exists!'
			
		else:		
			#print self.datadir
			q = "%s\n%s\n%s\nexit;" % ( spset,opt, query)
			assert qname, 'query name "qname" is not set'
			query_file=self.save_qry(qname,q)
			#print query_file
			#q = "%s%s" % ( opt,query)
			#cfg=[ db_client_dbshell, login]
		cfg=[ db_client_dbshell,"-S", login,r'@%s' %  query_file]
		
		

		#if self.args.nls_timestamp_format:
		#	os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
		#else:
			#print '2'
		#	os.environ['NLS_TIMESTAMP_FORMAT']=''
		pprint (cfg)
		p = Popen(cfg,  stdout=PIPE,stderr=PIPE, shell=True)
		output, err = p.communicate()
		#print output, err
		if err:
			self.log.error(err)
		status=p.wait()	
		for o in output.split(os.linesep):
			#print o
			if o.strip():
				if regexp:
					m = re.match(regexp, o.strip()) 
					#print m
					if m:
						if grp:
							out.append(m.group(grp).strip())
						else:
							groups=m.groups()
							if groups:
								out.append(groups)
				else:
					
					out.append(o.strip())


		#pprint(out)
		#print 'after'
		#e(0)
		return (out,status,err)		
	def coldef (self,x): 
		#pprint(x)
		(colname, colsize, coltype)= x[0].split(':')
		#print x, int(colsize), int(colsize)>265
		if colsize:
			if int(colsize)>255:
				#print x, '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
				#row = x.split(':')
				if coltype in ('VARCHAR2'):
					return '%s CHAR(%s) NULLIF %s=BLANKS ' % (colname,colsize,colname)
				if coltype in ('CHAR'):
					return '%s filler CHAR(%s)' % (colname,colsize)				
			if coltype in ('DATE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_date_format)
			if coltype in ('TIMESTAMP'):
				return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_format)
			if coltype in ('TIMESTAMP WITH TIMEZONE'):
					return '%s "TO_DATE(:%s, \'%s\')" ' % (colname,colname,self.args.nls_timestamp_tz_format)
					
		return colname			
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
		
	def get_db_client_dbshell(self):
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(self.conf.dbtools['DBSHELL'][self.db])
		if self.hm.local_source_client_home: #self.args.source_client_home:
			#print self.hm.local_source_client_home
			
			self.db_client_dbshell=(r'%s\%s' % (self.hm.local_source_client_home, loader)).strip("'").strip('\\').strip('\\')
			
		else:
			self.db_client_dbshell=self.conf.dbtools['DBSHELL'][self.db]
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %' % loader)
		#print self.db_client_dbshell
		#e(0)
		return self.db_client_dbshell
	def get_ddl_sppol_query(self):
		schema,tab= self.from_table.split('.')
		q= """set heading off;
set echo off;
Set pages 999;
set long 90000;

--spool ddl_list.sql
EXEC DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'PRETTY',true);
EXECUTE DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'SQLTERMINATOR',true);
select dbms_metadata.get_ddl('TABLE','%s','%s') 
from all_tables where owner='%s' and table_name='%s';

SELECT DBMS_METADATA.GET_DDL ('INDEX', index_name, table_owner)
FROM all_indexes
WHERE table_owner='%s' and table_name='%s';

exit;

""" % (tab.upper(), schema.upper(), schema.upper(), tab.upper(),schema.upper(), tab.upper())

		#print q
		return q	
	def spool_source_data(self,outfn, spConf, payload):
		#shard=0
		#pprint (payload)
		
		shard=payload[0].split('-')[1]
		#print payload[0]
		#e(0)
		assert not self.cr.has_key(shard), 'self.cr is already set'
		self.cr[shard]=code_release(self.log,self, self.conf, self.args, spConf, shard)
		#print self.args.host_map
		#pprint(payload)
		#print self.cr[shard].R
		#e(0)
		#print '-----%s--%s--%s' % (self.cr.shard, self.shard,payload[0].split('-')[1])
		if self.cr[shard].R:		
			self.log.info('Starting remote spool...')
			return self.spool_source_data_posix(outfn, spConf, payload)
		else:
			self.log.info('Starting local spool...')
			return self.spool_source_data_nt(outfn, spConf, payload)
		
			

		#e(0)
	def spool_source_data_posix(self,outfn, spConf, payload):
		(shard_name,from_pld,to_pld)=payload
		#remote_login=self.cr.remote_login
		home=self.conf.home
		log_dir=self.datadir
		ts= self.conf.ts
		out_dir=os.path.join(log_dir,'out',ts)
		shard=payload[0].split('-')[1]
		#print self.args.copy_vector
		#e(0)
		#print '-----%s' % self.cr.shard
		if self.args.copy_vector.upper().split(self.conf._to)[1] in self.conf.ff:
			
		
			self.cr[shard].release()
			#print self.cr.shard
			#e(0)
			self.cr[shard].execute(db_login_from=self.login, db_login_to=self.login)


		#e(0)


		#print out_dir
		#e(0)
		count=-1
		status=0
		return (count, status)	
		
	def spool_source_data_nt(self,outfn, spConf, payload):
		(shard_name,from_pld,to_pld)=payload

		#outf=open(outfn, "w")
		#print self.cols_from
		if 0:
			if self.args.nls_timestamp_format:
				os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
			else:
				os.environ['NLS_TIMESTAMP_FORMAT'] =''
			if self.args.nls_timestamp_tz_format:
				os.environ['NLS_TIMESTAMP_TZ_FORMAT'] = self.args.nls_timestamp_tz_format
			else:
				os.environ['NLS_TIMESTAMP_TZ_FORMAT'] =''	
		#print outfn
		#pprint(spConf)
		#e(0)
		output=None
		err=None
		if 1:
			p = Popen(spConf, stdout=PIPE, stderr=PIPE) # '-S',  stdin=p1.stdout,
			#print 1
			output, err = p.communicate()
			#print 1,output, 2,err
		else:
			p = Popen(spConf, stdin=PIPE, stdout=PIPE, stderr=PIPE)
			output=' '
			while output:
				output = p.stdout.readline()
				print output
			error=' '
			while error:
				error = p.stderr.readline()
				print 1,error				
				#out.append(output)		
			#if err:
			#	self.log.err(err)
				#print output
		status=p.wait()
		#print outfn
		#outf.close()
		#print 1
		#e(0)
		#print err
		count=-1
		
		#count is in err
		r=re.compile(r'exported\s+(\d+)\s+records')
		
		g=re.search(r,err)
		#print g.groups()
		if g:
			count=int(g.groups()[0])
			#rows_total +=rows_copied
			#print rows_total
		#print rows_copied
		#print count
		return (count, status)			
		

#
# Define your custom SQL*Loader config
#	
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
	def get_load_config(self, db_loader_loc,shard_name, row_from, row_to,ctlfn,outfn, datadir):
		to_db=self.args.copy_vector.split(self.conf._to)[1].upper()
		#from_file=self.args.input_files
		#print outfn
		file_format=''
		fn, file_ext = os.path.splitext(outfn) 
		file_ext = file_ext.strip('.')
		if file_ext.upper() in ('DATA','CSV'):
			file_format='csv'
		else:
			file_format=file_ext.lower()
		#print file_ext, file_format
		loadConf=[db_loader_loc, '-u', self.args.to_user, '-p', self.args.to_passwd, '/d', self.args.to_db_name,'/h',self.args.to_db_server, '/c', self.args.to_collection, '/file', outfn, '/type', file_format, '/headerline'] #'/f', self.args.to_column_names, 
		
		return loadConf	
		

	def save_ctl(self,  to_table,shard):
		ptn=''
		sptn=''
		cols = self.get_table_columns(to_table)
		#print cols
		dpl_mode='APPEND'
		line_term=''
		ctl=self.get_ctl(to_table,cols,dpl_mode,(line_term,'|'))

		ctlfn= '%s/%s%s_Shard-%s.ctl' % (self.ctldir,to_table, "%s%s" % (ptn,sptn),shard)


		f = codecs.open(ctlfn, 'w',"utf-8")
		status = f.write(unicode(ctl))

		if status!= None:
			self._logger.error('Cannot write to %s.' % ctlfn)
		f.close()
		return 	ctlfn	

	def get_ctl(self,  to_tab, r_int, dpl_mode, term):
		(line_term,field_term) =term
		part = ''
		#pprint(r_int)
		unrec = 'UNRECOVERABLE'	#INFILE '-' "str '%s\n'"			
		tmpl="""%s
	LOAD DATA
	%s
	INTO TABLE %s %s
	FIELDS TERMINATED BY '%s'
	TRAILING NULLCOLS
	(%s)""" % (unrec,dpl_mode,to_tab, part, field_term, ','.join(r_int[1]))
		#pprint(tmpl)
		#pprint(r_int)
		#sys.exit(1)
		return tmpl	
		
	def get_db_client_dbshell(self):
		assert self.hm.local_target_client_home, 'self.args.target_client_home is not set'
		if self.db_client_dbshell:
			return self.db_client_dbshell
		loader= os.path.basename(self.conf.dbtools['DBSHELL'][self.db])
		if self.hm.local_target_client_home:
			self.db_client_dbshell=(r'%s\%s' % (self.hm.local_target_client_home, loader)).strip("'").strip('\\').strip('\\')
		else:
			self.db_client_dbshell=self.conf.dbtools['DBSHELL'][self.db]
			print self.db_client_dbshell,self.db
			print self.hm.local_target_client_home
			e(0)
			
			if not os.path.isfile(self.db_client_dbshell):
				self.log.warn('Path to source loader is not set. Defaulting to %s' % loader)	
		return self.db_client_dbshell
	def load_data(self,logger,loadConf,outfn,shard):
		#pprint (shard)
		#print self.conf.home
		self.cr[shard]=code_release(self.log,self, self.conf, self.args, loadConf, shard)
		#e(0)		
		if self.cr[shard].R:
			logger.info('Starting remote load.')
			return self.load_data_posix(logger,loadConf,outfn,shard)
		else:
			logger.info('Starting local load..')
			return self.load_data_nt(logger,loadConf,outfn,shard)
		
			
	def load_data_posix(self,logger,loadConf,outfn,shard):
		
		out=[]
		err=[]
		home=self.conf.home
		log_dir=self.datadir
		ts= self.conf.ts
		out_dir=os.path.join(log_dir,'out',ts)
		self.cr[shard].release()
		#print (self.args.from_db)
		
		out=self.cr[shard].execute(db_login_from=self.args.from_db, db_login_to=self.login)
		
		#out,status,err,ins_cnt =([],0,None,-1)
		ins_cnt=-1
		spool_size=-1
		spool_status, load_status = (99,99)
		#regexp1=re.compile(r'(\d+) Rows successfully loaded')
		regexp1=re.compile(r'Load completed - logical record count (\d+)')
		
		regexp2=re.compile(r'Spool file size (\d+)b')
		regexp3=re.compile(r'Spool retcode = (\d+)')
		regexp4=re.compile(r'Load retcode = (\d+)')
		
		for l in out:
			#print l
			m = re.match(regexp1, l.strip()) 
			if m and m.groups():
				ins_cnt= m.groups()[0]
			m = re.match(regexp2, l.strip()) 
			
			if m and m.groups():
				spool_size= m.groups()[0]
			m = re.match(regexp3, l.strip())
			
			if m and m.groups():
				spool_status= int(m.groups()[0])
			m = re.match(regexp4, l.strip()) 
			
			if m and m.groups():
				load_status= int(m.groups()[0])

				
		#print ins_cnt, spool_size
		status= spool_status + load_status
		#print spool_status , load_status
		err=[]
		#e(0)
		return (out,status,err,ins_cnt,spool_size)	
		
	def load_data_nt(self,logger,loadConf,outfn,shard):
		
		out=[]
		err=[]
		if 0:
			if self.args.nls_date_format:
				os.environ['NLS_DATE_FORMAT'] = self.args.nls_date_format
			#else:
				#os.environ['NLS_DATE_FORMAT'] = ''
			if self.args.nls_timestamp_format:
				os.environ['NLS_TIMESTAMP_FORMAT'] = self.args.nls_timestamp_format
			if self.args.nls_timestamp_format:
				os.environ['NLS_TIMESTAMP_TZ_FORMAT'] = self.args.nls_timestamp_tz_format				

		
		#pprint(loadConf)
		#print ' '.join(loadConf)
		#e(0)
		
		if 1:
			p = Popen(loadConf, stdout=PIPE, stderr=PIPE) # '-S',  stdin=p1.stdout,
			#print 1
			output, err = p.communicate()
			#print 1,output
			#print 2,err
		else:
			p = Popen(loadConf, stdin=PIPE, stdout=PIPE, stderr=PIPE)
			output=' '
			while output:
				output = p.stdout.readline()
				print output
			error=' '
			while error:
				error = p.stderr.readline()
				print 1,error				

		status = p.wait()
		count=-1
		print err
		#count is in err
		r=re.compile(r'imported\s+(\d+)\s+documents')
		g=re.search(r,err)
		#print g.groups()
		if g:
			count=int(g.groups()[0])
			#rows_total +=rows_copied
			#print rows_total
		#print count
		if count>-1:
			err=[]
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
		return (out,status,err,count,stat)	
		
	def get_inserted_count(self,shard):
		ptn=''
		sptn=''
		
		logfn='%s\\%s%s_Shard-%s.log' % (self.ctldir,self.to_table, "%s%s" % (ptn,sptn),shard)

		rows_copied=-1
		#print logfn
		if not os.path.isfile(logfn):
			print 'Log file for shard "%s" is missing.' % shard
			#self.log.error('Log file for shard %d is missing.' % shard)
		else:
			shl=open(logfn, 'r').read()
			#print shl
			r=re.compile(r'\s+(\d+) Rows successfully loaded\.')

			g=re.search(r,shl)
			#print g.groups()
			if g:
				rows_copied=int(g.groups()[0])
				#rows_total +=rows_copied
				#print rows_total
		#print rows_copied
		return rows_copied

		
class SSHConnection(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, host, username, password, port=22):
        """Initialize and setup connection"""
        self.sftp = None
        self.sftp_open = False
 
        # open SSH Transport stream
        self.transport = paramiko.Transport((host, port))
 
        self.transport.connect(username=username, password=password)
 
    #----------------------------------------------------------------------
    def _openSFTPConnection(self):
        """
        Opens an SFTP connection if not already open
        """
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True
 
    #----------------------------------------------------------------------
    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        self._openSFTPConnection()        
        self.sftp.get(remote_path, local_path)        
 
    #----------------------------------------------------------------------
    def put(self, local_path, remote_path=None):
        """
        Copies a file from the local host to the remote host
        """
        self._openSFTPConnection()
        self.sftp.put(local_path, remote_path)
 
    #----------------------------------------------------------------------
    def close(self):
        """
        Close SFTP connection and ssh connection
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()