"""7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
 1+2+...+n = n(n+1)/2, где n — любое натуральное число."""
n = int(input('Введите натуральное число: '))
sum_1 = 0
sum_2 = n * (n + 1) / 2
for el in range(1, n+1):
    sum_1 += el
if sum_1 == sum_2:
    print(True)
else:
    print(False)