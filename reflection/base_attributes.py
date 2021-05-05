class TestClass:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def print(self):
        print('Hello, world!')


def sprint(obj):
    result = []
    for i in [v for v in dir(obj) if not callable(getattr(obj, v)) and v[0] != '_']:
        result.append(str(i) + ' ' + str(getattr(obj, i, '')))
    return result


def info(obj):
    print(f'created an instance of obj: {obj}')
    print(f' __class__: {obj.__class__}')
    print(f' __doc__: {obj.__doc__}')
    print(f' found attributes: {dir(obj)}')
    print(sprint(obj))


def main():
    obj = object()
    info(obj)

    obj = TestClass('Alice')
    info(obj)


if __name__ == '__main__':
    main()
