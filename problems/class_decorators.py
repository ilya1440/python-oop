# class decorator without arguments
class HandlerGET:
    def __init__(self, function):
        self.function = function

    # dependent function args and kwargs are transferred here
    def __call__(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.get('method', 'GET') == 'GET':
            result_value = self.function(request)
            return f"GET: {result_value}"

        return None


# class decorator with arguments
class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            return self.process(func, request, *args, **kwargs)

        return wrapper

    def process(self, function, request, *args, **kwargs):
        method = request.get('method', 'GET')
        if method in self.methods:
            result_value = function(request)
            return f"{method}: {result_value}"

        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)


def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if type(arg) != int:
                raise TypeError("аргументы должны быть целыми числами")
        for kwarg in kwargs.values():
            if type(kwarg) != int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(self, *args, *kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]