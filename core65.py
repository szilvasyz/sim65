class Core65:

    _instructions = {
        0x00: 'BRK', 0x01: 'ORA', 0x02: '---', 0x03: '---', 0x04: '---', 0x05: 'ORA', 0x06: 'ASL', 0x07: '---',
        0x08: 'PHP', 0x09: 'ORA', 0x0A: 'ASL', 0x0B: '---', 0x0C: '---', 0x0D: 'ORA', 0x0E: 'ASL', 0x0F: '---',
        0x10: 'BPL', 0x11: 'ORA', 0x12: '---', 0x13: '---', 0x14: '---', 0x15: 'ORA', 0x16: 'ASL', 0x17: '---',
        0x18: 'CLC', 0x19: 'ORA', 0x1A: '---', 0x1B: '---', 0x1C: '---', 0x1D: 'ORA', 0x1E: 'ASL', 0x1F: '---',
        0x20: 'JSR', 0x21: 'AND', 0x22: '---', 0x23: '---', 0x24: 'BIT', 0x25: 'AND', 0x26: 'ROL', 0x27: '---',
        0x28: 'PLP', 0x29: 'AND', 0x2A: 'ROL', 0x2B: '---', 0x2C: 'BIT', 0x2D: 'AND', 0x2E: 'ROL', 0x2F: '---',
        0x30: 'BMI', 0x31: 'AND', 0x32: '---', 0x33: '---', 0x34: '---', 0x35: 'AND', 0x36: 'ROL', 0x37: '---',
        0x38: 'SEC', 0x39: 'AND', 0x3A: '---', 0x3B: '---', 0x3C: '---', 0x3D: 'AND', 0x3E: 'ROL', 0x3F: '---',
        0x40: 'RTI', 0x41: 'EOR', 0x42: '---', 0x43: '---', 0x44: '---', 0x45: 'EOR', 0x46: 'LSR', 0x47: '---',
        0x48: 'PHA', 0x49: 'EOR', 0x4A: 'LSR', 0x4B: '---', 0x4C: 'JMP', 0x4D: 'EOR', 0x4E: 'LSR', 0x4F: '---',
        0x50: 'BVC', 0x51: 'EOR', 0x52: '---', 0x53: '---', 0x54: '---', 0x55: 'EOR', 0x56: 'LSR', 0x57: '---',
        0x58: 'CLI', 0x59: 'EOR', 0x5A: '---', 0x5B: '---', 0x5C: '---', 0x5D: 'EOR', 0x5E: 'LSR', 0x5F: '---',
        0x60: 'RTS', 0x61: 'ADC', 0x62: '---', 0x63: '---', 0x64: '---', 0x65: 'ADC', 0x66: 'ROR', 0x67: '---',
        0x68: 'PLA', 0x69: 'ADC', 0x6A: 'ROR', 0x6B: '---', 0x6C: 'JMP', 0x6D: 'ADC', 0x6E: 'ROR', 0x6F: '---',
        0x70: 'BVS', 0x71: 'ADC', 0x72: '---', 0x73: '---', 0x74: '---', 0x75: 'ADC', 0x76: 'ROR', 0x77: '---',
        0x78: 'SEI', 0x79: 'ADC', 0x7A: '---', 0x7B: '---', 0x7C: '---', 0x7D: 'ADC', 0x7E: 'ROR', 0x7F: '---',
        0x80: '---', 0x81: 'STA', 0x82: '---', 0x83: '---', 0x84: 'STY', 0x85: 'STA', 0x86: 'STX', 0x87: '---',
        0x88: 'DEY', 0x89: '---', 0x8A: 'TXA', 0x8B: '---', 0x8C: 'STY', 0x8D: 'STA', 0x8E: 'STX', 0x8F: '---',
        0x90: 'BCC', 0x91: 'STA', 0x92: '---', 0x93: '---', 0x94: 'STY', 0x95: 'STA', 0x96: 'STX', 0x97: '---',
        0x98: 'TYA', 0x99: 'STA', 0x9A: 'TXS', 0x9B: '---', 0x9C: '---', 0x9D: 'STA', 0x9E: '---', 0x9F: '---',
        0xA0: 'LDY', 0xA1: 'LDA', 0xA2: 'LDX', 0xA3: '---', 0xA4: 'LDY', 0xA5: 'LDA', 0xA6: 'LDX', 0xA7: '---',
        0xA8: 'TAY', 0xA9: 'LDA', 0xAA: 'TAX', 0xAB: '---', 0xAC: 'LDY', 0xAD: 'LDA', 0xAE: 'LDX', 0xAF: '---',
        0xB0: 'BCS', 0xB1: 'LDA', 0xB2: '---', 0xB3: '---', 0xB4: 'LDY', 0xB5: 'LDA', 0xB6: 'LDX', 0xB7: '---',
        0xB8: 'CLV', 0xB9: 'LDA', 0xBA: 'TSX', 0xBB: '---', 0xBC: 'LDY', 0xBD: 'LDA', 0xBE: 'LDX', 0xBF: '---',
        0xC0: 'CPY', 0xC1: 'CMP', 0xC2: '---', 0xC3: '---', 0xC4: 'CPY', 0xC5: 'CMP', 0xC6: 'DEC', 0xC7: '---',
        0xC8: 'INY', 0xC9: 'CMP', 0xCA: 'DEX', 0xCB: '---', 0xCC: 'CPY', 0xCD: 'CMP', 0xCE: 'DEC', 0xCF: '---',
        0xD0: 'BNE', 0xD1: 'CMP', 0xD2: '---', 0xD3: '---', 0xD4: '---', 0xD5: 'CMP', 0xD6: 'DEC', 0xD7: '---',
        0xD8: 'CLD', 0xD9: 'CMP', 0xDA: '---', 0xDB: '---', 0xDC: '---', 0xDD: 'CMP', 0xDE: 'DEC', 0xDF: '---',
        0xE0: 'CPX', 0xE1: 'SBC', 0xE2: '---', 0xE3: '---', 0xE4: 'CPX', 0xE5: 'SBC', 0xE6: 'INC', 0xE7: '---',
        0xE8: 'INX', 0xE9: 'SBC', 0xEA: 'NOP', 0xEB: '---', 0xEC: 'CPX', 0xED: 'SBC', 0xEE: 'INC', 0xEF: '---',
        0xF0: 'BEQ', 0xF1: 'SBC', 0xF2: '---', 0xF3: '---', 0xF4: '---', 0xF5: 'SBC', 0xF6: 'INC', 0xF7: '---',
        0xF8: 'SED', 0xF9: 'SBC', 0xFA: '---', 0xFB: '---', 0xFC: '---', 0xFD: 'SBC', 0xFE: 'INC', 0xFF: '---'
    }
    _addrmodes = {
        0x00: 'imp', 0x01: 'X,i', 0x02: '---', 0x03: '---', 0x04: '---', 0x05: 'zpg', 0x06: 'zpg', 0x07: '---',
        0x08: 'imp', 0x09: 'imm', 0x0A: 'Acc', 0x0B: '---', 0x0C: '---', 0x0D: 'abs', 0x0E: 'abs', 0x0F: '---',
        0x10: 'rel', 0x11: 'i,Y', 0x12: '---', 0x13: '---', 0x14: '---', 0x15: 'z,X', 0x16: 'z,X', 0x17: '---',
        0x18: 'imp', 0x19: 'a,Y', 0x1A: '---', 0x1B: '---', 0x1C: '---', 0x1D: 'a,X', 0x1E: 'a,X', 0x1F: '---',
        0x20: 'abs', 0x21: 'X,i', 0x22: '---', 0x23: '---', 0x24: 'zpg', 0x25: 'zpg', 0x26: 'zpg', 0x27: '---',
        0x28: 'imp', 0x29: 'imm', 0x2A: 'Acc', 0x2B: '---', 0x2C: 'abs', 0x2D: 'abs', 0x2E: 'abs', 0x2F: '---',
        0x30: 'rel', 0x31: 'i,Y', 0x32: '---', 0x33: '---', 0x34: '---', 0x35: 'z,X', 0x36: 'z,X', 0x37: '---',
        0x38: 'imp', 0x39: 'a,Y', 0x3A: '---', 0x3B: '---', 0x3C: '---', 0x3D: 'a,X', 0x3E: 'a,X', 0x3F: '---',
        0x40: 'imp', 0x41: 'X,i', 0x42: '---', 0x43: '---', 0x44: '---', 0x45: 'zpg', 0x46: 'zpg', 0x47: '---',
        0x48: 'imp', 0x49: 'imm', 0x4A: 'Acc', 0x4B: '---', 0x4C: 'abs', 0x4D: 'abs', 0x4E: 'abs', 0x4F: '---',
        0x50: 'rel', 0x51: 'i,Y', 0x52: '---', 0x53: '---', 0x54: '---', 0x55: 'z,X', 0x56: 'z,X', 0x57: '---',
        0x58: 'imp', 0x59: 'a,Y', 0x5A: '---', 0x5B: '---', 0x5C: '---', 0x5D: 'a,X', 0x5E: 'a,X', 0x5F: '---',
        0x60: 'imp', 0x61: 'X,i', 0x62: '---', 0x63: '---', 0x64: '---', 0x65: 'zpg', 0x66: 'zpg', 0x67: '---',
        0x68: 'imp', 0x69: 'imm', 0x6A: 'Acc', 0x6B: '---', 0x6C: 'ind', 0x6D: 'abs', 0x6E: 'abs', 0x6F: '---',
        0x70: 'rel', 0x71: 'i,Y', 0x72: '---', 0x73: '---', 0x74: '---', 0x75: 'z,X', 0x76: 'z,X', 0x77: '---',
        0x78: 'imp', 0x79: 'a,Y', 0x7A: '---', 0x7B: '---', 0x7C: '---', 0x7D: 'a,X', 0x7E: 'a,X', 0x7F: '---',
        0x80: '---', 0x81: 'X,i', 0x82: '---', 0x83: '---', 0x84: 'zpg', 0x85: 'zpg', 0x86: 'zpg', 0x87: '---',
        0x88: 'imp', 0x89: '---', 0x8A: 'imp', 0x8B: '---', 0x8C: 'abs', 0x8D: 'abs', 0x8E: 'abs', 0x8F: '---',
        0x90: 'rel', 0x91: 'i,Y', 0x92: '---', 0x93: '---', 0x94: 'z,X', 0x95: 'z,X', 0x96: 'z,Y', 0x97: '---',
        0x98: 'imp', 0x99: 'a,Y', 0x9A: 'imp', 0x9B: '---', 0x9C: '---', 0x9D: 'a,X', 0x9E: '---', 0x9F: '---',
        0xA0: 'imm', 0xA1: 'X,i', 0xA2: 'imm', 0xA3: '---', 0xA4: 'zpg', 0xA5: 'zpg', 0xA6: 'zpg', 0xA7: '---',
        0xA8: 'imp', 0xA9: 'imm', 0xAA: 'imp', 0xAB: '---', 0xAC: 'abs', 0xAD: 'abs', 0xAE: 'abs', 0xAF: '---',
        0xB0: 'rel', 0xB1: 'i,Y', 0xB2: '---', 0xB3: '---', 0xB4: 'z,X', 0xB5: 'z,X', 0xB6: 'z,Y', 0xB7: '---',
        0xB8: 'imp', 0xB9: 'a,Y', 0xBA: 'imp', 0xBB: '---', 0xBC: 'a,X', 0xBD: 'a,X', 0xBE: 'a,Y', 0xBF: '---',
        0xC0: 'imm', 0xC1: 'X,i', 0xC2: '---', 0xC3: '---', 0xC4: 'zpg', 0xC5: 'zpg', 0xC6: 'zpg', 0xC7: '---',
        0xC8: 'imp', 0xC9: 'imm', 0xCA: 'imp', 0xCB: '---', 0xCC: 'abs', 0xCD: 'abs', 0xCE: 'abs', 0xCF: '---',
        0xD0: 'rel', 0xD1: 'i,Y', 0xD2: '---', 0xD3: '---', 0xD4: '---', 0xD5: 'z,X', 0xD6: 'z,X', 0xD7: '---',
        0xD8: 'imp', 0xD9: 'a,Y', 0xDA: '---', 0xDB: '---', 0xDC: '---', 0xDD: 'a,X', 0xDE: 'a,X', 0xDF: '---',
        0xE0: 'imm', 0xE1: 'X,i', 0xE2: '---', 0xE3: '---', 0xE4: 'zpg', 0xE5: 'zpg', 0xE6: 'zpg', 0xE7: '---',
        0xE8: 'imp', 0xE9: 'imm', 0xEA: 'imp', 0xEB: '---', 0xEC: 'abs', 0xED: 'abs', 0xEE: 'abs', 0xEF: '---',
        0xF0: 'rel', 0xF1: 'i,Y', 0xF2: '---', 0xF3: '---', 0xF4: '---', 0xF5: 'z,X', 0xF6: 'z,X', 0xF7: '---',
        0xF8: 'imp', 0xF9: 'a,Y', 0xFA: '---', 0xFB: '---', 0xFC: '---', 0xFD: 'a,X', 0xFE: 'a,X', 0xFF: '---'
    }

    def __init__(self, debug=0):
        self.mem_rd_proc = []
        self.mem_wr_proc = []

        self.bitN = 0x80
        self.bitV = 0x40
        self.bitR = 0x20
        self.bitB = 0x10
        self.bitD = 0x08
        self.bitI = 0x04
        self.bitZ = 0x02
        self.bitC = 0x01

        self.flags = dict()
        self.regs = dict()
        
        self.flags["N"] = 0
        self.flags["V"] = 0
        self.flags["R"] = 1
        self.flags["B"] = 0
        self.flags["D"] = 0
        self.flags["I"] = 0
        self.flags["Z"] = 0
        self.flags["C"] = 0

        self.regs["A"] = 0
        self.regs["X"] = 0
        self.regs["Y"] = 0
        self.regs["S"] = 0
        self.regs["PC"] = 0
        self.cpu_state = 'reset'
        self.opr = 0
        self.res = 0

        self.debug = debug

    def __str__(self):
        return "S:{:5} PC={:04X} A={:02X} X={:02X} Y={:02X} S={:02X} P={:02X}".format(
            self.cpu_state,
            self.regs["PC"], self.regs["A"],
            self.regs["X"], self.regs["Y"],
            self.regs["S"], self._getpreg()
        )

    def _getpreg(self):
        return self.flags["N"] * self.bitN | \
               self.flags["V"] * self.bitV | \
               self.flags["R"] * self.bitR | \
               self.flags["B"] * self.bitB | \
               self.flags["D"] * self.bitD | \
               self.flags["I"] * self.bitI | \
               self.flags["Z"] * self.bitZ | \
               self.flags["C"] * self.bitC
    
    def _setpreg(self, bval):
        self.flags["N"] = 1 if bval & self.bitN else 0
        self.flags["V"] = 1 if bval & self.bitV else 0
        self.flags["R"] = 1 if bval & self.bitR else 0
        self.flags["B"] = 1 if bval & self.bitB else 0
        self.flags["D"] = 1 if bval & self.bitD else 0
        self.flags["I"] = 1 if bval & self.bitI else 0
        self.flags["Z"] = 1 if bval & self.bitZ else 0
        self.flags["C"] = 1 if bval & self.bitC else 0
        return

    def _memrd(self, addr, poll=False):
        for p in self.mem_rd_proc:
            d = p(addr, poll)
            if d is not None:
                return d

        return 0xFF

    def _memwr(self, addr, data):
        for p in self.mem_wr_proc:
            p(addr, data)
        return 

    def _fetch(self):
        fb = self._memrd(self.regs["PC"])
        self.regs["PC"] = (self.regs["PC"] + 1) & 0xFFFF
        return fb

    def _push(self, data):
        self._memwr(0x100 + self.regs["S"], data)
        self.regs["S"] = (self.regs["S"] - 1) & 0xFF

    def _pop(self):
        self.regs["S"] = (self.regs["S"] + 1) & 0xFF
        return self._memrd(0x100 + self.regs["S"])

    def addmem(self, read_proc, write_proc):
        self.mem_rd_proc.append(read_proc)
        self.mem_wr_proc.append(write_proc)

    def disasm(self, address=None):
        if address is None:
            address = self.regs["PC"]
        opcode = self._memrd(address, True)
        memst = "{:02X} ".format(opcode)
        oper1 = self._memrd((address + 1) & 0xFFFF, True)
        oper2 = self._memrd((address + 2) & 0xFFFF, True)
        dbyte = "${:02X}".format(oper1)
        dword = "${:04X}".format(oper1 + (oper2 << 8))
        instr = self._instructions[opcode] + " "
        amode = self._addrmodes[opcode]
        oplen = 0

        if amode == '---':
            pass
        elif amode == 'abs':
            instr += dword
            oplen = 2
        elif amode == 'Acc':
            instr += 'A'
        elif amode == 'a,X':
            instr += dword + ",X"
            oplen = 2
        elif amode == 'a,Y':
            instr += dword + ",Y"
            oplen = 2
        elif amode == 'imm':
            instr += "#" + dbyte
            oplen = 1
        elif amode == 'imp':
            pass
        elif amode == 'ind':
            instr += "(" + dword + ")"
            oplen = 2
        elif amode == 'i,Y':
            instr += "(" + dbyte + "),Y"
            oplen = 1
        elif amode == 'rel':
            address += 2 + oper1 + 0x10000
            if oper1 & 0x80:
                address -= 256
            address = address & 0xFFFF
            instr += "${:04X}".format(address)
            oplen = 1
        elif amode == 'X,i':
            instr += "(" + dbyte + ",X)"
            oplen = 1
        elif amode == 'zpg':
            instr += dbyte
            oplen = 1
        elif amode == 'z,X':
            instr += dbyte + ",X"
            oplen = 1
        elif amode == 'z,Y':
            instr += dbyte + ",Y"
            oplen = 1

        if oplen != 0:
            memst += "{:02X} ".format(oper1)
        if oplen == 2:
            memst += "{:02X} ".format(oper2)

        return "{:9}{:11}".format(memst, instr)

    def exec(self):
        if self.cpu_state == 'run':
            self._decode(self._fetch())

        elif self.cpu_state == 'reset':
            self.regs["PC"] = self._memrd(0xFFFC)
            self.regs["PC"] |= (self._memrd(0xFFFD) << 8)
            self.cpu_state = 'run'
        else:
            pass

    def _decode(self, opcode):
        instr = self._instructions[opcode]
        amode = self._addrmodes[opcode]

        if self.debug:
            print(instr, " ", amode)

        self.opr = self._getoper(amode)
        self._doinst(instr)

    def _getoper(self, amode):

        oper = 0x10000

        if amode == '---':
            pass
        elif amode == 'abs':
            oper = self._fetch()
            oper |= self._fetch() << 8
        elif amode == 'Acc':
            oper = 'A'
        elif amode == 'a,X':
            oper = self._fetch()
            oper |= self._fetch() << 8
            oper = (oper + self.regs["X"]) & 0xFFFF
        elif amode == 'a,Y':
            oper = self._fetch()
            oper |= self._fetch() << 8
            oper = (oper + self.regs["Y"]) & 0xFFFF
        elif amode == 'imm':
            oper = self.regs["PC"]
            self.regs["PC"] += 1
        elif amode == 'imp':
            pass
        elif amode == 'ind':
            addr = self._fetch()
            addr |= self._fetch() << 8
            oper = self._memrd(addr)
            oper |= (self._memrd((addr + 1) & 0xFFFF) << 8)
        elif amode == 'i,Y':
            oper = self._fetch()
            addr = self._memrd(oper)
            addr |= (self._memrd((oper + 1) & 0xFF) << 8)
            oper = (addr + self.regs["Y"]) & 0xFFFF
        elif amode == 'rel':
            oper = self._fetch()
            if oper & 0x80:
                oper -= 256
            oper += self.regs["PC"]
        elif amode == 'X,i':
            oper = (self._fetch() + self.regs["X"]) & 0xFF
            addr = self._memrd(oper)
            addr |= (self._memrd((oper + 1) & 0xFF) << 8)
            oper = addr
        elif amode == 'zpg':
            oper = self._fetch()
        elif amode == 'z,X':
            oper = (self._fetch() + self.regs["X"]) & 0xFF
        elif amode == 'z,Y':
            oper = (self._fetch() + self.regs["Y"]) & 0xFF

        return oper

    def _doinst(self, instr):

        if instr == '---':
            pass

        elif instr == 'ADC':

            opr = self._memrd(self.opr)
            res = self.regs["A"] + opr + self.flags["C"]

            if self.flags["D"]:
                if (res & 0x0F > 0x09) or ((self.regs["A"] ^ opr ^ res) & 0x10):
                    res += 0x06
                if ((res & 0xF0) > 0x90) or (res & 0x100):
                    res += 0x60

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["V"] = 1 if (res ^ self.regs["A"]) & (res ^ opr) & 0x80 else 0
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'AND':
            opr = self._memrd(self.opr)
            res = self.regs["A"] & opr
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'ASL':
            if self.opr == 'A':
                res = self.regs["A"]
            else:
                res = self._memrd(self.opr)

            res = (res << 1)
            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            if self.opr == 'A':
                self.regs["A"] = res
            else:
                self._memwr(self.opr, res)

        elif instr == 'BCC':
            if self.flags["C"] == 0:
                self.regs["PC"] = self.opr

        elif instr == 'BCS':
            if self.flags["C"]:
                self.regs["PC"] = self.opr

        elif instr == 'BEQ':
            if self.flags["Z"]:
                self.regs["PC"] = self.opr

        elif instr == 'BIT':
            res = self._memrd(self.opr)
            self.flags["N"] = 1 if res & 0x80 else 0
            self.flags["V"] = 1 if res & 0x40 else 0
            self.flags["Z"] = 1 if (res & self.regs["A"]) == 0 else 0

        elif instr == 'BMI':
            if self.flags["N"]:
                self.regs["PC"] = self.opr

        elif instr == 'BNE':
            if self.flags["Z"] == 0:
                self.regs["PC"] = self.opr

        elif instr == 'BPL':
            if self.flags["N"] == 0:
                self.regs["PC"] = self.opr

        elif instr == 'BRK':
            self._fetch()
            self._push(self.regs["PC"] >> 8)
            self._push(self.regs["PC"] & 0xFF)
            self._push(self._getpreg() | self.bitB | self.bitR)
            self.flags["I"] = 1
            self.regs["PC"] = self._memrd(0xFFFE)
            self.regs["PC"] |= self._memrd(0xFFFF) << 8

        elif instr == 'BVC':
            if self.flags["V"] == 0:
                self.regs["PC"] = self.opr

        elif instr == 'BVS':
            if self.flags["V"]:
                self.regs["PC"] = self.opr

        elif instr == 'CLC':
            self.flags["C"] = 0

        elif instr == 'CLD':
            self.flags["D"] = 0

        elif instr == 'CLI':
            self.flags["I"] = 0

        elif instr == 'CLV':
            self.flags["V"] = 0

        elif instr == 'CMP':

            res = self.regs["A"] + (0xFF ^ self._memrd(self.opr)) + 1

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

        elif instr == 'CPX':

            res = self.regs["X"] + (0xFF ^ self._memrd(self.opr)) + 1

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

        elif instr == 'CPY':

            res = self.regs["Y"] + (0xFF ^ self._memrd(self.opr)) + 1

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

        elif instr == 'DEC':

            res = (self._memrd(self.opr) - 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self._memwr(self.opr, res)

        elif instr == 'DEX':

            res = (self.regs["X"] - 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["X"] = res

        elif instr == 'DEY':

            res = (self.regs["Y"] - 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["Y"] = res

        elif instr == 'EOR':

            res = (self.regs["A"] ^ self._memrd(self.opr)) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'INC':

            res = (self._memrd(self.opr) + 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self._memwr(self.opr, res)

        elif instr == 'INX':

            res = (self.regs["X"] + 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["X"] = res

        elif instr == 'INY':

            res = (self.regs["Y"] + 1) & 0xFF

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["Y"] = res

        elif instr == 'JMP':
            self.regs["PC"] = self.opr

        elif instr == 'JSR':
            addr = (self.regs["PC"] - 1) & 0xFFFF
            self._push(addr >> 8)
            self._push(addr & 0xFF)
            self.regs["PC"] = self.opr

        elif instr == 'LDA':

            res = self._memrd(self.opr)

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'LDX':
            res = self._memrd(self.opr)

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["X"] = res

        elif instr == 'LDY':

            res = self._memrd(self.opr)

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["Y"] = res

        elif instr == 'LSR':

            if self.opr == 'A':
                res = self.regs["A"]
            else:
                res = self._memrd(self.opr)

            self.flags["C"] = 1 if res & 0x01 else 0
            res = (res >> 1)
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            if self.opr == 'A':
                self.regs["A"] = res
            else:
                self._memwr(self.opr, res)

        elif instr == 'NOP':
            pass

        elif instr == 'ORA':

            res = self.regs["A"] | self._memrd(self.opr)

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'PHA':
            self._push(self.regs["A"])

        elif instr == 'PHP':
            self._push(self._getpreg() | self.bitR | self.bitB)

        elif instr == 'PLA':
            res = self._pop()

            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'PLP':
            self._setpreg(self._pop())

        elif instr == 'ROL':
            if self.opr == 'A':
                res = self.regs["A"]
            else:
                res = self._memrd(self.opr)

            res = (res << 1) | (1 if self.flags["C"] else 0)

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            if self.opr == 'A':
                self.regs["A"] = res
            else:
                self._memwr(self.opr, res)

        elif instr == 'ROR':
            if self.opr == 'A':
                res = self.regs["A"]
            else:
                res = self._memrd(self.opr)

            res |= 0x100 if self.flags["C"] else 0

            self.flags["C"] = 1 if res & 0x01 else 0
            res = res >> 1
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            if self.opr == 'A':
                self.regs["A"] = res
            else:
                self._memwr(self.opr, res)

        elif instr == 'RTI':
            self._setpreg(self._pop())
            addr = self._pop()
            addr |= self._pop() << 8
            self.regs["PC"] = addr

        elif instr == 'RTS':
            addr = self._pop()
            addr |= self._pop() << 8
            self.regs["PC"] = (addr + 1) & 0xFFFF

        elif instr == 'SBC':

            opr = self._memrd(self.opr) ^ 0xFF
            res = self.regs["A"] + opr + self.flags["C"]

            if self.flags["D"]:
                if ((res & 0x0F) > 0x09) or (((self.regs["A"] ^ opr ^ res) & 0x10) == 0):
                    res -= 0x06
                if ((res & 0xF0) > 0x90) or ((res & 0x100) == 0):
                    res -= 0x60

            self.flags["C"] = 1 if res & 0x100 else 0
            res &= 0xFF
            self.flags["V"] = 1 if (res ^ self.regs["A"]) & (res ^ opr) & 0x80 else 0
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0

            self.regs["A"] = res

        elif instr == 'SEC':
            self.flags["C"] = 1

        elif instr == 'SED':
            self.flags["D"] = 1

        elif instr == 'SEI':
            self.flags["I"] = 1

        elif instr == 'STA':
            self._memwr(self.opr, self.regs["A"])

        elif instr == 'STX':
            self._memwr(self.opr, self.regs["X"])

        elif instr == 'STY':
            self._memwr(self.opr, self.regs["Y"])

        elif instr == 'TAX':
            res = self.regs["A"]
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0
            self.regs["X"] = res

        elif instr == 'TAY':
            res = self.regs["A"]
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0
            self.regs["Y"] = res

        elif instr == 'TSX':
            res = self.regs["S"]
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0
            self.regs["X"] = res

        elif instr == 'TXA':
            res = self.regs["X"]
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0
            self.regs["A"] = res

        elif instr == 'TXS':
            res = self.regs["X"]
            self.regs["S"] = res

        elif instr == 'TYA':
            res = self.regs["Y"]
            self.flags["Z"] = 1 if res == 0 else 0
            self.flags["N"] = 1 if res & 0x80 else 0
            self.regs["A"] = res
