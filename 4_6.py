import itertools

for i in itertools.count(3):
    print(i)
    if i == 10:
        break

my_str = ""
for i in itertools.cycle("GeekBrains"):
    my_str += i
    if len(my_str) > 1001:
        break

print(my_str)
