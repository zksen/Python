def int_func (str):
    ans = "Я не умею работать с такими строками"
    if str.find(" ") == -1:
        return str.capitalize()
    else:
        return ans

my_str = input("Введите пожалуйста строку -> ")
my_list = my_str.split()
n = len(my_list)
for i in range(n):
    my_list.append(int_func(my_list[i]))

print(" ".join(my_list[n:]))
