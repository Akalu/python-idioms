from time import time


def performance_test_1():
    mx = 5000

    t = time()  # start time for the for loop
    floop = []
    for a in range(1, mx):
        for b in range(a, mx):
            floop.append(divmod(a, b))
    print('for loop: {:.4f} s'.format(time() - t))  # elapsed time

    t = time()  # start time for the list comprehension

    compr = [
        divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
    print('list comprehension: {:.4f} s'.format(time() - t))

    t = time()  # start time for the generator expression
    gener = list(
        divmod(a, b) for a in range(1, mx) for b in range(a, mx))
    print('generator expression: {:.4f} s'.format(time() - t))


def performance_test_2():
    mx = 2 * 10 ** 7

    t = time()
    absloop = []
    for n in range(mx):
        absloop.append(abs(n))
    print('for loop: {:.4f} s'.format(time() - t))

    t = time()
    abslist = [abs(n) for n in range(mx)]
    print('list comprehension: {:.4f} s'.format(time() - t))

    t = time()
    absmap = list(map(abs, range(mx)))
    print('map: {:.4f} s'.format(time() - t))


def main():
    performance_test_1()
    performance_test_2()


if __name__ == '__main__':
    main()
