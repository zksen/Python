class Stationary:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationary):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"У Вас в руках: {self.title}.")


class Pencil(Stationary):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"У Вас в руках: {self.title}.")


class Handle(Stationary):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"У Вас в руках: {self.title}.")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
pen.draw()
pencil.draw()
handle.draw()