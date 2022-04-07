class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def mass(self):
        print(
            f"{self._width} м*{self._length} м*25 кг*5 см = {int(round(self._width * self._length * 25 * 5 * (10 ** (-3))))} т.")


my_road = Road(5000, 20)
my_road.mass()
