import copy


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


c = DatabaseConnection()

try:
    c.connect('aaa', 'bbb')
except ConnectionError:
    assert c._fl_connection_open
else:
    assert False, "не сгенерировалось исключение ConnectionError"

try:
    with DatabaseConnection() as conn:
        conn.connect('aaa', 'bbb')
except ConnectionError:
    assert True
else:
    assert False, "не сгенерировалось исключение ConnectionError"

assert conn._fl_connection_open == False, "атрибут _fl_connection_open принимает значение True, а должно быть False"


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._current_weight = 0
        self._things = []

    def add_thing(self, thing):
        if thing[1] + self._current_weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        else:
            self._current_weight += thing[1]
            self._things.append(thing)


class BoxDefender:
    def __init__(self, box):
        self.box = box
        self.tmp_box = Box(None, None)
        self.tmp_box.__dict__ = copy.deepcopy(box.__dict__)

    def __enter__(self):
        return self.tmp_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.box.__dict__ = self.tmp_box.__dict__
        return False

