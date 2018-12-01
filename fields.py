#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

from cells import Cell


class Field:
    def __init__(self, height=22, width=78, density=3):
        self.height = height
        self.width = width
        self.field = []

        if density < 1:
            self.density = 1
        elif density > 9:
            self.density = 9
        else:
            self.density = density

    def set_cell(self):
        num = random.random()
        if num >= self.density / 10:
            return False
        else:
            return True

    def gen_field(self):
        for row in range(self.height):
            self.field.append([])
            for cell in range(self.width):
                cell = Cell(
                    self,
                    self.set_cell(),
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
        mask = [[cell.live for cell in row] for row in self.field]
        return mask
