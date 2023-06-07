class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackIterator:
    def __init__(self, top):
        self.top = top

    def __next__(self):
        if not self.top:
            raise StopIteration

        result = self.top
        self.top = self.top.next
        return result

    def __iter__(self):
        return self


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None
        self.length = 0

    def get_last(self):
        tmp_object = None
        if self.top and self.top.next:
            tmp_object = self.top
            while tmp_object.next != self.tail:
                tmp_object = tmp_object.next
        elif self.top:
            return self.top
        return tmp_object

    def push_back(self, obj):
        if self.tail:
            self.tail.next = obj
            self.tail = obj
        else:
            self.top = obj
            self.tail = obj
        self.length += 1

    def push_front(self, obj):
        if self.top:
            tmp_object = self.top
            self.top = obj
            self.top.next = tmp_object
        else:
            self.top = self.tail = obj
        self.length += 1

    def pop(self):
        pop_object = None
        tmp_obj = self.get_last()
        if tmp_obj == self.top:
            pop_object = self.top
            self.top = None
            self.tail = None
            self.length -= 1
        elif tmp_obj:
            pop_object = self.tail
            self.tail = tmp_obj
            tmp_obj.next = None
            self.length -= 1
        return pop_object

    def check(self, index):
        if not isinstance(index, int) or index < 0 or index > self.length - 1:
            raise IndexError('неверный индекс')

    def get_item_by_index(self, index):
        count = 0
        tmp_object = self.top
        while count != index:
            tmp_object = tmp_object.next
            count += 1
        return tmp_object

    def __getitem__(self, item):
        self.check(item)
        result = self.get_item_by_index(item)
        return result.data

    def __setitem__(self, key, value):
        self.check(key)
        value = StackObj(value)
        tmp_object = self.top
        if key == 0:
            if self.tail == self.top:
                self.tail = self.top = value
            else:
                tmp_object = self.top.next
                self.top = value
                self.top.next = tmp_object

        else:
            count = 0
            while count != key - 1:
                tmp_object = tmp_object.next
                count += 1
            if tmp_object.next == self.tail:
                self.tail = value
            pop_object = tmp_object.next.next
            value.next = pop_object
            tmp_object.next = value

    def __len__(self):
        return self.length

    def __iter__(self):
        return StackIterator(self.top)



st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"