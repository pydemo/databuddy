#'192.168.15.91', 'oracle', 'oracle'
from ftplib import FTP
ftp = FTP('192.168.15.91') 
ftp.login('oracle', 'oracle')
ftp.cwd('/tmp')           
ftp.retrlines('LIST') 

pscp.exe  -pw oracle oracle@192.168.15.91:/tmp/qctest/release.pyc  "C:\tmp\putty\release.pyc"