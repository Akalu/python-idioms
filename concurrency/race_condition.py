import threading
from random import random
from time import sleep

counter = 0  # a global variable accessible from different threads
incr_lock = threading.Lock()

random_delay = lambda : sleep(0.1 * random())


def inc(n, name):
    global counter
    for count in range(n):
        current = counter
        random_delay()
        counter = current + 1
        random_delay()


def inc_thread_safe(n, name):
    global counter
    for count in range(n):
        with incr_lock:
            current = counter
            random_delay()
            counter = current + 1
            random_delay()


def race():
    global counter
    counter = 0
    n = 10
    t1 = threading.Thread(target=inc, args=(n, 'th1'))  # create a new thread using incr() function as a base
    t2 = threading.Thread(target=inc, args=(n, 'th2'))
    print('starting {t1}')
    t1.start()
    print('starting {t2}')
    t2.start()
    t1.join()
    t2.join()
    print(f'race counter: {counter}')


def no_race():
    global counter
    counter = 0
    n = 10
    t1 = threading.Thread(target=inc_thread_safe,
                          args=(n, 'th1'))  # create a new thread using incr() function as a base
    t2 = threading.Thread(target=inc_thread_safe, args=(n, 'th2'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'no_race counter: {counter}')


def main():
    race()
    no_race()


if __name__ == '__main__':
    main()
