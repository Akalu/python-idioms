def f(obj):
    print('size attribute =', obj.size)

# __new__(): It’s a method which is called before __init__().
# It creates the object and return it. One can override this method to control how the objects are created.

# __init__(): This method just initialize the created object passed as parameter
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.size = 100
        return x


class ClassE(metaclass=Meta):
    pass


def main():
    ClassA = type('ClassA', (), {})
    class_a = ClassA()
    print(class_a)
    print('=================')

    ClassB = type('ClassB', (ClassA,), dict(size=100))

    class_b = ClassB()
    print(class_b)
    print(class_b.size)
    print('=================')

    ClassC = type('ClassC',
                  (),
                  {
                      'size': 100,
                      'get_size': lambda x: x.size
                  }
                  )

    class_c = ClassC()
    print(class_c)
    print(class_c.size)
    print(class_c.get_size())
    print('=================')

    ClassD = type('ClassD',
                  (),
                  {
                      'size': 100,
                      'get_size': f  # could be used to bind some external functionality to the newly constructed type
                  }
                  )

    class_d = ClassD()
    print(class_d)
    print(class_d.size)
    class_d.get_size()
    print('=================')

    class_e = ClassE()
    print(class_e)
    print(class_e.size)


if __name__ == '__main__':
    main()
