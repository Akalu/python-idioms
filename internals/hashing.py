class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'({self.name},{self.age})'


class NamedPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, o):
        if o is None:
            return False
        return self.name == o.name

    def __repr__(self):
        return f'({self.name},{self.age})'


def print_info(person_0, person_1, person_2):
    print(f'hash(person_0) = {hash(person_0)}')
    print(f'hash(person_1) = {hash(person_1)}')
    print(f'hash(person_2) = {hash(person_2)}')
    # NOTE: default implementation of hash and eq functions are memory-based
    print(f'person_1 == person_0 ? {person_1 == person_0}')
    print(f'person_1 == person_2 ? {person_1 == person_2}')
    print(f'person_1 == person_2 ? {person_1.__eq__(person_2)}')

    persons = set()

    persons.add(person_0)
    persons.add(person_1)
    persons.add(person_2)

    print(persons)


def calc_hash():
    val_1 = 10
    val_2 = 10

    # for small numbers and all Strings Python re-use objects
    print(f'id of val_1 = {hash(val_1)}')
    print(f'id of val_2 = {hash(val_2)}')

    str_1 = 'string_token'
    str_2 = 'string_token'

    print(f'id of str_1 = {hash(str_1)}')
    print(f'id of str_2 = {hash(str_2)}')

    person_0 = Person('Alice', 12)
    person_1 = Person('Alice', 12)
    person_2 = Person('Alice', 55)

    print_info(person_0, person_1, person_2)

    person_0 = NamedPerson('Alice', 12)
    person_1 = NamedPerson('Alice', 12)
    person_2 = NamedPerson('Alice', 55)

    print_info(person_0, person_1, person_2)

def data_structures_hashes():
    all = dict()
    tuple1 = ('a','b')
    all[tuple1] = 1
    print(f'tuple1 in all {tuple1 in all}')
    tuple2 = ('a','b')
    print(f'tuple2 in all {tuple2 in all}')


def main():
    calc_hash()
    data_structures_hashes()


if __name__ == '__main__':
    main()
