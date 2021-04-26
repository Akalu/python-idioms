import threading
from random import randint

local = threading.local()


def run(local, barrier):
    local.my_value = randint(0, 100) # any number in [0, 100] - to be tied with this thread instance forever
    t = threading.current_thread()
    print(f'Thread {t.name} has value {local.my_value}')
    barrier.wait()
    print(f'Thread {t.name} still has value {local.my_value}')


def local_vars():
    count = 3
    barrier = threading.Barrier(count)
    threads = [
        threading.Thread(
            target=run, name=f'T{name}', args=(local, barrier) # creates 3 threads with barrier logic
        ) for name in range(count)
    ]
    for t in threads:
        t.start()


def main():
    local_vars()


if __name__ == '__main__':
    main()
