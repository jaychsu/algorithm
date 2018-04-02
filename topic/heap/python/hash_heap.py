# TODO
# class HashHeap:


import heapq


class HashHeapqWithLazy:
    def __init__(self):
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    def __len__(self):
        return self.__size

    def __bool__(self):
        return self.__size > 0

    def push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    def pop(self):
        if self._is_empty():
            return

        self.__size -= 1
        return heapq.heappop(self.__heap)

    def remove(self, val):
        if self._is_empty():
            return

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    def top(self):
        if self._is_empty():
            return

        return self.__heap[0]

    def _is_empty(self):
        while self.__heap and self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        return self.__size == 0


class HashHeapq:
    def __init__(self):
        self.__heap = []

    def __repr__(self):
        return repr(self.__heap)

    def __len__(self):
        return len(self.__heap)

    def __bool__(self):
        return bool(self.__heap)

    def push(self, val):
        heapq.heappush(self.__heap, val)

    def pop(self):
        if not self.__heap:
            return

        return heapq.heappop(self.__heap)

    def remove(self, val):
        if not self.__heap:
            return

        i = 0
        n = len(self.__heap)

        while i < n and self.__heap[i] != val:
            i += 1

        if i == n:
            return

        if i == n - 1:
            self.__heap.pop()
        else:
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    def top(self):
        if not self.__heap:
            return

        return self.__heap[0]
