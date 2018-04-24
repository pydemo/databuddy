import os
import sys
import time
from pprint import pprint
if sys.platform == "win32":
    import msvcrt

# Get file descriptor from argument
pipearg = 260 #int(sys.argv[1])
if sys.platform == "win32":
    pipeoutfd = msvcrt.open_osfhandle(pipearg,os.O_WRONLY)
else:
    pipeoutfd = pipearg

# Read from pipe
# Note:  Could be done with os.read/os.close directly, instead of os.fdopen
#os.write()
#os.close()
if 1:
	pipein = os.fdopen(pipeoutfd, 'w')
	#for i in range(1000):

	time.sleep(5)
	pipein.write('Hello from client')
	#pprint (dir(pipein))
	#pipein.flush()
	#time.sleep(2)
	pipein.write('Hello from client')
	
	pipein.close()
	#time.sleep(2000)
	
