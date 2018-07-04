from _test.python import *
from heap.python import *


class TestHeap(TestBase):
    def _test_heapify(self, Heap):
        h = Heap([i for i in range(5)] * 2)

        self.assertEqual(len(h), 10)
        self.assertEqual(h.top(), 0)
        self.assertEqual(
            [h.pop() for _ in range(10)],
            [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        )
        self.assertEqual(len(h), 0)

        with self.assertRaises(IndexError):
            h.pop()
            h.pop()
            h.pop()

    def _test_push(self, Heap):
        CASES = (1, 2, 3, 1, 3, 2, 0, 1, 4)
        h = Heap()
        self.assertEqual(len(h), 0)

        for i in range(len(CASES)):
            self.assertIsNone(h.push(CASES[i]))
            self.assertEqual(len(h), i + 1)

        self.assertEqual(
            [h.pop() for _ in range(len(CASES))],
            [0, 1, 1, 1, 2, 2, 3, 3, 4]
        )
        self.assertEqual(len(h), 0)

        with self.assertRaises(IndexError):
            h.pop()
            h.pop()
            h.pop()

    def _test_pop(self, Heap):
        CASES = list(range(10))
        h = Heap(CASES)
        self.assertEqual(len(h), 10)

        for i in range(len(CASES)):
            self.assertEqual(h.pop(), i)
            self.assertEqual(len(h), len(CASES) - i - 1)

        self.assertEqual(len(h), 0)

        with self.assertRaises(IndexError):
            h.pop()
            h.pop()
            h.pop()

    def _test_remove(self, Heap):
        CASES = (1, 2, 3, 1, 3, 2, 0, 1, 4)
        h = Heap(CASES)
        self.assertEqual(len(h), 9)

        self.assertIsNone(h.remove(1))
        self.assertEqual(len(h), 8)
        self.assertIsNone(h.remove(1))
        self.assertEqual(len(h), 7)
        self.assertIsNone(h.remove(1))
        self.assertEqual(len(h), 6)
        with self.assertRaises(KeyError):
            h.remove(1)
            h.remove(5)
            h.remove(1)

        self.assertEqual(h.pop(), 0)
        self.assertEqual(len(h), 5)

        self.assertEqual(h.top(), 2)
        self.assertEqual(len(h), 5)
        self.assertIsNone(h.push(1))
        self.assertEqual(len(h), 6)
        self.assertEqual(h.top(), 1)
        self.assertEqual(len(h), 6)
        self.assertIsNone(h.remove(1))
        self.assertEqual(h.top(), 2)
        self.assertEqual(len(h), 5)

        self.assertEqual(h.pop(), 2)
        self.assertEqual(len(h), 4)
        self.assertIsNone(h.remove(3))
        self.assertEqual(len(h), 3)
        self.assertIsNone(h.remove(2))
        self.assertEqual(len(h), 2)
        self.assertIsNone(h.remove(3))
        self.assertEqual(len(h), 1)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(len(h), 0)
        with self.assertRaises(KeyError):
            h.remove(-1)
            h.remove(0)
            h.remove(1)
            h.remove(2)
            h.remove(3)
            h.remove(4)
            h.remove(5)

    def _test_top(self, Heap):
        CASES = (1, 2, 3, 1, 3, 2, 0, 1, 4)
        h = Heap(CASES)
        self.assertEqual(len(h), 9)

        for _ in range(len(CASES)):
            self.assertEqual(h.top(), h.pop())

        self.assertEqual(len(h), 0)

        with self.assertRaises(IndexError):
            h.top()
            h.top()
            h.top()

    def _run_heap_test(self, Heap):
        self._test_heapify(Heap)
        self._test_push(Heap)
        self._test_pop(Heap)
        self._test_top(Heap)

    def _run_removable_heap_test(self, Heap):
        self._test_heapify(Heap)
        self._test_push(Heap)
        self._test_pop(Heap)
        self._test_remove(Heap)
        self._test_top(Heap)

    def test_binary_hash_heap(self):
        self._run_removable_heap_test(BinaryHashHeap)

    def test_binary_heap(self):
        self._run_heap_test(BinaryHeap)

    def test_lazy_removable_heapq(self):
        self._run_removable_heap_test(LazyRemovableHeapq)

    def test_removable_heapq(self):
        self._run_removable_heap_test(RemovableHeapq)
