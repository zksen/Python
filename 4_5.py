from functools import reduce

my_list = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(lambda x_1, x_2: x_1 * x_2, my_list))