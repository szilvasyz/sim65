import sys
import time
import myio


class Machine:

    def __init__(self):
        self.components = []

    def add(self, obj):
        self.components.append(obj)

    def list(self):
        for comp in self.components:
            print(comp)


class Component:

    def __init__(self):
        self.type = ""

    def __str__(self):
        return self.type


class Cpu(Component):

    def __init__(self):
        self.type = "CPU"


class Mem(Component):

    def __init__(self):
        self.type = "MEM"


mymachine = Machine()
mycpu = Cpu()
mymem = Mem()

mymachine.add(mycpu)
mymachine.add(mymem)
mymachine.add(Mem())

mymachine.list()


sys.stdout = myio.Unbuffered(sys.stdout)
print('Hello')


mykey = myio.GetKey()

while True:
    key = mykey.getkey()
    if key != None:
        print(chr(key), end="")
    else:
        time.sleep(0.1)
