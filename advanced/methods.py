class StringUtil:

    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):  # factory -  cls is a Point
        return cls(*coords)

    @classmethod
    def from_point(cls, point):  # factory - cls is a Point
        return cls(point.x, point.y)


def main():
    print(StringUtil.is_palindrome('Anna', case_insensitive=False))
    print(StringUtil.is_palindrome('Anna', case_insensitive=True))

    p = Point.from_tuple((3, 7))
    print(p.x, p.y)

    q = Point.from_point(p)
    print(q.x, q.y)


if __name__ == '__main__':
    main()
