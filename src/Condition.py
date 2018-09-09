from threading import Condition, Thread


def count_even(c_even, c_odd):

    for i in range(0, 101, 2):
        with c_odd:
            c_odd.wait()
            print(i)
        with c_even:
            c_even.notifyAll()


def count_odd(c_even, c_odd):

    for i in range(1, 101, 2):
        with c_even:
            c_even.wait()
            print(i)
        with c_odd:
            c_odd.notifyAll()


if __name__ == "__main__":
    c_even = Condition()
    c_odd = Condition()

    t1 = Thread(target=count_even, args=(c_even, c_odd,))
    t2 = Thread(target=count_odd, args=(c_even, c_odd,))

    t1.start()
    t2.start()
    with c_odd:
        c_odd.notifyAll()
