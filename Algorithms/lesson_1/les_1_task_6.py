"""По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
 составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
  равнобедренным или равносторонним."""
a = float(input("Введите длину первого отрезка: "))
b = float(input("Введите длину второго отрезка: "))
c = float(input("Введите длину третьего отрезка: "))
if a < b + c and b < a + c and c < a + b:
    if a == c or c == b or a == b:
        if a == c and c == b:
            print("Треугольник существует и он равносторонний")
        else:
            print("Треугольник существует и он равнобедренный")
    else:
        print("Треугольник существует и он разносторонний")
else:
    print("Не существует треугольника с такими сторонами")