import timeit


def fibo(n):
    a, b = 1, 1
    i = 1
    while i != n:
        a, b = b, a + b
        i += 1
    return a


if __name__ == "__main__":
    VALUE = 100
    COUNT = 1000
    REPEAT = 100
    py = (timeit.repeat('fibo(VALUE)',
                       repeat=REPEAT,
                       number=COUNT,
                       globals=globals()))
    print(sum(py)/len(py))
