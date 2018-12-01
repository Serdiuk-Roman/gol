#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import curses
import time

from fields import Field


class Game:
    def __init__(self):
        self.place = None
        self.previous_step = []
        self.two_steps_back = []

    def init_place(self):
        # y, x, d = self.dialog()

        self.place = Field(12, 24, 5)
        self.place.gen_field()

    def check_prev_steps(self):
        current = self.place.make_mask()

        if current == self.previous_step:
            return True
        elif current == self.two_steps_ago:
            return True
        else:
            self.two_steps_ago = self.previous_step
            self.previous_step = current
            return False

    def run(self):
        while True:
            self.place.show_field()
            self.place.check_alive()
            self.place.step()
            if self.check_prev_steps():
                self.place.show_field()
                print("Все закончилося или зависло")
                break
            time.sleep(0.5)

    def dialog(self):
        y = input("height(def:10) : ")
        if not y:
            y = 10
        else:
            y = int(y)
        x = input("width(def:20) : ")
        if not x:
            x = 20
        else:
            x = int(x)
        d = input("density([1:9]def:5) : ")
        if not d:
            d = 5
        else:
            d = int(d)
        return y, x, d


if __name__ == "__main__":
    g = Game()
    g.init_place()
    g.run()
