def str_to_list(str):
    length = len(str)
    my_list = []
    for i in range(length):
        my_list.append(str[i])
    return my_list


def clever_str(str):
    length = len(str)
    my_list = str_to_list(str)
    for i in range(length):
        if (ord(my_list[i]) <= 96 or ord(my_list[i]) >= 123) and ord(my_list[i]) != 32:
            return False
        else:
            continue
    return True


def upp_reg(str):
    length = len(str)
    for i in range(1, length - 1):
        if ord(str[i-1]) == 32 and ord(str[i]) != 32 and (ord(str[i]) <= 64 or ord(str[i]) >= 91):
            str = str[:i] + chr(ord(str[i]) - 32) + str[(i+1):]
        else:
            continue
    if str[0] != 32:
        str = chr(ord(str[0]) - 32) + str[1:]
    else:
        str = str
    return str


def my_func():
    mrk = False
    while mrk == False:
        str = input("Введите строку строчными латинскими буквами, содержащую пробелы (для выхода нажмите Q) -> ")
        if clever_str(str) == True:
            print(upp_reg(str))
        elif str == "Q":
            mrk = True
        else:
            continue


my_func()


