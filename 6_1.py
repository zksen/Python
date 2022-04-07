import time as tm


class TrafficLight:
    __color = [("Красный", 7), ("Желтый", 2), ("Зеленый", 10)]

    def running(self):
        while True:
            for i in range(3):
                print("\n" * 100)
                print(self.__color[i][0])
                tm.sleep(self.__color[i][1])


my_traffic_color = TrafficLight()
my_traffic_color.running()
