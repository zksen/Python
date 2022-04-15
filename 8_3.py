class CheckList(Exception):
    """CheckList"""
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        value = input("Enter str, for Exit press Ctrl + F2\n")
        if not value.isdigit():
            raise CheckList("Entered not a num")
        my_list.append(int(value))
    except CheckList as err:
        print(f"{err}\n{my_list}")
    except KeyboardInterrupt:
        print(f"Exit\tYour List: {my_list}")
        break
    else:
        print(my_list)
