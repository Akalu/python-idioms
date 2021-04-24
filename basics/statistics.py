import string


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
    alphabet_iterator = map(chr, range(ord('a'), ord('z') + 1))

    print(alphabet_std)
    print(alphabet)
    print(rev_alphabet)
    print(list(alphabet_iterator))


def main():
    collecting_statistics()
    collecting_full_statistics()
    alphabet_manipulation()


if __name__ == '__main__':
    main()
