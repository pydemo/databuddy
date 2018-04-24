import os
import sys

if sys.platform == "win32":
    import msvcrt

# Get file descriptor from argument
pipearg = 260 #int(sys.argv[1])
if sys.platform == "win32":
    pipeoutfd = msvcrt.open_osfhandle(pipearg,os.O_RDONLY)
else:
    pipeoutfd = pipearg

# Read from pipe
# Note:  Could be done with os.read/os.close directly, instead of os.fdopen
print pipeoutfd
pipeout = os.fdopen(pipeoutfd, 'r')
print pipeout.read()
pipeout.close()