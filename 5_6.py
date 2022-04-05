def format_str(s):
    s_1 = ""
    for el in range(len(s)):
        if s[el].isdigit() or el == " ":
            s_1 += s[el]
        else:
            continue
    return s_1


def sum_of_str(l):
    l_2 = []
    for i in range(len(l)):
        l_2.append(int(l[i]))
    return sum(l_2)


with open("text_6.txt", "r", encoding="utf-8") as my_file:
    my_dict = {
        el.split()[0]: sum_of_str(
            (format_str(el.split()[1]) + " " + format_str(el.split()[2]) + " " + format_str(el.split()[3])).split()) for
        el in
        my_file.read().split("\n")}
    my_file.close()

print(my_dict)
