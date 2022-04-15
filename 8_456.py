class Stock:
    """Stock"""

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.my_dict = {"Name": self.name, "Price": self.price, "Count": self.count}


class Printer(Stock):
    """Printers"""

    def __init__(self, name, price, count, type_print, model_print):
        super().__init__(name, price, count)
        self.type_print = type_print
        self.model_print = model_print


class Scaner(Stock):
    """Scaner"""

    def __init__(self, name, price, count, type_scan, model_scan):
        super().__init__(name, price, count)
        self.type_scan = type_scan
        self.model_scan = model_scan


class Xerox(Stock):
    """Xerox"""

    def __init__(self, name, price, count, type_xerox, model_xerox):
        super().__init__(name, price, count)
        self.type_xerox = type_xerox
        self.model_xerox = model_xerox



