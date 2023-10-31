class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        # your arbitrarily complex comparison here:
        if self.name == other.name:
            return self.age < other.age
        else:
            return self.name < other.name

        # or, as simple as:
        # return (self.name, self.age) < (other.name, other.age)

    def __repr__(self):
        return f'({self.name}, {self.age})'


def complex_sorting():
    person_1 = ('Alice', 19)
    person_2 = ('Ann', 13)
    person_3 = ('Bob', 21)
    person_4 = ('Ann', 15)

    lst = [person_4, person_3, person_1, person_2]

    print(lst)

    sorted_by_one_param = lst[:]
    sorted_by_one_param.sort(key=lambda n: n[0], reverse=False)
    print('sorting by 1st elem of object (i.e. byName')
    print(sorted_by_one_param)

    print('sorting by 2 elems of object (i.e. firstly byName, then byAge) - variant # 1')

    sorted_by_two_params = lst[:]
    sorted_by_two_params.sort(key=lambda t: (t[0], t[1]), reverse=False)
    print(sorted_by_two_params)

    print('sorting by 2 elems of object (byName, byAge) - variant # 2 - using a Compare Function __lt__')

    sorted_by_two_params = [Person('Alice', 19), Person('Ann', 13), Person('Bob', 21), Person('Ann', 15)]
    sorted_by_two_params.sort(reverse=False)
    print(sorted_by_two_params)


def main():
    complex_sorting()


if __name__ == '__main__':
    main()
