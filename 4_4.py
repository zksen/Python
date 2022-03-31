import random as rndm

my_list = []
length = rndm.randint(1, 20)

for i in range(length):
    my_list.append(rndm.randint(1, 100))

result = [n for n in my_list if my_list.count(n) == 1]
print(my_list)
print(result)