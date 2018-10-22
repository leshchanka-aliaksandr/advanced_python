import timeit
import pyximport
import fibo_cy
import fib_count_c

pyximport.install()


def fibo(n):
    a, b = 1, 1
    i = 1
    while i != n:
        a, b = b, a + b
        i += 1
    return a


if __name__ == "__main__":
    VALUE = 30
    COUNT = 1000
    REPEAT = 100
    py = (timeit.repeat('fibo(VALUE)',
                        repeat=REPEAT,
                        number=COUNT,
                        globals=globals()))
    print("py: {:.6f}".format(sum(py) / len(py)))
    cy = (timeit.repeat('fibo_cy.fibo(VALUE)',
                        repeat=REPEAT,
                        number=COUNT,
                        globals=globals()))
    print("cy: {:.6f}".format(sum(cy) / len(cy)))
    cext = (timeit.repeat('fib_count_c.fibo(VALUE)',
                          repeat=REPEAT,
                          number=COUNT,
                          globals=globals()))
    print("cext: {:.6f}".format(sum(cext) / len(cext)))
