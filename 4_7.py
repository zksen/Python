def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        yield result


k = int(input())
my_list = [el for el in fact(k)]
print(my_list)

