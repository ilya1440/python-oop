TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        name = args[0]
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
            setattr(obj, 'name', name)
            return obj
        else:
            obj = super().__new__(DialogLinux)
            setattr(obj, 'name', name)
            return obj


def main():
    print('Session started')


if __name__ == '__main__':
    main()