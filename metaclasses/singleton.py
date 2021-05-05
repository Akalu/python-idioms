class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f'first call, ever: creating an instance of Singleton')
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


def main():
    x = SingletonClass()
    y = SingletonClass()
    print(x == y)
    print(f'id(x)={id(x)}')
    print(f'id(x)={id(y)}')
    print(type(x))

    x = RegularClass()
    y = RegularClass()
    print(x == y)
    print(f'id(x)={id(x)}')
    print(f'id(x)={id(y)}')
    print(type(x))


if __name__ == '__main__':
    main()
