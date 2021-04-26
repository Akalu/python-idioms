import threading
from queue import Queue

SENTINEL = object()


def producer(q, n):
    a, b = 0, 1
    while a <= n:
        q.put(a)
        print(f'produced {a}')
        a, b = b, a + b
    q.put(SENTINEL)


def consumer(q):
    while True:
        num = q.get()
        q.task_done()
        if num is SENTINEL:
            break
        print(f'Got number {num}')


def producer_consumer():
    q = Queue()
    cns = threading.Thread(target=consumer, args=(q,))
    prd = threading.Thread(target=producer, args=(q, 35))
    cns.start()
    prd.start()
    q.join()


event = threading.Event()


def fire():
    print('Firing event...')
    event.set()


def listen():
    event.wait()
    print('Event has been caught')


def events():
    t1 = threading.Thread(target=fire)
    t2 = threading.Thread(target=listen)
    t2.start() # first start listening thread otherwise there is a risk to loose events
    t1.start()


def main():
    producer_consumer()
    events()


if __name__ == '__main__':
    main()
