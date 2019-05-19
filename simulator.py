import time
import curswin
import curses
import configparser


keys = []

mem_rd_proc = []
mem_wr_proc = []


def _conread(poll):
    if keys:
        if poll:
            return keys[-1]
        else:
            return keys.pop()
    else:
        return 0


def _conwrite(data):
    wmain.addstr(chr(data))


def _memrd(addr, poll=False):
    for p in mem_rd_proc:
        d = p(addr, poll)
        if d is not None:
            return d

    return 0xFF


def _memwr(addr, data):
    for p in mem_wr_proc:
        p(addr, data)
    return


wc = curswin.WinColl()
wmenu = wc.addwin(align="top", title="menu", size=1,
                  fill=" ", border=0)
wstat = wc.addwin(align="bottom", title="status", size=1,
                  fill=" ", fg=curswin.BLACK, bg=curswin.GREEN, border=0)
wkbuf = wc.addwin(align="bottom", title="keybuf", size=1,
                  fill=" ", fg=curswin.CYAN, border=0)
wmem  = wc.addwin(align="left", title="memory", size=20,
                  fill=" ", fg=curswin.WHITE, bg=curswin.CYAN)
wproc = wc.addwin(align="bottom", title="processor", size=3,
                  fill=" ", fg=curswin.YELLOW, bg=curswin.RED)
wasm  = wc.addwin(align="right", title="assembly", size=30,
                  fill=" ", fg=curswin.WHITE, bg=curswin.BLUE)
wmain = wc.addwin(align="fill", title="main", size=0,
                  fill=" ", fg=curswin.YELLOW, bg=curswin.BLACK, border=0, cursor=True)

wc.setsize()

wmenu.addstr(0, 0, "F", curswin.UNDERLINE)
wmenu.addstr("ile ")
wmenu.addstr("E", curswin.UNDERLINE)
wmenu.addstr("dit ")


config = configparser.ConfigParser()
config.read("simulator.ini")

for section in config.sections():

    if config.has_option(section, 'type'):
        tp = config.get(section, 'type')

        if tp == "mem":
            mtype = "mod_" + config.get(section, 'module')
            exec("import " + mtype)
            memory = eval(mtype + ".cells(_conread, _conwrite)")

            if config.has_option(section, "start"):
                msta = int(config.get(section, 'start'), 0)
                mend = int(config.get(section, 'end'), 0)
                mfil = int(config.get(section, 'fill'), 0)
                memory.fill(msta, mend, mfil)

            if config.has_option(section, 'initfile'):
                memory.load(config.get(section, 'initfile'))

            mem_rd_proc.append(memory.read)
            mem_wr_proc.append(memory.write)

        elif tp == "cpu":
            mtype = "mod_" + config.get(section, 'module')
            exec("import " + mtype)
            cpu = eval(mtype + ".cpu(debug=0)")
            cpu.addmem(_memrd, _memwr)


#cpu = core65.Core65(debug=0)
#cpu.addmem(memory.read, memory.write)
#cpu.addmem(ioread, iowrite)
#cpu.addmem(_memrd, _memwr)


termchars = []
for c in range(32, 128):
    termchars += [c]

termchars += [ord("C") - 64]
termchars += [ord("X") - 64]
termchars += [ord("H") - 64]


#wproc.addstr(0, 0, str(cpu))
nexttime = time.monotonic()
timeres = 0.5

runstate = "halt"

while True:

    c = wc.getch()

    if c != curses.ERR:
        try:
            n = curses.keyname(c).decode("ASCII")
        except:
            n = "---"

        wmem.addstr("\n{:6.6} {:b}\n{:10}".format(str(c), (c in termchars), n))
        wmem.refresh()

        if c in termchars:
            keys.insert(0, c)

        elif c == ord('Q') - 64:
            quit()

        elif c == curses.KEY_DOWN:
            wmain.pad.scroll(1)
            wmain.refresh()

        elif c == curses.KEY_UP:
            pass

        elif c == curses.KEY_F8:
            wmem.pad.clear()
            wasm.pad.clear()
            wc.setsize()

        elif c == curses.KEY_F2:
            runstate = "halt"

        elif c == curses.KEY_F3:
            runstate = "run"

        elif c == curses.KEY_F4:
            runstate = "step"
            nexttime = time.monotonic()

        elif c == curses.KEY_RESIZE:
            wc.setsize()

        elif c == curses.KEY_MOUSE:
            try:
                cm = curses.getmouse()
            except:
                cm = None

            # wasm.addstr("{:20.20}\n{:08x}\n".format(str(cm), cm[4]))
            # wasm.refresh()

    if runstate in ["run", "step"]:
        wasm.pad.addstr("\n{}".format(cpu.disasm()))
        cpu.exec()
        if runstate == "step":
            runstate = "halt"

    if time.monotonic() > nexttime:
        nexttime = time.monotonic() + timeres
        wproc.addstr("\n{:4} {} {}".format(runstate, str(cpu), cpu.disasm()))
        wstat.addstr("\n{}".format(str(time.asctime(time.localtime()))))
        wkbuf.addstr("\n{}".format(str(keys)))
        wasm.refresh()

