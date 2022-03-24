my_str = input("Введите строку -> ")
my_list = my_str.split()
for i in range(len(my_list)):
    print(f"{i + 1}. {my_list[i][:10]}")
