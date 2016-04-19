
import os
import subprocess
import sys

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
	pipeouth = msvcrt.get_osfhandle(pipeout)
	pipeoutih = _subprocess.DuplicateHandle(curproc, pipeouth, curproc, 0, 1,
			_subprocess.DUPLICATE_SAME_ACCESS)

	pipearg = str(int(pipeoutih))   
	print pipearg
else:
	pipearg = str(pipeout)

	# Must close pipe input if child will block waiting for end
	# Can also be closed in a preexec_fn passed to subprocess.Popen
	fcntl.fcntl(pipein, fcntl.F_SETFD, fcntl.FD_CLOEXEC)

# Start child with argument indicating which FD/FH to read from
subproc = subprocess.Popen(['python', 'child_out.py', pipearg], close_fds=False)

# Close read end of pipe in parent
os.close(pipeout)
if sys.platform == "win32":
	pipeoutih.Close()

# Write to child (could be done with os.write, without os.fdopen)
pipefh = os.fdopen(pipein, 'w')
pipefh.write("Hello from parent.")
pipefh.close()

# Wait for the child to finish
subproc.wait()