import sys

sys.setrecursionlimit(1 << 30)


def f():
    """Segfault method"""

    f()


if __name__ == "__main__":
    f()
