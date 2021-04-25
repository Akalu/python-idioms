from math import sqrt


def zipping():
    # NOTE: ideally must be of equal size, but if not the result will be min(n, m)
    avgs = [22, 21, 29, 24]
    grades = [18, 23, 30]
    zip_list = list(zip(avgs, grades))

    print(zip_list)


# decorate-sort-undecorate idiom (AKA Schwartzian transform)
def mapping():
    students = [
        dict(id=0, credits=dict(math=9, physics=6, history=7)),
        dict(id=1, credits=dict(math=6, physics=7, latin=10)),
        dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
        dict(id=3, credits=dict(math=5, physics=5, geography=7)),
    ]

    def decorate(student):
        # create a 2-tuple (sum of credits, student) from student dict
        return sum(student['credits'].values()), student

    def undecorate(decorated_student):
        # discard sum of credits, return original student dict
        return decorated_student[1]

    students = sorted(map(decorate, students), reverse=True)
    print(students)

    students = list(map(undecorate, students))
    print(students)


def filtering():
    arr = [2, 5, 8, 0, 0, 1, 0]

    filtered_list_1 = list(filter(None, arr))  # 0 == False, so Identity filter returns False for zero elements
    print(filtered_list_1)

    filtered_list_2 = list(filter(lambda x: x, arr))  # equivalent to previous one
    print(filtered_list_2)

    filtered_list_3 = list(filter(lambda x: x >= 5, arr))  # keep only items >= 5
    print(filtered_list_3)


def comprehensions():
    # using map and filter
    sq1 = list(
        map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
    )
    # equivalent, but using list comprehensions
    sq2 = [n ** 2 for n in range(10) if not n % 2]

    print(sq1)
    print(f'sq1 == sq2 {sq1 == sq2}')

    # map comprehensions
    word = 'Hello, World'
    swaps = {c: c.swapcase() for c in word}
    print(swaps)


def comprehensions_with_filter():
    mx = 10
    # chained comprehensions
    triples = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]

    # here we combine filter and map in one list comprehension
    triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
    print(triples)


def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q ** k
        if result <= 100000:
            yield result
        else:
            return
        k += 1


def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


def generators():
    squares = get_squares_gen(4)  # this creates a generator object
    print(squares)
    print(next(squares))  # prints: 0 - the 1st value
    print(next(squares))
    print(next(squares))
    print(next(squares))  # prints: 9
    # the following raises StopIteration, the generator is exhausted,
    # any further call to next will keep raising StopIteration
    try:
        print(next(squares))
    except StopIteration:
        print('no more values')

    for n in geometric_progression(2, 5):
        print(n)

    geometric_seq = [n for n in geometric_progression(2, 5)]
    print(geometric_seq)


def main():
    mapping()
    zipping()
    filtering()
    comprehensions()
    comprehensions_with_filter()
    generators()


if __name__ == '__main__':
    main()
