import random as rndm

my_list = []
length = rndm.randint(1, 20)

for i in range(length):
    my_list.append(rndm.randint(1, 100))

result = [n[0] for n in list(zip(my_list[1:], my_list)) if n[0] > n[1]]


print(my_list)
print(result)
