#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

from games import Game


class Manager:
    def __init__(self):
        self.game = Game()
        self.window = None

    def make_window(self):
        try:
            self.window = curses.initscr()
            self.window.clear()
            self.window.border(0)

            curses.noecho()
            curses.raw()
            curses.cbreak()

            self.run()

            self.window.refresh()
            self.window.getch()
        finally:
            curses.echo()
            curses.nocbreak()
            self.window.keypad(False)
            curses.endwin()

    def render(self):
        rows = []
        for row in self.game.current:
            line = ""
            for cell in row:
                if cell:
                    line = line + "0"
                else:
                    line = line + " "
            rows.append(line)
        return rows

    def run(self):
        self.game.init_place()
        while True:
            rows = self.render()
            for i in range(len(rows)):
                self.window.addstr(i + 1, 1, rows[i])
            self.window.addstr(23, 0, "")
            self.window.refresh()
            if self.game.stop:
                break
            self.game.step()
            time.sleep(0.2)
        self.window.addstr(23, 7, "Все закончилося или зависло")
        self.window.refresh()


if __name__ == "__main__":
    m = Manager()
    m.make_window()
