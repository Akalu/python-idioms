import string


def strings_manipulation():
    str1 = 'part1'
    #          \3=='t - excluded
    str2 = 'part2'
    #          \3=='t - included
    str_res = str1[:3] + '|' + str2[3:]
    print(str_res)

    # one-line reverse
    str_rev = str_res[::-1]
    print(str_rev)


def collecting_statistics():
    str = 'Abcda'

    s = str.lower()
    map = dict()

    # collect statistics about letters
    for let in s:
        if let not in map:
            map[let] = 1
        else:
            map[let] += 1

    for pair in map.items():
        print(f'key={pair[0]} value={pair[1]}')


def collecting_full_statistics():
    str = 'Abcda'

    s = str.lower()
    map = dict()

    for char in string.ascii_lowercase:
        map[char] = 0

    # collect statistics about letters
    for let in s:
        map[let] += 1

    for pair in map.items():
        print(f'key={pair[0]} value={pair[1]}')


def alphabet_manipulation():
    alphabet_std = string.ascii_lowercase
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    rev_alphabet = alphabet[::-1]
    alphabetIterator = map(chr, range(ord('a'), ord('z') + 1))

    print(alphabet_std)
    print(alphabet)
    print(rev_alphabet)
    print(list(alphabetIterator))


class Person():
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
        return (self.name, self.age) < (other.name, other.age)

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
    collecting_statistics()
    collecting_full_statistics()
    alphabet_manipulation()
    strings_manipulation()
    complex_sorting()


if __name__ == '__main__':
    main()
