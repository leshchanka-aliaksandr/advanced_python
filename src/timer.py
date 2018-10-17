from threading import Timer


def counter(i):
    print(i)


if __name__ == "__main__":
    odd = 0
    even = odd + 1
    while odd < 101 and even < 101:
        t1 = Timer(0, counter, args=(odd, ))
        t2 = Timer(0.5, counter, args=(even, ))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        odd += 2
        even += 2
