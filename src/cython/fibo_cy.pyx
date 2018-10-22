def fibo(n int):
    i int = 0
    a int = 1
    b int = 1
    while i != n:
        a, b = b, a + b
        i += 1
    return a

  