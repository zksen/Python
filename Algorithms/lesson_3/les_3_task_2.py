"""2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа."""
import random
size = 6
my_list = [random.randint(1, 100) for _ in range(size)]
my_list2 = [i for i in range(len(my_list)) if my_list[i] % 2 == 0]
print(my_list)
print(my_list2)