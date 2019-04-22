import termios
import sys
import os


class GetKey:

    old_settings = None

    def __init__(self):
        print("construct")
        self.old_settings = termios.tcgetattr(sys.stdin)
        self.new_settings = termios.tcgetattr(sys.stdin)
        self.new_settings[3] = self.new_settings[3] & ~(termios.ECHO | termios.ICANON) # lflags
        self.new_settings[6][termios.VMIN] = 0  # cc
        self.new_settings[6][termios.VTIME] = 0 # cc
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.new_settings)

    def __del__(self):
        if self.old_settings:
            print("destruct")
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def getkey(self):
        ch = os.read(sys.stdin.fileno(), 1)
        if len(ch) > 0:
            return ch[0]
        else:
            return None


class Unbuffered(object):

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


