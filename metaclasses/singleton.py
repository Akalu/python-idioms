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

    print(Singleton.__class__) # top parent type is absent, so the type is 'type'
    print(SingletonClass.__class__)
    print(SingletonClass.__class__.__class__)
    print(RegularClass.__class__)
    print(type.__class__)


if __name__ == '__main__':
    main()
