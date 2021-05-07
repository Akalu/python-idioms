import heapq


def min_heap():
    arr = [3, 5, 1, 2, 6, 8, 7]
    heapq.heapify(arr)  # O(n)

    print(f'array before heappop {arr}')
    smallest = heapq.heappop(arr)
    print(smallest)
    print(f'array after heappop {arr}')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f'({self.name},{self.age})'


def max_heap():
    p1 = Person('Alice', 23)
    p2 = Person('Bob', 34)
    p3 = Person('Eva', 12)
    arr = [p1, p2, p3]

    heapq.heapify(arr)  # O(n)
    print(f'array before heappop {arr}')
    biggest = heapq.heappop(arr)
    print(biggest)
    print(f'array after heappop {arr}')


def main():
    min_heap()
    max_heap()


if __name__ == '__main__':
    main()
