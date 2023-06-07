import operator as op


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __do(self, other, f_name, new_object=True):
        if isinstance(other, self.__class__) and len(other) == len(self):
            new_coords = (f_name(a, b) for a, b in zip(self.coords, other.coords))
        elif isinstance(other, (int, float)):
            new_coords = (f_name(b, other) for b in self.coords)
        else:
            raise ArithmeticError('размерности векторов не совпадают')
        if new_object:
            return self.__class__(*new_coords, )
        else:
            self.coords = (*new_coords,)
            return self

    def __add__(self, other):
        return self.__do(other, op.add)

    def __sub__(self, other):
        return self.__do(other, op.sub)

    def __mul__(self, other):
        return self.__do(other, op.mul)

    def __iadd__(self, other):
        return self.__do(other, op.add, False)

    def __isub__(self, other):
        return self.__do(other, op.sub, False)

    def __imul__(self, other):
        return self.__do(other, op.mul, False)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coords == other.coords
        raise TypeError('Сравнение векторов не возможно!')
