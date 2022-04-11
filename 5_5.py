with open("text_5.txt", "w+", encoding="utf-8") as my_file:
    my_file.writelines("1 2 3 4 5 6")
    print(my_file.tell())
    my_file.seek(0)
    print(sum([int(el) for el in my_file.read().split()]))

