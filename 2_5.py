my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг - {my_list}")
n = int(input("Введите число -> "))
while True:
    for i in range(len(my_list)):
        if my_list[i] == n:
            mrk = my_list.count(n)
            my_list.insert(i + mrk, n)
            break
        elif my_list[0] < n:
            my_list.insert(0, n)
        elif my_list[-1] > n:
            my_list.append(n)
        elif my_list[i] > n and my_list[i + 1] < n:
            my_list.insert(i + 1, n)
            break
    print(f"Текущий рейтинг - {my_list}")
    n = int(input("Введите число -> "))
