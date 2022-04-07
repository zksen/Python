import random as rndm


class Car:
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    def go(self):
        print(f"Машина {self.color} {self.name} поехала")

    def stop(self):
        print(f"Машина {self.color} {self.name} остановилась")

    def turn(self):
        mrk = rndm.randint(0, 1)
        if mrk == 0:
            print(f"Машина {self.color} {self.name} повернула направо")
        else:
            print(f"Машина {self.color} {self.name} повернула налево")

    def show_speed(self):
        print(f"Машина {self.color} {self.name} движется со скоростью {self.speed}")

    def correct(self):
        if self.is_police:
            print(f"Машина {self.color} {self.name} полицейская")
        else:
            print(f"Машина {self.color} {self.name} не полицейская")


class TownCar(Car):
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)

    def show_speed(self):
        print(f"Машина {self.color} {self.name} движется со скоростью {self.speed}")
        if self.speed > 60:
            print(f"Машина {self.color} {self.name} превышает скорость")
        else:
            print(f"Машина {self.color} {self.name} движется с нормальной скоростью")


class SportCar(Car):
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)


class WorkCar(Car):
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)

    def show_speed(self):
        print(f"Машина {self.color} {self.name} движется со скоростью {self.speed}")
        if self.speed > 40:
            print(f"Машина {self.color} {self.name} превышает скорость")
        else:
            print(f"Машина {self.color} {self.name} движется с нормальной скоростью")


class PoliceCar(Car):
    def __init__(self, s, c, n, i_p):
        super().__init__(s, c, n, i_p)


my_auto = TownCar(rndm.randint(0, 100), "Желтый", "Шевроле", False)
my_auto.correct()
my_auto.turn()
my_auto.go()
my_auto.show_speed()
