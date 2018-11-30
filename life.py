
import random

x_lenght = 25
y_lenght = 10
napovnenist = 0.7


def inst_point():
    num = random.random()
    if num >= napovnenist:
        return "O"
    else:
        return "_"


def gen_fields():
    fields = [
        [
            inst_point()
            for i in range(x_lenght)
        ]
        for j in range(y_lenght)
    ]
    return fields


def print_fields(fields):
    for row in fields:
        print(*row)


def change(fiels):
    for index_x in range(len(fiels)):
        for index_y in range(len(fiels[index_x])):
            it_is_a_live(index_x, index_y)


if __name__ == "__main__":
    f = gen_fields()
    print_fields(f)
    change(f)
