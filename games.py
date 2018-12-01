#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from fields import Field


class Game:
    def __init__(self):
        self.place = None
        self.current = []
        self.previous_step = []
        self.two_steps_ago = []
        self.stop = False

    def init_place(self):

        self.place = Field()
        self.place.gen_field()
        self.current = self.place.make_mask()

    def check_prev_steps(self):
        self.current = self.place.make_mask()

        if self.current == self.previous_step:
            return True
        elif self.current == self.two_steps_ago:
            return True
        else:
            self.two_steps_ago = self.previous_step
            self.previous_step = self.current
            return False

    def step(self):
        self.place.check_alive()
        self.place.make_step()
        if self.check_prev_steps():
            self.stop = True


