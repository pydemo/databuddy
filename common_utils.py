import os, sys
from tc_lib import *
#from tc_lib import _send
#from wx.lib.pubsub import Publisher
from tc_init import *
from subprocess import Popen, PIPE,STDOUT
from pprint import pprint 
from tc_lib import  send #, sub

	
#import paramiko, sys
use_paramico=True
imitate_copy=True
try:
    import paramiko
	
except ImportError: # if paramiko not there use pscp.
	use_paramico=False
	if 0:
		tc_srv='bk_dev'
		tc_home='netezza'
		tc_host= {tc_srv:("zkqfas6",lpwd,'lrche25546')}
		tc_loc = {tc_srv:{tc_home:('/home/zkqfas6/tab_copy', 'pipeline/posix/','clients/table_copy/tab_copy/')}}
		tc_runat = {}
		for name, locs in tc_loc.items():
			#tc_runat[name]={}
			for loc_name, loc in locs.items():
				tc_runat['%s.%s' % (name,loc_name)]=(tc_host[name][2],loc[0],loc_name)
		print tc_runat
class PanelLog:
	def log(self,msg,  panel_id=None):
		#Publisher().sendMessage( "append_log", (msg,(0,1),panel_id) )
		assert panel_id, 'panel_id is not set'
		send( "append_log", (msg,(0,1),panel_id) )
	def err(self,msg,  panel_id=None):
		#Publisher().sendMessage( "append_err", (msg,(0,1),panel_id) )
		assert panel_id, 'panel_id is not set'
		send( "append_err", (msg,(0,1),panel_id) )
plog=PanelLog()		

def log_del(msg,  panel_id=None):
	#wx.LogMessage(msg)
	#Publisher().sendMessage( "append_log", (msg,(0,1),panel_id) )	
	send( "append_log", (msg,(0,1),panel_id) )

class NullLog:
	def write(*args):
		print args
		
class BrowserLog:
	def err(self,msg,pos=None):
		#Publisher().sendMessage( "append_browser_err", (msg,pos ))
		#print 'sending append_browser_err from blog'
		assert pos, 'pos is not set'
		send("append_browser_err", (msg,pos ))
	def log(self,msg,pos=None):
		assert pos, 'pos is not set'
		send( "append_browser_log", (msg,pos) )

blog= BrowserLog()
		
def rcopyFile(from_loc, to_loc, pos, panel_id):
	print 'remote copy',use_paramico
	print 'from', from_loc
	print 'to', 	to_loc
	(username, password, hostname) = tc_host[tc_srv]
	err=[]
	if imitate_copy:
		plog.log('Transfering 2: %s' % from_loc,panel_id)
		return(0,[])
	else:
		if use_paramico:
			
			

			#hostname = 'swmapetldev01.nam.nsroot.net'
			#password = 'prince987!'
			#username = "bk94994"
			port = 22

			#mypath='C:\\Python27.2.5\\_TaCo_\\Projects\\table_copy\\out\\tc_copy_test.xml'
			#remotepath='/opt/etl/apps/smart_dev/volumes/etl/scripts/tab_copy/tc_copy_test.xml'


			t = paramiko.Transport((hostname, 22))
			t.connect(username=username, password=password)
			sftp = paramiko.SFTPClient.from_transport(t)
			status=sftp.put(from_loc, to_loc)
			print 'remote copy status ', status
			
			
		else: #use pscp
			#remote_loc='/home/zkqfas6/tab_copy/pipeline/posix'
			status=0
			if 1:
			
				cmd='pscp -pw %s  "%s" %s@%s:%s' % (password,from_loc,username,hostname,to_loc)
				print cmd
				#sys.exit(1)
				#os.system(cmd)
				if 1:
					proc = Popen(cmd, stdin=PIPE,stdout=PIPE,stderr=PIPE, shell=True)
					output=' '
					out=[]
					status=0
					tt= proc.communicate(input='y\n')
					for t in tt:
						if t.startswith('Access denied') or t.startswith('Fatal') or t.startswith('ssh_init: Host does not exist'):
							err.append(t)
							
							#blog.err(t,pos)
					print 'y/n'
					print(tt)				
					while output:
						output = proc.stdout.readline() #string.replace(p2.stdout.readline(),'SQL>','')
						#blog.log(output,pos)
						out.append(output)
					error=' '
					
					while error:
						error=''
						error = proc.stderr.readline()	
						if error:					
							#blog.err(error,pos)
							err.append(error)
					#print 'after communicate'
					#print out
					#print err
					if err:
						status=1
						print '#'*20, ' ERROR ','#'*20
						print '#3#'.join(err)
						print '#'*20, ' ERROR ','#'*20
						print 'calling plog.log'
						plog.log(out,panel_id)
						
						print 'calling plog.err'
						plog.err(err,panel_id) 
						print 'calling plog.err'
						plog.log('remote copy completed with errors.',panel_id)
					else:
						plog.log(out,panel_id) 
						plog.log('remote copy completed.',panel_id)
					
			else:
				pass
		
			return (status,err)

def pui_rcopyFile(*args):
	(a,b,c) = args
	ret= rcopyFile(*a)
	return ret			
