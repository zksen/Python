len_list = int(input("Введите количество элементов списка -> "))
my_list = []
for i in range(len_list):
    my_list.append(input("Введите элемент -> "))
print(my_list)
my_list1 = []
my_list2 = []
marker = my_list[0]
for i in range(len_list):
    my_list1 = my_list[::2]
    my_list2 = my_list[1::2]
my_list3 = []
for i in range(int(len(my_list) / 2)):
    my_list3.append(my_list2[i])
    my_list3.append(my_list1[i])
if len_list % 2 == 1:
    my_list3.append(my_list[len_list-1])
print(my_list3)
# print(my_list1)
# print(my_list2)
