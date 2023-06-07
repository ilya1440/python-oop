class ListMath:
    def __init__(self, values=[]):
        self.lst_math = values

    def __setattr__(self, key, values):
        result = [*filter(lambda value: type(value) in (int, float), values)]
        object.__setattr__(self, key, result)

    def operation_logic(self, other, operation, reverse=False):
        result = []
        if operation == 'add':
            result = [value + other for value in self.lst_math]
        if operation == 'sub':
            result = [value - other if not reverse else other - value for value in self.lst_math]
        if operation == 'mul':
            result = [value * other for value in self.lst_math]
        if operation == 'div':
            result = [value / other if not reverse else other / value for value in self.lst_math]
        return result

    # addition methods
    def __add__(self, other):
        result = self.operation_logic(other, 'add')
        return ListMath(result)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        result = self.operation_logic(other, 'add')
        self.lst_math = result
        return self

    # subtraction methods
    def __sub__(self, other):
        result = self.operation_logic(other, 'sub')
        return ListMath(result)

    def __rsub__(self, other):
        result = self.operation_logic(other, 'sub', True)
        return ListMath(result)

    def __isub__(self, other):
        result = self.operation_logic(other, 'sub')
        self.lst_math = result
        return self

    # mul methods
    def __mul__(self, other):
        result = self.operation_logic(other, 'mul')
        return ListMath(result)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        result = self.operation_logic(other, 'mul')
        self.lst_math = result
        return self

    # subtraction methods
    def __truediv__(self, other):
        result = self.operation_logic(other, 'div')
        return ListMath(result)

    def __rtruediv__(self, other):
        result = self.operation_logic(other, 'div', True)
        return ListMath(result)

    def __itruediv__(self, other):
        result = self.operation_logic(other, 'div')
        self.lst_math = result
        return self
