import unittest
from _test.python import *
from bitwise_operation.python import *


class TestBitCalculator(unittest.TestCase):
    CASES = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1), ( 0, 0), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),

        # (-0x80000000, -1),
        # (-0x80000000,  1),
        # ( 0x7FFFFFFF, -1),
        # ( 0x7FFFFFFF,  1),
        # (-1, -0x80000000),
        # (-1,  0x7FFFFFFF),
        # ( 1, -0x80000000),
        # ( 1,  0x7FFFFFFF),

        (-9, -7), (-9,  7),
        ( 9, -7), ( 9,  7),
        (-7, -9), (-7,  9),
        ( 7, -9), ( 7,  9),

        (-123,    0),
        ( 123,    0),
        (   0, -123),
        (   0,  123),
    )

    @classmethod
    def setUpClass(cls):
        starting_test(cls.__name__)

    @classmethod
    def tearDownClass(cls):
        finished_test(cls.__name__)

    def test_plus_recursion(self):
        for a, b in self.CASES:
            self.assertEqual(a + b, Calculator._plus(a, b))

    def test_plus_iteration(self):
        for a, b in self.CASES:
            self.assertEqual(a + b, Calculator.plus(a, b))

    def test_minus(self):
        for a, b in self.CASES:
            self.assertEqual(a - b, Calculator.minus(a, b))

    def test_times(self):
        for a, b in self.CASES:
            self.assertEqual(a * b, Calculator.times(a, b))

    def test_divide(self):
        c = None
        for a, b in self.CASES:
            if not b:
                c = float('inf') if a >= 0 else float('-inf')
            elif not a:
                c = 0
            else:
                c = a // b

            self.assertEqual(c, Calculator.divide(a, b))
