from _test.python import *
from linked_list.python import *


class TestLinkedList(TestBase):
    def _get_instance(self, LinkedList):
        ll = LinkedList()

        for i in range(10):
            ll.add(i)

        self.assertEqual(
            ','.join([str(i) for i in ll]),
            '0,1,2,3,4,5,6,7,8,9'
        )

        return ll

    def _test_set(self, LinkedList):
        ll = self._get_instance(LinkedList)

        for i, val in (
            (0, 11),
            (3, 12),
            (9, 15),
            (-1, 21),
            (-5, 25),
            (-10, 29),
        ):
            self.assertEqual(ll.set(val, i), val)
            self.assertEqual(ll.get(i), val)

        with self.assertRaises(IndexError):
            ll.set(31, 10)
            ll.set(31, 11)
            ll.set(31, -11)
            ll.set(31, -12)

    def _test_get(self, LinkedList):
        ll = self._get_instance(LinkedList)

        with self.assertRaises(IndexError):
            ll.get(10)
            ll.get(11)
            ll.get(15)
            ll.get(-11)
            ll.get(-15)

        self.assertEqual(ll.get(0), 0)
        self.assertEqual(ll.get(5), 5)
        self.assertEqual(ll.get(9), 9)

        self.assertEqual(ll.get(-1), 9)
        self.assertEqual(ll.get(-3), 7)
        self.assertEqual(ll.get(-6), 4)
        self.assertEqual(ll.get(-10), 0)

    def _test_add(self, LinkedList):
        ll = LinkedList()

        self.assertEqual(len(ll), 0)

        i = 0
        for c in 'abcdefg':
            self.assertIsNone(ll.add(c))
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get(i), c)
            i += 1

        for c in range(-1, -10, -1):
            self.assertIsNone(ll.add(c, c))
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll.get(c), c)
            i += 1

        ll.add('Tail_A', -50)
        self.assertEqual(ll.get(-1), 'Tail_A')

        ll.add('Tail_B', 50)
        self.assertEqual(ll.get(-1), 'Tail_B')

    def _test_add_all(self, LinkedList):
        ll = LinkedList()

        self.assertEqual(len(ll), 0)

        with self.assertRaises(ValueError):
            ll.add_all(None)
            ll.add_all(123)

        self.assertIsNone(ll.add_all([i for i in range(5)]))
        self.assertEqual(len(ll), 5)
        self.assertEqual(
            ','.join([str(i) for i in ll]),
            '0,1,2,3,4'
        )

        self.assertIsNone(ll.add_all([i for i in range(5, 10)], -3))
        self.assertEqual(len(ll), 10)
        self.assertEqual(
            ','.join([str(i) for i in ll]),
            '0,1,2,5,6,7,8,9,3,4'
        )

        ll.add_all('Tail_A', -50)
        self.assertEqual(ll.get(-1), 'A')

        ll.add_all('Tail_B', 50)
        self.assertEqual(ll.get(-1), 'B')

    def _test_remove(self, LinkedList):
        ll = self._get_instance(LinkedList)

        self.assertEqual(len(ll), 10)

        with self.assertRaises(IndexError):
            ll.remove(10)
            ll.remove(15)
            ll.remove(-11)
            ll.remove(-15)

        for i in range(2, -1, -1):
            self.assertEqual(ll.remove(i), i)
            self.assertEqual(len(ll), 7 + i)

        for i in range(2, 0, -1):
            self.assertEqual(ll.remove(-i), 10 - i)
            self.assertEqual(len(ll), 4 + i)

        with self.assertRaises(IndexError):
            ll.remove(6)
            ll.remove(-6)

    def _test_contains(self, LinkedList):
        ll = self._get_instance(LinkedList)

        self.assertTrue(ll.contains(0))
        self.assertTrue(ll.contains(3))
        self.assertTrue(ll.contains(9))

        self.assertFalse(ll.contains(-1))
        self.assertFalse(ll.contains(-5))
        self.assertFalse(ll.contains(10))
        self.assertFalse(ll.contains(15))

    def _test_index(self, LinkedList):
        ll = self._get_instance(LinkedList)

        for i in range(10):
            self.assertEqual(ll.index(i), i)

    def _test_last_index(self, LinkedList):
        ll = self._get_instance(LinkedList)

        for i in range(10):
            self.assertEqual(ll.last_index(i), 10 - i)

    def _test_clear(self, LinkedList):
        ll = self._get_instance(LinkedList)

        self.assertEqual(len(ll), 10)

        ll.clear()

        self.assertEqual(len(ll), 0)

    def _test_clone(self, LinkedList):
        pass

    def _test_sort(self, LinkedList):
        pass

    def _run_list_test(self, LinkedList):
        self._test_set(LinkedList)
        self._test_get(LinkedList)
        self._test_add(LinkedList)
        self._test_add_all(LinkedList)
        self._test_remove(LinkedList)
        self._test_contains(LinkedList)
        self._test_index(LinkedList)
        self._test_last_index(LinkedList)
        self._test_clear(LinkedList)
        self._test_clone(LinkedList)
        self._test_sort(LinkedList)

    def test_cyclic_list(self):
        self._run_list_test(CyclicList)

    def test_cyclic_doubly_list(self):
        self._run_list_test(CyclicDoublyList)

    # def test_dummy_tail_list(self):
    #     self._run_list_test(DummyTailList)

    # def test_dummy_tail_doubly_list(self):
    #     self._run_list_test(DummyTailDoublyList)

    # def test_head_tail_list(self):
    #     self._run_list_test(HeadTailList)

    # def test_head_tail_doubly_list(self):
    #     self._run_list_test(HeadTailDoublyList)

    # def test_two_dummy_list(self):
    #     self._run_list_test(TwoDummyList)

    # def test_two_dummy_doubly_list(self):
    #     self._run_list_test(TwoDummyDoublyList)
