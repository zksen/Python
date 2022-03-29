def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name="Zakhar",
              surname="Ksendikov",
              year="1994",
              city="Saint-Petersburg",
              email="zakharksendikov4@gmail.com",
              telephone="89811219006"))
