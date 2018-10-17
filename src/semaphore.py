from threading import Semaphore
from threading import Thread


def count_even(s_even, s_odd):
    for i in range(0, 101, 2):
        s_even.acquire()
        print(i)
        s_odd.release()


def count_odd(s_even, s_odd):
    for i in range(1, 101, 2):
        s_odd.acquire()
        print(i)
        s_even.release()


if __name__ == "__main__":
    s_even = Semaphore(1)
    s_odd = Semaphore(0)

    t1 = Thread(target=count_even, args=(s_even, s_odd))
    t2 = Thread(target=count_odd, args=(s_even, s_odd))

    t1.start()
    t2.start()
