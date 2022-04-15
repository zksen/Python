class Date:
    """Date"""
    def __init__(self, date):
        self.date = date

    @classmethod
    def str_to_int(cls, obj):
        """Str to list"""
        data_list = [int(el) for el in obj.date.split("-")]
        for el in range(len(data_list)):
            print(data_list[el], end=" ")
        print(cls.valid(obj.date))

    @staticmethod
    def valid(date):
        """Valid date"""
        date_list = [int(el) for el in date.split("-")]
        str_1 = "Incorrect date"
        str_2 = "Correct date"
        if 1 <= date_list[1] <= 12 and 1 <= date_list[0] <= 31 and 1 <= date_list[2] <= 9999:
            return str_2
        else:
            return str_1


my_data = Date("01-12-1999")
my_data.str_to_int(my_data)
