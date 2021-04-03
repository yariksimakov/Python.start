class ComplexNumber:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return ComplexNumber(self.param + other.param)

    def __mul__(self, other):
        return ComplexNumber(self.param * other.param)

    def __str__(self):
        return f"{self.param}"


one = ComplexNumber(4 + 2j)
two = ComplexNumber(-7 - 5j)
print(one + two + two)
print(type(one + two))
print()
print(one * two * one)
print(type(one * two))