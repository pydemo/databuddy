import console
(width, height) = console.getTerminalSize()

print "Your terminal's width is: %d" % width
EDIT: oh, I'm sorry. That's not a python standard lib one, here's the source of console.py (I don't know where it's from).

The module seems to work like that: It checks if termcap is available, when yes. It uses that; if no it checks whether the terminal supports a special ioctl call and that does not work, too, it checks for the environment variables some shells export for that. This will probably work on UNIX only.

def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])