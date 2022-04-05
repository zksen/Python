with open("text_3.txt", "r", encoding="utf-8") as my_f:
    my_list = [(float(el.split()[1]), el.split()[0]) for el in my_f.read().split("\n")]
    my_list_1 = [el[1] for el in my_list if el[0] < 20000]
    print("Список сотрудников имеющих доход меньше 20000:\n")
    for el in range(len(my_list_1)):
        print(my_list_1[el])
    gl_sum = 0
    for el in range(len(my_list)):
        gl_sum += my_list[el][0]
    print(f"\nСредняя зарплата работников: {gl_sum / len(my_list)}")

my_f.close()
