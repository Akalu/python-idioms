class A:
    label = 'a'


class B(A):
    label = 'b' # overrides a


class C(A):
    label = 'c' # overrides a


class D(B, C):
    pass


def main():
    d = D()
    print(d.label) # could be either 'b' or 'c'
    print(d.__class__.mro())  # notice another way to get the MRO - look up until target met


if __name__ == '__main__':
    main()
