def my_func():
    mrk = True
    result = 0
    while mrk == True:
        str = input("Введите два числа через пробел. Для выхода введите 'q' -> ")
        my_list = str.split()
        rs = 0
        for i in range(len(my_list)):
            if my_list[i] == "q":
                mrk = False
                break
            else:
                rs = rs + int(my_list[i])
        result = result + rs
        print(result)


my_func()
