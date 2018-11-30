import random
import time

from cells import Cell


class Field:
    def __init__(self, height, weigth):
        self.height = height
        self.weigth = weigth
        self.field = []

    def inst_point(self):
        napovnenist = 0.7
        num = random.random()
        if num >= napovnenist:
            return True
        else:
            return False

    def gen_field(self):
        for row in range(self.height):
            self.field.append([])
            for cell in range(self.weigth):
                cell = Cell(
                    self.field,
                    self.inst_point(),
                    cell,
                    row
                )
                self.field[row].append(cell)

    def show_field(self):
        for row in self.field:
            show_row = []
            for cell in row:
                if cell.live:
                    show_row.append("O")
                else:
                    show_row.append("_")
            print(*show_row)

    def show_neib(self):
        for row in self.field:
            show_row = []
            for cell in row:
                show_row.append(cell.neiborhuds)
            print(*show_row)


# if __name__=="__main__":
field = Field(10, 20)
field.gen_field()
while True:
    # field.show_neib()
    field.show_field()
    for row in field.field:
        for cell in row:
            cell.is_a_live()
    for row in field.field:
        for cell in row:
            cell.set_next_step()
    print("\n\n\n")
    time.sleep(1)

