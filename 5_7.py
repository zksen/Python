import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    i = 0
    my_list_prof = []
    av = 0
    el = 0
    while True:
        mrk = my_file.readline()
        if mrk != "":
            prof = int(mrk.split()[2]) - int(mrk.split()[3])
            my_list_prof.append(prof)
            if prof > 0:
                el += 1
                av += prof
            else:
                continue
        else:
            break
    my_file.seek(0)
    my_list = [{el.split()[0]: int(el.split()[2]) - int(el.split()[3]) for el in my_file.read().split("\n")},
               {"average_profit": av / el}]
    my_file.close()
with open("text_77.json", "a", encoding="utf-8") as my_file_2:
    my_file_2.write("\n")
    json.dump(my_list, my_file_2, indent=4, ensure_ascii=False)
    my_file.close()