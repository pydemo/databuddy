
import os
import subprocess
import sys
import time
from pprint import pprint
if sys.platform == "win32":
	import msvcrt
	import _subprocess
else:
	import fcntl

# Create pipe for communication
pipeout, pipein = os.pipe()

# Prepare to pass to child process
if sys.platform == "win32":
	curproc = _subprocess.GetCurrentProcess()
	pprint (dir(curproc))
	pipeouth = msvcrt.get_osfhandle(pipein)
	pipeoutih = _subprocess.DuplicateHandle(curproc, pipeouth, curproc, 0, 1,
			_subprocess.DUPLICATE_SAME_ACCESS)

	pipearg = str(int(pipeoutih))   
	print pipearg
else:
	pipearg = str(pipein)

	# Must close pipe input if child will block waiting for end
	# Can also be closed in a preexec_fn passed to subprocess.Popen
	fcntl.fcntl(pipeout, fcntl.F_SETFD, fcntl.FD_CLOEXEC)

# Start child with argument indicating which FD/FH to read from
ON_POSIX = 'posix' in sys.builtin_module_names
subproc = subprocess.Popen(['python', 'child_in.py', pipearg], close_fds=ON_POSIX)
subproc2 = subprocess.Popen(['python', 'child_in.py', pipearg], close_fds=ON_POSIX)

# Close read end of pipe in parent
os.close(pipein)
if sys.platform == "win32":
	pipeoutih.Close()
#p = Popen(['myprogram.exe'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
from threading  import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

#ON_POSIX = 'posix' in sys.builtin_module_names

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    #out.close()
	
q = Queue()
import io
# Write to child (could be done with os.write, without os.fdopen)
pipefh = io.open(pipeout, 'r') #os.fdopen(pipeout, 'r',0)
t = Thread(target=enqueue_output, args=(pipefh, q))
t.daemon = True # thread dies with the program
t.start()

# ... do other things here

# read line without blocking
line=''
for i in range(100):
	try:  line = q.get_nowait() # or q.get(timeout=.1)
	except Empty:
		print('no output yet')
	else: # got line
		print 2, line
		# ... do something with line
	time.sleep(1)
	
if 0:
	import io
	# Write to child (could be done with os.write, without os.fdopen)
	pipefh = io.open(pipeout, 'r') #os.fdopen(pipeout, 'r',0)
	#while 1:
	# Wait for the child to finish
	#pprint(dir(pipefh))
	for i in range(100):
		
		print pipefh.closed, pipefh.tell(), pipefh.isatty()
		test= pipefh.read()
		print 1, test	
		time.sleep(1)
	pipefh.close()
	subproc.wait()
	subproc2.wait()


