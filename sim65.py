import mod_6502
from intelhex import IntelHex
# import curses
import myio
import sys


def memory_read(address, debug=0):
    if (address & 0xFFF0) == 0xCF10:
        memory[0xCF11] |= 0x02
        ch = mykey.getkey()
        if ch is not None:
            memory[0xCF10] = ch
            memory[0xCF11] |= 0x01
    data = memory[address]
    if address == 0xCF10:
        memory[0xCF11] &= ~0x01
    if debug:
        print("Read {:04X} -> {:02X}".format(address, data))
    return data


def memory_write(address, data, debug=0):
    if address == 0xCF10:
#         print("{:c}".format(data), end="")
#         stdscr.addstr(",")
        if data != 13:
            print(chr(data), end="")
#            stdscr.refresh()
    if debug:
        print("Write {:04X},{:02X}".format(address, data))
    memory[address] = data


def memory_read_test(address, debug=0):
    try:
        data = memory[address]
        if address == 0xF004:
            while True:
                ch = mykey.getkey()
                if ch is not None:
                    data = ch
                    break

#            data = ord(sys.stdin.read(1)[0])
        if debug:
            print("Read {:04X} -> {:02X}".format(address, data))
    except:
        print("Error reading ", type(address), address)
        data = 0

    return data


def memory_write_test(address, data, debug=0):
    if address == 0xF001:
        print("{:c}".format(data), end="")
    if debug:
        print("Write {:04X},{:02X}".format(address, data))
    memory[address] = data


sys.stdout = myio.Unbuffered(sys.stdout)
mykey = myio.GetKey()


memory = [0xEA] * 65536


ih = IntelHex("6502_functional_test.hex")
for add in ih.addresses():
    memory[add] = ih[add]

#ih = IntelHex("prog6502.hex")
#for add in ih.addresses():
#    memory[add + 0xD000] = ih[add]


#cpu = core65.Core65(memory_read, memory_write, debug=0)
cpu = mod_6502.Core65(memory_read_test, memory_write_test, debug=0)
#cpu.cpu_state = 'run'
#cpu.regs["PC"] = 0x0400
print(cpu)


#for c in range(320060000):
for c in range(320000000):
    cpu.exec()
#    print(c, cpu)


