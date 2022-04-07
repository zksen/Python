class Worker:
    def __init__(self, n, s, p, w, b):
        self._income = {"wage": w, "bonus": b}
        self.name = n
        self.surname = s
        self.position = p


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


my_pos = Position("Ваня", "Васечкин", "менеджер", 200000, 200000)
print(f"Полное имя сотрудника: {my_pos.get_full_name()}. Оклад этого сотрудника: {my_pos.get_total_income()}")
