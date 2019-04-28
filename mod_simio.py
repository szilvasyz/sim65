
class cells:

    def __init__(self, conread=None, conwrite=None):
        self.conread = conread
        self.conwrite = conwrite

    def fill(self, lower, upper, data):
        pass

    def load(self, filename):
        pass

    def read(self, address, poll):
        if address == 0xF004:
            return self.conread(poll)
        else:
            return None

    def write(self, address, data):
        if address == 0xF001:
            self.conwrite(data)

