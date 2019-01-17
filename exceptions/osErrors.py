try:
    import msvcrt

    def getKey():
        return msvcrt.getch()
except ImportError:
    import sys
    import tty
    import termios

    def getKey():
        fd = sys.stdin.fileno()
        orginalAttributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, orginalAttributes)
            return ch
