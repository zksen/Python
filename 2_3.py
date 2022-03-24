n = int(input("Введите число от 1 до 12 -> "))
my_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
list_values = list(my_dict.values())
list_keys = list(my_dict.keys())
len_list_values = len(list_values)
result = ""
for i in range(len_list_values):
    if list_values[i].count(n) == 1:
        result = list_keys[i]
print(f"Месяц под номером {n} относится к времени года {result}")
