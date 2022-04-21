"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки."""
x_1 = float(input("Введите x_1: "))
y_1 = float(input("Введите y_1: "))
x_2 = float(input("Введите x_2: "))
y_2 = float(input("Введите y_2: "))
if x_1 == x_2:
    print(f"Уравнение прямой: x = {x_1}")
else:
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_1 - x_1 * k
    print(f"Уравнение прямой: y = {k} * x + {b}")