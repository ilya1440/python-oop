class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
        else:
            self.head = obj
            self.tail = obj

    def remove_obj(self):
        if self.tail:
            temp_obj = self.tail.get_prev()
            if temp_obj:
                temp_obj.set_next(None)
                self.tail = temp_obj
            else:
                self.tail = None
                self.head = None

    def get_data(self):
        if self.head:
            next_flag = self.head
            result = []
            while next_flag:
                result.append(next_flag.get_data())
                next_flag = next_flag.get_next()
        else:
            result = []
        return result


def main():
    print('Session started')


if __name__ == '__main__':
    main()