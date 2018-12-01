#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cell:

    def __init__(self, observer, live, cord_x, cord_y):
        self.observer = observer
        self.live = live
        self.next_live = False
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.neighbors = 0

    def check_cell(self, index_x, index_y):
        if index_y < 0:
            index_y = self.observer.height + index_y
        if index_y >= self.observer.height:
            index_y = index_y % self.observer.height
        if index_x < 0:
            index_x = self.observer.width + index_x
        if index_x >= self.observer.width:
            index_x = index_x % self.observer.width

        if self.observer.field[index_y][index_x].live:
            self.neighbors += 1

    def coun_neighbors_in_line(self, index_y):
        self.check_cell(self.cord_x - 1, index_y)
        self.check_cell(self.cord_x, index_y)
        self.check_cell(self.cord_x + 1, index_y)

    def count_neighbors(self):
        self.neighbors = 0

        self.check_cell(self.cord_x - 1, self.cord_y)
        self.check_cell(self.cord_x + 1, self.cord_y)

        self.coun_neighbors_in_line(self.cord_y - 1)
        self.coun_neighbors_in_line(self.cord_y + 1)

    def is_alive(self):
        self.count_neighbors()

        if not self.live and self.neighbors == 3:
            self.next_live = True
            return True
        if self.live and self.neighbors < 2:
            self.next_live = False
            return True
        if self.live and (self.neighbors in [2, 3]):
            self.next_live = True
            return
        if self.live and self.neighbors > 3:
            self.next_live = False
            return True

    def next_step(self):
        self.live = self.next_live
