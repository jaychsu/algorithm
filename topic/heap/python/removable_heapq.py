"""
in `remove`, we cannot record index in hashmap
since index in `heapq` changed all the time
"""


import heapq


class RemovableHeapq:
    def __init__(self, iterable=None):
        self.__heap = []

        if iterable:
            self.heapify(iterable)

    def __len__(self):
        return len(self.__heap)

    def __bool__(self):
        return bool(self.__heap)

    def heapify(self, iterable):
        if not iterable:
            return

        for val in iterable:
            self.push(val)

    def push(self, val):
        heapq.heappush(self.__heap, val)

    def pop(self):
        if not self.__heap:
            raise IndexError('index out of range')

        return heapq.heappop(self.__heap)

    def remove(self, val):
        if not self.__heap:
            raise ValueError('value was not in heap')

        i = 0
        n = len(self.__heap)

        while i < n and self.__heap[i] != val:
            i += 1

        if i == n:
            raise ValueError('value was not in heap')

        if i == n - 1:
            self.__heap.pop()
        else:
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    def top(self):
        if not self.__heap:
            raise IndexError('index out of range')

        return self.__heap[0]
