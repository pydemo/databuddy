class Decompress(object):

    # Maximum to read from the decompressed stream
    maxsize = 2097152
    data = ""

    def __init__(self, application_path, type, filePath):

        # UPX Decompression
        if type == "UPX":

            print "Checking UPX file %s" % filePath 

            try:   
                p = win32pipe.CreateNamedPipe(r'\\.\pipe\upx', win32pipe.PIPE_ACCESS_DUPLEX, win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT, 1, 2097152, 2097152, 300, None)

                phandle = p.handle

                success, stdout, stderr = run_popen_with_timeout(application_path + r'tools\upx.exe -d --no-color --no-progress --no-backup -o\\.\pipe\upx ' + filePath, 3, "")
                #print stdout
                #print stderr   

                data = win32file.ReadFile(phandle, self.maxsize)

                p.close()

                #print "Read " + str(len(data[1])) + " bytes from decompressed EXE"

                self.data = data[1]
                #print self.data[:10]

            except Exception, e:
                traceback.print_exc()

def run_popen_with_timeout(command_string, timeout, input_data):
    """
    Run a sub-program in subprocess.Popen, pass it the input_data,
    kill it if the specified timeout has passed.
    returns a tuple of success, stdout, stderr
    """
    kill_check = threading.Event()
    def _kill_process_after_a_timeout(pid):
        os.kill(pid, signal.SIGTERM)
        kill_check.set() # tell the main routine that we had to kill
        # use SIGKILL if hard to kill...
        return
    p = Popen(command_string, stderr=STDOUT, stdout=PIPE)
    #print p.communicate()[0]
    print command_string
    pid = p.pid
    watchdog = threading.Timer(timeout, _kill_process_after_a_timeout, args=(pid, ))
    watchdog.start()
    (stdout, stderr) = p.communicate()
    watchdog.cancel() # if it's still waiting to run
    success = not kill_check.isSet()
    kill_check.clear()
    return (success, stdout, stderr) 