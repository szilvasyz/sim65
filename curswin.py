import curses
import atexit


BLACK   = curses.COLOR_BLACK
RED     = curses.COLOR_RED
GREEN   = curses.COLOR_GREEN
YELLOW  = curses.COLOR_YELLOW
BLUE    = curses.COLOR_BLUE
CYAN    = curses.COLOR_CYAN
MAGENTA = curses.COLOR_MAGENTA
WHITE   = curses.COLOR_WHITE

NORMAL    = curses.A_NORMAL
REVERSE   = curses.A_REVERSE
BOLD      = curses.A_BOLD
UNDERLINE = curses.A_UNDERLINE


class WinColl:

    class Win:

        def __init__(self, screen, number, align, title, size, fill, fg, bg, border, cursor):
            curses.init_pair(2 * number - 1, fg, bg)
            curses.init_pair(2 * number, bg, fg)
            self.border = border
            self.cursor = cursor
            self.title = title
            self.align = align
            self.size = size
            self.fill = fill
            self.topx = 0
            self.topy = 0
            self.maxx = 0
            self.maxy = 0
            self.number = number
            self.win = curses.newwin(0, 0)
            self.pad = curses.newpad(1000, 80)
            self.pad.scrollok(True)
            self.win.bkgd(self.fill, curses.color_pair(2 * number - 1))
            self.pad.bkgd(self.fill, curses.color_pair(2 * number - 1))
            self.pad.chgat(999, 0, 1,
                           curses.color_pair(2 * number) if cursor == 1 else curses.color_pair(2 * number - 1))
            self.win.nodelay(True)

        def __str__(self):
            topx, topy = self.win.getbegyx()
            maxx, maxy = self.win.getmaxyx()
            return "({:1}){:8} at {:03d}:{:03d}-{:03d}:{:03d}\n".format(self.fill, self.align, topx, topy, maxx, maxy)

        def setsize(self, topx, topy, maxx, maxy):
            self.topx = topx
            self.topy = topy
            self.maxx = maxx
            self.maxy = maxy
            self.win.resize(maxx, maxy)
            self.win.erase()
            self.win.mvwin(topx, topy)
            if self.border:
                self.win.border()
            self.win.addstr(0, 1, self.title)
            self.refresh()

        def refresh(self):
            try:
                self.win.refresh()
                bw = 1 if self.border else 0
                ml = self.win.getmaxyx()[0] - 2*bw
                self.pad.refresh(1000 - ml, 0,
                                 self.topx + bw, self.topy + bw,
                                 self.topx + self.maxx - 1 - bw, self.topy + self.maxy - 1 - bw
                                )
            except:
                pass

        def addstr(self, *args):
            if self.cursor:
                self.pad.chgat(1, curses.color_pair(2 * self.number) - 1)
            self.pad.addstr(*args)
            if self.cursor:
                self.pad.chgat(1, curses.color_pair(2 * self.number))
            self.refresh()

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.nodelay(True)
        self.screen.keypad(True)
        curses.mousemask(-1)
        curses.raw()
        curses.noecho()
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        self.winlist = []
        atexit.register(self.closewin)

    def __str__(self):
        s = ""
        for w in self.winlist:
            s += str(w)
        return s

    def getkey(self):
        try:
            k = self.screen.getkey()
        except:
            k = None
        finally:
            return k

    def getch(self):
        return self.screen.getch()

    def addwin(self, align="fill", title="", size=0, fill=" ",
               fg=WHITE, bg=BLACK, border=1, cursor=False):
        w = self.Win(screen=self.screen, number=len(self.winlist)+1,
                     align=align, title=title, size=size, fill=fill,
                     fg=fg, bg=bg, border=border, cursor=cursor)
        self.winlist.append(w)
        return w

    def closewin(self):
        curses.endwin()

    def setsize(self):
        try:
            curses.resize_term(0, 0)
            begx, begy = self.screen.getbegyx()
            maxx, maxy = self.screen.getmaxyx()
            self.screen.erase()

            for w in self.winlist:

                wbegx, wbegy = begx, begy
                wmaxx, wmaxy = maxx, maxy

                if w.align == "top":
                    wmaxx = w.size
                    begx += wmaxx
                    maxx -= wmaxx

                elif w.align == "bottom":
                    wmaxx = w.size
                    wbegx += maxx - wmaxx
                    maxx -= wmaxx

                elif w.align == "left":
                    wmaxy = w.size
                    begy += wmaxy
                    maxy -= wmaxy

                elif w.align == "right":
                    wmaxy = w.size
                    wbegy += maxy - wmaxy
                    maxy -= wmaxy

                elif w.align == "fill":
                    maxx = 0
                    maxy = 0
                    pass

                else:
                    wmaxx = 0
                    wmaxy = 0
                    pass

                w.setsize(wbegx, wbegy, wmaxx, wmaxy)
                w.refresh()

        except:
            pass

        finally:
            self.screen.untouchwin()
            self.screen.refresh()

