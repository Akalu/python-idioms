from collections import deque, namedtuple
from enum import Enum


def mutable_sequences():
    arr = [1, 2, 1, 3, 13]
    print(arr)
    arr.insert(3, 16)
    print(arr)

    arr.insert(-3, 0)  # the 3rd elem if to consider -1 the last, elements are shifted right
    print(arr)
    arr.insert(-10, 0)  # !!!
    print(arr)
    arr.insert(10, 0)
    print(arr)

    # comprehensions
    arr_long = [range(10)]
    print(arr_long)


def sets():
    set_1 = set()
    set_1.add(1)
    set_1.add(2)
    set_1.add(4)
    print(set_1)

    set_2 = set([1, 2, 3])
    print(set_2)

    print(f'intersection is {set_1.intersection(set_2)}')
    print(f'left difference is {set_1.difference(set_2)}')
    print(f'symmetric_difference is {set_1.symmetric_difference(set_2)}')


def queues():
    queue_1 = deque()
    queue_1.append(1)
    queue_1.append(2)
    queue_1.append(3)
    print(queue_1)
    print(f'first elem {queue_1.popleft()}')
    print(f'last elem {queue_1.pop()}')

    print(queue_1)


def stacks():
    stack_1 = []
    stack_1.append(1)
    stack_1.append(2)
    print(f'stack initial state: {stack_1}')

    stack_1.pop()
    print(stack_1)


def maps():
    map_1 = dict()
    map_1['orange'] = 7
    map_1['watermelon'] = 1

    print(map_1)
    print(f'is orange present ? {"orange" in map_1}')

    del map_1['orange']
    print(f'is orange present ? {"orange" in map_1}')


def named_tuple():
    Geo_coords = namedtuple('Geo_coords', ['lat', 'long'])  # this is how definition must be declared
    coords = Geo_coords(9.5, 8.8)
    print(coords)


def enums():
    class Semaphore(Enum):
        GREEN = 1
        YELLOW = 2
        RED = 4

    state = Semaphore.GREEN

    print(f' is state green ? {state == Semaphore.GREEN}')


def main():
    mutable_sequences()
    sets()
    queues()
    stacks()
    maps()
    named_tuple()
    enums()


if __name__ == '__main__':
    main()
