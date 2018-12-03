#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

from cells import Cell


class Field:
    def __init__(self):
        self.height = 22
        self.width = 78
        self.field = []
        self.density = random.randint(3, 7)

    def set_alive(self):
        chance = random.randint(0, 10)
        return chance >= self.density

    def gen_field(self):
        for row in range(self.height):
            self.field.append([])
            for cell in range(self.width):
                cell = Cell(
                    self,
                    self.set_alive(),
                    cell,
                    row
                )
                self.field[row].append(cell)

    def check_alive(self):
        for row in self.field:
            for cell in row:
                cell.is_alive()

    def make_step(self):
        for row in self.field:
            for cell in row:
                cell.next_step()

    def make_mask(self):
        mask = [
            [cell.live for cell in row]
            for row in self.field
        ]
        return mask
