import sys
import Crypto
#sys.modules['Crypto'] = crypto
import paramiko
from ssh_file import  SSHConnection
paramiko.util.log_to_file('ssh.log')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.load_system_host_keys()
#
ctl_file='SCOTT.Timestamp_test_to_Shard-0.ctl'
e=sys.exit
import os
import zipfile

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()



if 1:
	host='192.168.15.47'
	username='oracle'
	pw='oracle123'
	

	#dst='/tmp/qctest/sqlloader/%s' % zipped
	path_from=r'C:\Temp\qc_log\qc_job'
	
	ts ='20150408_172619_171000_'
	path_to='%s_dist' % ts
	loc=os.path.join(path_from, ts)
	origin='%s.zip' % path_to
	dst='/tmp/qctest/%s.zip' % path_to


if 1:	
		
	client.connect('192.168.15.47', username='oracle', password='oracle123')
	remote_home='/tmp/qctest'
	remote_home_ts='/tmp/qctest/%s' % ts
	sql_file='%s/%s/spool.sql' % (remote_home, ts)
	result_file='result.data'
	ora_home='/home/oracle/app/oracle/product/12.1.0/dbhome_1'
	tns_admin ='/home/oracle/app/oracle/product/12.1.0/dbhome_1/network/admin'
	ora_profile="""
ORACLE_HOME=%s
export ORACLE_HOME
#LD_LIBRARY_PATH=$ORACLE_HOME/lib;
#export LD_LIBRARY_PATH
PATH=$PATH:$ORACLE_HOME/bin;
export PATH
TNS_ADMIN=%s
export TNS_ADMIN
echo $TNS_ADMIN
	""" % (ora_home,tns_admin)
	with open(os.path.join(loc,'.ora_profile'), 'wb') as file_:
		file_.write(ora_profile.replace(r'\r\n',r'\n'))	
	r_ctl_file_loc='%s/%s/sqlloader/%s' % (remote_home, ts, ctl_file)
	fname, ext =  os.path.splitext(ctl_file)
	r_log_file_loc='%s/%s/sqlloader/%s.log' % (remote_home, ts, fname)
	r_bad_file_loc='%s/%s/sqlloader/%s.bad' % (remote_home, ts, fname)
	r_dsc_file_loc='%s/%s/sqlloader/%s.dsc' % (remote_home, ts, fname)
	run="""		
cd %s
. ./.ora_profile
NLS_DATE_FORMAT='YYYY-MM-DD HH24.MI.SS'
export NLS_DATE_FORMAT
NLS_TIMESTAMP_FORMAT='YYYY-MM-DD HH24.MI.SS.FF2'
export NLS_TIMESTAMP_FORMAT
NLS_TIMESTAMP_TZ_FORMAT='YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM'
export NLS_TIMESTAMP_TZ_FORMAT

test= $ORACLE_HOME/bin/sqlplus -S $1 @%s>%s

echo $test
retcode=`echo $?`
echo $retcode
ls -al %s
time $ORACLE_HOME/bin/sqlldr control=%s userid=$1 DATA=%s LOG=%s BAD=%s DISCARD=%s BINDSIZE=200010 ERRORS=10 SKIP_UNUSABLE_INDEXES=TRUE COLUMNARRAYROWS=10000 DIRECT=TRUE STREAMSIZE=500000 READSIZE=200000 MULTITHREADING=TRUE SKIP_INDEX_MAINTENANCE=TRUE PARALLEL=TRUE
retcode=`echo $?`
echo $retcode
rm %s

	""" % ( remote_home_ts, sql_file, result_file, result_file, r_ctl_file_loc,result_file, r_log_file_loc,r_bad_file_loc,r_dsc_file_loc, result_file)
	with open(os.path.join(loc,'run.sh'), 'wb') as file_:
		file_.write(run)
	zip(path_from, path_to)
	if 1:
		ssh=SSHConnection(host, username, pw)
		ssh.put(origin, dst)
		#ssh.close()		
	print run
	#e(0)
	login='scott/tiger@orcl_ol7'
	from_zip='%s/%s_log.zip' % (remote_home,ts)
	cmd="""
	cd %s
	unzip -o %s
	rm %s
	cd %s/%s
	
	chmod +x ./run.sh
	./run.sh %s
	cd %s
	zip %s %s %s/* -r	
	""" % ( remote_home,dst,dst, remote_home, ts, login,remote_home,from_zip,ts,ts)
	print cmd
	#chan = client.get_transport().open_session()
	#print "running '%s'" % cmd
	#stdin, stdout, stderr =chan.exec_command(cmd)
	stdin, stdout, stderr = client.exec_command(cmd)
	#print dir(client)

	print '-'*40
	line =' '
	while line:
		line= stdout.readline()
		print line
	print '-'*60
	line =' '
	while line:
		line= stderr.readline()
		print line 
	client.close()
	to_log_zip=r'c:\tmp\%s_log.zip'
	#import time
	#time.sleep(1)
	if 1:
		#ssh=SSHConnection(host, username, pw)
		ssh.get(from_zip, to_log_zip)
		ssh.close()	
