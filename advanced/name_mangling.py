class Base:
    def __init__(self, field):
        self.__field = field

    def op1(self):
        print(f'Base class has __field = {self.__field}...')


class Child(Base):

    def op2(self, field):
        self.__field = field  # is not shadowed because the FQN is _Child__field
        print(f'Child class has __field =  {self.__field}...')


def main():
    obj = Base(100)
    obj.op1()

    obj = Child(200)
    obj.op2(34)
    obj.op1()
    print(obj.__dict__)  # prints all fields with their respective FQNs


if __name__ == '__main__':
    main()
