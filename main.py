#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

from games import Game


class Manager:
    def __init__(self, stdscr):
        self.game = Game()
        self.stdscr = stdscr
        curses.curs_set(0)

    def run(self):
        self.stdscr.clear()
        self.stdscr.border(0)

        self.game.init_place()
        while True:
            rows = self.render()
            for i in range(len(rows)):
                self.stdscr.addstr(i + 1, 1, rows[i])
            self.stdscr.refresh()
            if self.game.stop:
                break
            self.game.step()
            time.sleep(0.1)
        self.stdscr.addstr(23, 7, "  Все закончилося или зависло  ")
        self.stdscr.refresh()
        self.stdscr.getch()

    def render(self):
        rows = []
        for row in self.game.current:
            line = "".join([str(cell) for cell in row])
            line = line.replace("True", "0")
            line = line.replace("False", " ")
            rows.append(line)
        return rows

    def __del__(self):
        curses.endwin()


if __name__ == "__main__":
    m = curses.wrapper(Manager)
    m.run()
