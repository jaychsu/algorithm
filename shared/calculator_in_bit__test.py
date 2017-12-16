import unittest
from _test_helper import *

from calculator_in_bit import Calculator


class TestBitCalculator(unittest.TestCase):
    CASES = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1),

        (9, 7), (9, -7),
        (-7, 9), (7, -9),

        (-23, -7), (23, -7),
        (-7, 23), (7, -23),
    )

    @classmethod
    def setUpClass(cls):
        show_msg(cls.__name__, msg_type='starting')

    @classmethod
    def tearDownClass(cls):
        show_msg(cls.__name__, msg_type='finished')

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
