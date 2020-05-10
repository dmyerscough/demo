#!/usr/bin/env python


def fib():
    """
    Fibonacci numbers
    """
    a, b = 0, 1

    while True:
        a, b = b, a + b
        yield a
