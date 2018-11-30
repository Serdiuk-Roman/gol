

class Cell:

    def __init__(self, field, live, cord_x, cord_y):
        self.field = field
        self.live = live
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.next_live = False
        self.neiborhuds = 0

    def check_cell(self, index_x, index_y):
        if index_y < 0:
            index_y = len(self.field) + index_y
        if index_y >= len(self.field):
            index_y = index_y % len(self.field)
        if index_x < 0:
            index_x = len(self.field[0]) + index_x
        if index_x >= len(self.field[0]):
            index_x = index_x % len(self.field[0])

        if self.field[index_y][index_x].live:
            self.neiborhuds += 1

    def coun_neib_in_line(self, index_y):
        self.check_cell(self.cord_x - 1, index_y)
        self.check_cell(self.cord_x, index_y)
        self.check_cell(self.cord_x + 1, index_y)

    def count_neib(self):
        self.neiborhuds = 0

        self.check_cell(self.cord_x - 1, self.cord_y)
        self.check_cell(self.cord_x + 1, self.cord_y)

        self.coun_neib_in_line(self.cord_y - 1)
        self.coun_neib_in_line(self.cord_y + 1)

    def is_a_live(self):
        self.count_neib()

        if self.live and self.neiborhuds < 2:
            self.next_live = False
        if self.live and (self.neiborhuds in [2, 3]):
            self.next_live = True
        if self.live and self.neiborhuds > 3:
            self.next_live = False
        if not self.live and self.neiborhuds == 3:
            self.next_live = True

    def set_next_step(self):
        self.live = self.next_live
