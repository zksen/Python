with open("text_4.txt", "r", encoding="utf-8") as my_f:
    my_list = [len(el.split()) for el in my_f.read().split("\n")]
    for el in range(len(my_list)):
        print(f"В строке {el + 1} количество слов:{my_list[el]}")

    print(f"Всего в файле количество строк: {len(my_list)}")
