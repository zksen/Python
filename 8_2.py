class DivNull(Exception):
    """DivNull"""
    def __init__(self, txt):
        self.txt = txt


try:
    n_1 = int(input("First num: "))
    n_2 = int(input("Second num: "))
    if n_2 == 0:
        raise DivNull("Can't divide by zero!")
except ValueError:
    print("Entered not a num")
except DivNull as err:
    print(err)
else:
    print(f"{(n_1 / n_2):.2f}")
