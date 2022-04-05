my_f_1 = open("text_4.txt", "r", encoding="utf-8")
my_f_2 = open("text_4_1.txt", "w", encoding="utf-8")
my_list = [[el.split()[2], el.split()[1]] for el in my_f_1.read().split("\n")]
for el in range(len(my_list)):
    if my_list[el][0] == "1":
        my_list[el].append("Один")
    elif my_list[el][0] == "2":
        my_list[el].append("Два")
    elif my_list[el][0] == "3":
        my_list[el].append("Три")
    elif my_list[el][0] == "4":
        my_list[el].append("Четыре")
    elif my_list[el][0] == "5":
        my_list[el].append("Пять")
    elif my_list[el][0] == "6":
        my_list[el].append("Шесть")
    elif my_list[el][0] == "7":
        my_list[el].append("Семь")
    elif my_list[el][0] == "8":
        my_list[el].append("Восемь")
    elif my_list[el][0] == "9":
        my_list[el].append("Девять")
    elif my_list[el][0] == "0":
        my_list[el].append("Ноль")
my_list_2 = [el[2] + " " + el[1] + " " + el[0] for el in my_list]
for el in range(len(my_list_2)):
    if el != len(my_list_2) - 1:
        my_f_2.writelines(f"{my_list_2[el]}\n")
    else:
        my_f_2.writelines(f"{my_list_2[el]}")
my_f_1.close()
my_f_2.close()
