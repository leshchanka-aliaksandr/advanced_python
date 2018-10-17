from threading import Lock
from threading import Thread


def count_even(l_even, l_odd):

    for i in range(0, 101, 2):
        l_odd.acquire()
        print(i)
        l_even.release()


def count_odd(l_even, l_odd):

    for i in range(1, 101, 2):
        l_even.acquire()
        print(i)
        l_odd.release()


if __name__ == "__main__":
    l_even = Lock()
    l_even.acquire()
    l_odd = Lock()

    t1 = Thread(target=count_even, args=(l_even, l_odd, ))
    t2 = Thread(target=count_odd, args=(l_even, l_odd, ))

    t1.start()
    t2.start()
