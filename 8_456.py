class CheckCount(Exception):
    """Check count printer"""

    def __init__(self, txt):
        self.txt = txt


class Stock:
    """Stock"""

    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        """Add to dict object by name"""
        try:
            if equipment.group_name() == "Printer" and not equipment.count.isdigit():
                raise CheckCount(
                    f"Number of printers {equipment.name} {equipment.model_pr} is written in text --> {equipment.count}"
                    f". Fix it!")
        except CheckCount as err:
            print(err)
        else:
            self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        """Extract from dict object by name of Class"""
        try:
            if self._dict[name]:
                self._dict.setdefault(name).pop(0)
        except KeyError as err:
            print(f"There is no such equipment with this name {err} in stock")


class OfficeEquipment:
    """Office Equipment"""

    def __init__(self, name, count, year):
        self.name = name
        self.count = count
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        """Name group"""
        return f"{self.group}"

    def __str__(self):
        return f"{self.name} {self.count} {self.year}"


class Printer(OfficeEquipment):
    """Printers"""

    def __init__(self, name, count, year, model_pr):
        super().__init__(name, count, year)
        self.model_pr = model_pr

    def __repr__(self):
        return f"{self.name} {self.count} {self.year} {self.model_pr}"

    def action(self):
        """Action"""
        return f"All printers with name {self.name} Print"


class Scanner(OfficeEquipment):
    """Scaner"""

    def __init__(self, name, count, year, model_sc):
        super().__init__(name, count, year)
        self.model_sc = model_sc

    def __repr__(self):
        return f"{self.name} {self.count} {self.year} {self.model_sc}"

    def action(self):
        """Action"""
        return f"All scanners with name {self.name} Scan"


class Copiers(OfficeEquipment):
    """Copiers"""

    def __init__(self, name, count, year, model_x):
        super().__init__(name, count, year)
        self.model_x = model_x

    def __repr__(self):
        return f"{self.name} {self.count} {self.year} {self.model_x}"

    def action(self):
        """Action"""
        return f"All copiers with name {self.name} Copy"


sklad = Stock()
scaner_1 = Scanner("Fujitsu", "60", 2022, "FI-7700S")
sklad.add_to(scaner_1)
scaner_2 = Scanner("Brother", "30", 2021, "ADS-3000N")
sklad.add_to(scaner_2)
scaner_3 = Scanner("Epson", "40", 2020, "Perfection V850 Pro")
sklad.add_to(scaner_3)
printer_1 = Printer("HP", "50", 2005, "ENVY 110")
sklad.add_to(printer_1)
printer_2 = Printer("EPSON", "twenty", 2008, "L805")
sklad.add_to(printer_2)
copy_1 = Copiers("Xerox", "30", 2019, "3050")
print(sklad._dict)
sklad.extract(scaner_1.group_name())
print(sklad._dict)
sklad.extract("Xerox")