def execRemoteCmd(specs, worker,panel_id):
	import paramiko, sys

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	(username, password, hostname) = tc_host[tc_srv]
	ssh.connect(hostname, username=username, password = password )
	#ssh.exec_command( 'ls -al' )	
	#stdin,stdout,stderr = ssh.exec_command("cd /opt/etl/apps/smart_dev/volumes/etl/scripts/tab_copy;. ./.ora_profile;./run.sh t tab_copy;")
	cmd='time python tc.py --pipeline_spec=%s --pipeline=%s;' % (specs, worker)
	print cmd
	print specs
	print worker
	#sys.exit(1)
	stdin,stdout,stderr = ssh.exec_command("cd /opt/etl/apps/smart_dev/volumes/etl/scripts/tab_copy;. ./.ora_profile;%s" % cmd)
	
	#time python tc.py --pipeline_spec=pipeline/posix/pipeline_spec.xml --pipeline=clients/table_copy/tab_copy/tc_t.xml

	
	#stdin,stdout,stderr = ssh.exec_command("pbrun voletlusr")

	out= stdout.read()
	if out:
		if '** FATAL **' in out or '** ERROR **' in out or  'ERROR in line' in out or '## ERROR **' in out:
			#Publisher().sendMessage( "append_err", (out,(0,1),panel_id) )
			send("append_err", (out,(0,1),panel_id))
			return ([],out)
		else:
			#Publisher().sendMessage( "append_log", (out,(0,1),panel_id) )	
			send("append_log", (out,(0,1),panel_id) )
	err= stderr.read()
	pprint(err)
	if len(err.split('\n'))==5 and 'real' in err and 'user' in err and 'sys' in err:
		#Publisher().sendMessage( "append_log", (err,(0,1),panel_id) )
		send("append_log", (err,(0,1),panel_id) )
		err=[]		
	#sys.exit(0)
	if err:
		print '#'*40
		print err.strip()
		print '#'*40
		#Publisher().sendMessage( "append_err", ( err,(0,1),panel_id) )	
		send( "append_err", ( err,(0,1),panel_id) )
	#sys.exit(1)
	
	return (out,err)

def pui_execTaCo(*args):
	(a,b,c) = args
	ret= execTaCo(*a)
	return ret	
def execTaCo( specs, worker,panel_id):
	print specs
	print worker
	if imitate_copy:
		plog.log('remote exec imitation completed.',panel_id)
		return(0,[])
		
	(out,err)=((),0)
	if use_paramico:
		print 'using paramico'
		#plink_loc=r'C:\Program Files\PuTTY'
		#command = r"%s\plink.exe -ssh zkqfas6@lrche25546 -pw %s cd tab_copy;time python tc.py --pipeline_spec=%s --pipeline=%s" % (plink_loc, lpwd, specs,worker)
		#print command
		(out, err) = execRemoteCmd(specs, worker,panel_id)
		#sys.exit(1)
	else:
		#plink_loc=r"C:\Users\zkqfas6\Installs\putty"
		(username, password, hostname) = tc_host[tc_srv]
		print tc_loc
		print tc_runat
		srv=tc_loc[tc_srv][tc_home]
		print tc_srv, tc_home
		cmd = r'plink.exe -ssh %s@%s -pw %s cd %s;. ./.ora_profile;time python tc.py --pipeline_spec=%s --pipeline=%s' % (username, hostname, password,srv[0], specs,worker)
		print cmd
		#sys.exit(1)
		#test=os.system(cmd)
		#print test
		#status=os.popen(cmd).read()
		#print status
		if 1:
			proc = Popen(cmd, stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			out=[]
			status=0
			while output:
				output = proc.stdout.readline() #string.replace(p2.stdout.readline(),'SQL>','')
				print output
				out.append(output)
			error=' '
			err=[]
			while error:
				error = proc.stderr.readline()						
				err.append(error)
			print 'after communicate'
			print out
			pprint (err)
			if len(err)==5 and 'real' in err[1] and 'user' in err[2] and 'sys' in err[3]:
				#Publisher().sendMessage( "append_log", (err,(0,1),panel_id) )
				plog.err(err,panel_id)
				#send( "append_log", (err,(0,1),panel_id))
				err=[]	
			if err:
				print '#'*20, ' ERROR ','#'*20
				print '#1#'.join(err)
				print '#'*20, ' ERROR ','#'*20
				#Publisher().sendMessage( "append_err", ( err,(0,1),panel_id) )	
				print 'calling plog.err'
				plog.err(err,panel_id)
				#plog.err(err,panel_id)
				#send("append_err", ( err,(0,1),panel_id))
				
		
		if 0:
			try:
				#out=subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=False)
				process = subprocess.Popen(cmd, stdout=subprocess.STDOUT,stderr=subprocess.STDOUT)
				output, unused_err = process.communicate()
				retcode = process.poll()
				print 'retcode--------'
				print retcode
				print output
				print unused_err
				
			except e:
				print 'error--------', e
				print out 
				print dir(subprocess.STDOUT)
			print 'os.system(command) status=' 
		#print subprocess.STDOUT
		
		
	return (out,err)
	