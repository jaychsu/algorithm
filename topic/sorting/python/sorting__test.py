import unittest
from _test.python import *
from sorting.python import *


class TestSorting(unittest.TestCase):

    CASES = (
        (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, -1, -1, -1, 0, 1, -1),
        (-2, -5, 3, 7, 6, 6, 0, -9, 7, 2),
        (-6, -3, -9, -1, 0, 2, 2, 8, 6),
        (18, 3, 18, 2, 15, 0, -12, -10, -12, -3),
        (-4, -18, -13, -10, -10, 0, 13, 5, 1, 1),
        (70, 91, 92, -42, -4, 13, -12, -94, -56, -70, 34, -97, 58, -14, -75),
    )

    @classmethod
    def setUpClass(cls):
        starting_test(cls.__name__)

    @classmethod
    def tearDownClass(cls):
        finished_test(cls.__name__)

    def _run_sorting_test(self, _sort):
        A = B = None
        for case in self.CASES:
            A = list(case)
            B = list(case)

            B.sort()
            _sort(A)

            self.assertIsNot(B, A)
            self.assertEqual(B, A)

    def test_quick_sort(self):
        self._run_sorting_test(quick_sort)

    def test_merge_sort(self):
        self._run_sorting_test(merge_sort)
