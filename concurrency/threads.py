import threading
from random import random
from time import sleep


def sum_and_product(a, b):
    s, p = a + b, a * b
    print(f'{a}+{b}={s}, {a}*{b}={p}\n')


def status(t):
    status = 'alive' if t.is_alive() else 'terminated'
    print(f'Thread {t.name} has {status}')


def print_current():
    print(f'The current thread is {threading.current_thread()}.')
    print(f'Threads: {list(threading.enumerate())}')


def run(n):
    t = threading.current_thread()
    for count in range(n):
        print(f'Hello from {t.name}! ({count})')
        sleep(0.2 * random())


def one_thread():
    print_current()
    t = threading.Thread(
        target=sum_and_product, name='SumProd', args=(3, 7)
    )
    t.start()
    status(t)  # more likely to see terminated status than alive
    t.join()
    status(t)


def two_threads():
    # spawns 2 concurrently running threads, which are printing numbers from 0 till n
    one = threading.Thread(target=run, name='the first thread', args=(4,))
    two = threading.Thread(target=run, name='the second thread', args=(3,))
    one.start()
    two.start()
    one.join()  # main thread stop execution here until one finishes
    two.join()  # main thread stop execution here until two finishes (if still running)


def main():
    one_thread()
    two_threads()


if __name__ == '__main__':
    main()
