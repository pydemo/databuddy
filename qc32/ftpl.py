#'192.168.15.91', 'oracle', 'oracle'
import sys
e=sys.exit

#pscp.exe  -pw oracle oracle@192.168.15.227:/tmp/qctest/release.pyc  "C:\tmp\putty\release.pyc"


if 0:
	from ftplib import FTP
	ftp = FTP('192.168.15.227') 
	ftp.login('oracle', 'oracle')
	ftp.cwd('/tmp')           
	ftp.retrlines('LIST') 
if 0:
	from ftplib import FTP_TLS
	ftps = FTP_TLS('192.168.15.227','oracle', 'oracle')
	#ftps = FTP_TLS('ftp.python.org')
	#e(0)
	print ftps
	ftps.login()           
	ftps.prot_p()          
	ftps.cwd('/tmp/qctest')  
	ftps.retrlines('LIST')	
if 1:
	import pysftp
	with pysftp.Connection('192.168.15.227', username='oracle', password='oracle') as sftp:
		 with sftp.cd('/tmp/qctest'):
			sftp.put(r'C:\Users\alex_buz\Documents\GitHub\DataBuddy\release.pyc')  # upload file to public/ on remote