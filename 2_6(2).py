my_list = []
length = int(input("Введите количество товара -> "))
for i in range(length):
    my_list.append((i + 1, {"название": input("Введите название товара -> "),
                            "цена": int(input(f"Введите стоимость товара -> ")),
                            "количество": int(input(f"Введите количество товара -> ")),
                            "ед": input(f"Введите в чем измеряется количество товара -> ")}))
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
my_dict = {"название": lis_name, "цена": lis_price, "количество": lis_number, "ед": list(set(lis_un_it))}
print(my_dict)
