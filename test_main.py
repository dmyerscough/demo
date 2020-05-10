#!/usr/bin/env python

import unittest

from main import fib


class TestFib(unittest.TestCase):

    def test_fib(self):
        """
        Test fibonacci
        """
        fibonacci = []

        s = fib()

        for _ in range(0, 11):
            fibonacci.append(next(s))

        self.assertEqual(fibonacci, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


if __name__ == '__main__':

    unittest.main()
