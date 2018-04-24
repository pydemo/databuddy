from subprocess import Popen, PIPE

f = open(FILENAME, 'wb')
args = ['mysqldump', '-u', 'UNAME', '-pPASSWORD', '--add-drop-database', '--databases', 'DB']

p1 = Popen(args, stdout=PIPE)
P2 = Popen('gzip', stdin=p1.stdout, stdout=f)
p2.wait()
p1.wait()