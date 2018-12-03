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

    def changes(self):
        self.current = self.place.make_mask()

        if self.current == self.previous_step:
            return False
        elif self.current == self.two_steps_ago:
            return False
        else:
            self.two_steps_ago = self.previous_step
            self.previous_step = self.current
            return True

    def step(self):
        self.place.check_alive()
        self.place.make_step()
        if not self.changes():
            self.stop = True


