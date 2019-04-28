class cells:

    def __init__(self, conread=None, conwrite=None):
        self.conread = conread
        self.conwrite = conwrite
        self.memory[0xCF10] = 0
        self.memory[0xCF11] = 0
        self.memory[0xCF12] = 0
        self.memory[0xCF13] = 0
        self.memory[0xCF14] = 0
        self.memory[0xCF15] = 0
        self.memory[0xCF16] = 0
        self.memory[0xCF17] = 0
        self.memory[0xCF18] = 0
        self.memory[0xCF19] = 0
        self.memory[0xCF1A] = 0
        self.memory[0xCF1B] = 0
        self.memory[0xCF1C] = 0
        self.memory[0xCF1D] = 0
        self.memory[0xCF1E] = 0
        self.memory[0xCF1F] = 0

    def fill(self, lower, upper, data):
        pass

    def load(self, filename):
        pass

    def read(self, address, poll):
        if (address & 0xFFF0) == 0xCF10:
            memory[0xCF11] |= 0x02
            ch = self.conread()
            if ch is not None:
                self.memory[0xCF10] = ch
                self.memory[0xCF11] |= 0x01

            data = self.memory[address]
            if address == 0xCF10:
                self.memory[0xCF11] &= ~0x01
            return data
        else:
            return None

    def write(self, address, data):
        if (address & 0xFFF0) == 0xCF10:
            if address == 0xCF10:
                self.conwrite(data)
            self.memory[address] = data

