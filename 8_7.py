class ComplexNumber:
    """Complex Numbers"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


complex_1 = ComplexNumber(1, 2)
complex_2 = ComplexNumber(3, 4)
print(f"({complex_1}) + ({complex_2}) = {complex_1 + complex_2}")
print(f"({complex_1}) * ({complex_2}) = {complex_1 * complex_2}")
