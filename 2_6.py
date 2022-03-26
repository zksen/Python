na_me = ""
price = 0
number = 0
un_it = ""
my_list = []
length = int(input("Введите количество товара -> "))
for i in range(length):
    na_me = input("Введите название товара -> ")
    price = int(input(f"Введите стоимость товара с именем {na_me} -> "))
    number = int(input(f"Введите количество товара с именем {na_me} -> "))
    un_it = input(f"Введите в чем измеряется количество товара с именем {na_me} -> ")
    my_list.append((i + 1, {"название": na_me, "цена": price, "количество": number, "ед": un_it}))
print(my_list)
lis_name = []
lis_price = []
lis_number = []
lis_un_it = []
for i in range(length):
    lis_name.append(my_list[i][1].get('название'))
    lis_price.append(my_list[i][1].get("цена"))
    lis_number.append(my_list[i][1].get("количество"))
    lis_un_it.append(my_list[i][1].get("ед"))
my_dict = {"название": lis_name, "цена": lis_price, "количество": lis_number, "ед": lis_un_it}
print(my_dict)
