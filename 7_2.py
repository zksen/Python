from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, s, g):
        self.size = s
        self.growth = g

    @property
    @abstractmethod
    def consuptions(self):
        pass


class Coat(Clothes):
    @property
    def consuptions(self):
        return f"Подсчет количества ткани на пальто {(self.size / 6.5 + 0.5):.1f}"


class Suit(Clothes):
    @property
    def consuptions(self):
        return f"Подсчет количества ткани на костюм {(self.growth * 2 + 0.3):.1f}"


my_coat = Coat(48, 180)
my_suit = Suit(50, 190)
print(my_coat.consuptions + "\n" + my_suit.consuptions + "\n")
