my_f = open("1.txt", "w", encoding="utf-8")


mrk = True
while mrk:
        el = input("Что вы хотите записать в файл? -> ")
        if el != "":
            my_f.writelines(f"{el}\n")
        else:
            mrk = False

my_f.close()
