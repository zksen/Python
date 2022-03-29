def my_func(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    my_list = sorted(my_list)
    my_list.pop(0)
    return sum(my_list)


print(my_func(int(input()), int(input()), int(input())))
