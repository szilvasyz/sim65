from intelhex import IntelHex


class Memory:

    def __init__(self):
        self.memory = dict()

    def fill(self, lower, upper, data):
        for addr in range(lower, upper):
            self.memory[addr] = data

    def load(self, filename):
        ih = IntelHex(filename)
        for addr in ih.addresses():
            self.memory[addr] = ih[addr]

    def read(self, address, poll):
        try:
            if address in self.memory:
                data = self.memory[address]

            else:
                data = None

        except:
            print("Error reading ", type(address), address)
            data = None

        return data

    def write(self, address, data):
        try:
            if address in self.memory:
                self.memory[address] = data

        except:
            print("Error writing ", type(address), address)


# def memory_write_test(address, data, debug=0):
#     if address == 0xF001:
#         print("{:c}".format(data), end="")
#     if debug:
#         print("Write {:04X},{:02X}".format(address, data))
#     memory[address] = data


