# Named Pipe Server Source Code:

from ctypes import *

PIPE_ACCESS_DUPLEX = 0x3
PIPE_TYPE_MESSAGE = 0x4
PIPE_READMODE_MESSAGE = 0x2
PIPE_WAIT = 0
PIPE_UNLIMITED_INSTANCES = 255
BUFSIZE = 4096
NMPWAIT_USE_DEFAULT_WAIT = 0
INVALID_HANDLE_VALUE = -1
ERROR_PIPE_CONNECTED = 535

MESSAGE = "\0"
MESSAGE_INC = 1

szPipename = "\\\\.\\pipe\\mynamedpipe"




class NamedPipeServer(object):
	def __init__(self, pipename):
		self.pipename 		= pipename
		
		self.rwthread 		= CFUNCTYPE(c_int, c_int)
		self.thread_func 	= self.rwthread(self.readwrite)

		
		self.runner()
		
	def runner(self):
		
		print "Starting NamedPipe Server"
		
		while 1:
			
			hPipe = windll.kernel32.CreateNamedPipeA(
				self.pipename, 
				PIPE_ACCESS_DUPLEX, 
				PIPE_TYPE_MESSAGE | PIPE_READMODE_MESSAGE | PIPE_WAIT, 
				PIPE_UNLIMITED_INSTANCES, 
				BUFSIZE, 
				BUFSIZE, 
				NMPWAIT_USE_DEFAULT_WAIT,
				None)
			
			
			if (hPipe == INVALID_HANDLE_VALUE):
				print "Error in creating Named Pipe"
				return 0

			fConnected = windll.kernel32.ConnectNamedPipe(hPipe, None)
			#print fConnected
			if ((fConnected == 0) and (windll.kernel32.GetLastError() == ERROR_PIPE_CONNECTED)):
				fConnected = 1				

			if (fConnected == 1):
				
				dwThreadId = c_ulong(0)
				hThread = windll.kernel32.CreateThread(None, 0, self.thread_func, hPipe, 0, byref(dwThreadId))
				
				if (hThread == -1):
					print "Thread error"
					return 0
				else:
					windll.kernel32.CloseHandle(hThread)
			else:
				#print "Could not connect to the Named Pipe"
				windll.kernel32.CloseHandle(hPipe)
		return 0

	def readwrite(self, hPipe):
		global MESSAGE
		global MESSAGE_INC
		
		chBuf = create_string_buffer(BUFSIZE)
		cbRead = c_ulong(0)
	
		while 1:
		
			fSuccess = windll.kernel32.ReadFile(hPipe, chBuf, BUFSIZE, byref(cbRead), None)
		
			if ((fSuccess ==1) or (cbRead.value != 0)):
				print "Got Data from Client:", chBuf.value
			
				MESSAGE_INC += 1
				MESSAGE = "Message Nr:"+ str(MESSAGE_INC)+" Sent from the SERVER\0"
				
				cbWritten = c_ulong(0)
				fSuccess = windll.kernel32.WriteFile(hPipe, c_char_p(MESSAGE), len(MESSAGE), byref(cbWritten), None)
		
			else:
				break
		
			if ( (not fSuccess) or (len(MESSAGE) != cbWritten.value)):
				print "Could not reply to the client's request from the pipe"
				break
			#else:
				#print "Number of bytes written:", cbWritten.value

		windll.kernel32.FlushFileBuffers(hPipe)
		windll.kernel32.DisconnectNamedPipe(hPipe)
		windll.kernel32.CloseHandle(hPipe)
		return 0

		
def main():
	nps = NamedPipeServer(szPipename)
		
if __name__ == "__main__":
	main()