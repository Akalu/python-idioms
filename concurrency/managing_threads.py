import threading
from time import sleep


class Fibonacci(threading.Thread):

    def __init__(self, *a, **kwa):
        super().__init__(*a, **kwa)
        self._running = True

    def stop(self):
        self._running = False

    def run(self):
        a, b = 0, 1
        while self._running:
            print(a, end=' ')
            a, b = b, a + b
            sleep(0.07)
        print()


def stop_thread_gracefully():
    fibo = Fibonacci()
    fibo.start()
    sleep(1) # allow thread to run some time - roughly 10 cycles
    fibo.stop()
    fibo.join()
    print('Complete')


def main():
    stop_thread_gracefully()


if __name__ == '__main__':
    main()