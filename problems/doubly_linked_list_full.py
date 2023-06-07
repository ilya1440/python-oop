class Element:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    next = Element()
    prev = Element()
    data = Element()

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __call__(self, indx):
        result = self.get_element_by_id(indx=indx, remove=False)
        if result:
            return result.data

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_obj(self, obj):
        if self.tail:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        else:
            self.tail = self.head = obj

        self.length += 1

    def remove_obj(self, indx):
        result = self.get_element_by_id(indx)
        if result:
            if indx == self.length - 1:
                result.prev.next = result.next
                self.tail = result.prev
            elif indx == 0:
                result.next.prev = result.prev
                self.head = result.next
            else:
                result.prev.next = result.next
                result.next.prev = result.prev

            self.length -= 1

    def get_element_by_id(self, indx, remove=True):
        result = None
        finder = 0
        if indx + 1 > self.length:
            pass
        else:
            if remove and self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                result = self.head
                while finder != indx:
                    result = result.next
                    finder += 1
        return result


linked_lst = LinkedList()
testobj = ObjList("Sergey")
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
