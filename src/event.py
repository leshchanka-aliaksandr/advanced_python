from threading import Event
from threading import Thread


def count_even(e_even, e_odd):
    for i in range(0, 101, 2):
        e_even.wait(1)
        print(i)
        e_even.clear()
        e_odd.set()


def count_odd(e_even, e_odd):
    for i in range(1, 101, 2):
        e_odd.wait(1)
        print(i)
        e_odd.clear()
        e_even.set()


if __name__ == "__main__":
    e_even = Event()
    e_odd = Event()

    e_even.set()

    t1 = Thread(target=count_even, args=(e_even, e_odd))
    t2 = Thread(target=count_odd, args=(e_even, e_odd))

    t1.start()
    t2.start()
