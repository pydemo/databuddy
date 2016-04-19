import time
import sys
hg=['-','\\','|', '/']
for i in range(100):
	time.sleep(0.1)
	#sys.stdout.write("\r%d%%" % hg[i%2])
	sys.stdout.write("\r%s" % hg[i%4])
	
	sys.stdout.flush()
sys.stdout.write("\r%d%%" % 100)
	#print i%2