def div_ision(n_1, n_2):
    try:
        print(n_1 / n_2)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


div_ision(int(input("Введите первое число -> ")), int(input("Введите второе число -> ")))
