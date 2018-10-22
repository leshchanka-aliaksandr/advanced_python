def fibo(int n):
    cdef int a, b, i
    a, b, i = 1, 1, 1
    while i != n:
        a, b = b, a + b
        i += 1
    return a

  