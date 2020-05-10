#!/usr/bin/env python


def fib():
    """

    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    s = fib()

    for i in range(0, 11):
        print(next(s))
