"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
 в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)"""
number = int(input('Введите число '))
chet = 0
n_chet = 0
while number > 0:
    if number % 10 % 2 == 0:
        chet += 1
        number //= 10
    else:
        n_chet += 1
        number //= 10

print(chet, n_chet)