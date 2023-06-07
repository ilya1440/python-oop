class Product:
    id: int
    name: str
    weight: (int, float)
    price: (int, float)
    count = 0

    def __init__(self, name, weight, price):
        self.id = self.generate_id()
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def generate_id(cls):
        cls.count += 1
        return cls.count

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key, object)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

test = Product(34, 45, 84)