class Digit:
    def __init__(self, value):
        self._value = value

    def __setattr__(self, name, value):
        if not self._check_value(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(name, value)

    def _check_value(self, value):
        return type(value) in (int, float)


class Integer(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is int


class Float(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is float


class Positive(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value > 0


class Negative(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value < 0


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = [*filter(lambda x: isinstance(x, Positive), digits)]
lst_float = [*filter(lambda x: isinstance(x, Float), digits)]