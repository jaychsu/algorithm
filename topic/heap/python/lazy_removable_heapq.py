import collections
import heapq


class LazyRemovableHeapq:
    def __init__(self, iterable=None):
        self.__heap = []
        self.__size = 0
        self.__cnts = collections.defaultdict(int)

        if iterable:
            self.heapify(iterable)

    def __len__(self):
        return self.__size

    def __bool__(self):
        return self.__size > 0

    def heapify(self, iterable):
        if not iterable:
            return

        for val in iterable:
            self.push(val)

    def push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1
        self.__cnts[val] += 1

    def pop(self):
        if self._is_empty():
            raise IndexError('index out of range')

        val = heapq.heappop(self.__heap)
        self.__size -= 1
        self.__cnts[val] -= 1
        return val

    def remove(self, val):
        if self._is_empty() or self.__cnts.get(val, 0) < 1:
            raise ValueError('value was not in heap')

        self.__size -= 1
        self.__cnts[val] -= 1

    def top(self):
        if self._is_empty():
            raise IndexError('index out of range')

        return self.__heap[0]

    def _is_empty(self):
        while self.__heap and self.__cnts.get(self.__heap[0]) == 0:
            heapq.heappop(self.__heap)

        return self.__size == 0
