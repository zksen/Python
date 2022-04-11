import emoji


class Cell:
    def __init__(self, n):
        self.number = n

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(
            self.number - other.number) if self.number > other.number else "\U0001F606" * self.number + " меньше " + "\U0001F606" * other.number

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def __str__(self):
        return "\U0001F606" * self.number

    def make_order(self, i):
        str = ""
        for el in range(self.number):
            if (el + 1) % i == 0:
                str += "\U0001F606\n"
            else:
                str += "\U0001F606"
        return str


my_cell_1 = Cell(7)
my_cell_2 = Cell(4)
print("Сумма: ", my_cell_1 + my_cell_2, "\n")
print("Разность: ", my_cell_1 - my_cell_2, "\n")
print("Разность: ", my_cell_2 - my_cell_1, "\n")
print("Умножение: ", my_cell_1 * my_cell_2, "\n")
print("Деление: ", my_cell_1 / my_cell_2, "\n")
print(my_cell_1.make_order(3))
