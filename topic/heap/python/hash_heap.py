# TODO
# class HashHeap:


import heapq


class HashHeapq:
    """
    [Deprecated], TODO
    since the items will be lazy deleted, so the behavior is weird.
    need to explore more
    """
    def __init__(self):
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    def __len__(self):
        return self.__size

    def __bool__(self):
        return not self.is_empty()

    def push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    def pop(self):
        if self.is_empty():
            return

        self.__size -= 1
        return heapq.heappop(self.__heap)

    def remove(self, val):
        if self.is_empty():
            return

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    def top(self):
        if self.is_empty():
            return

        return self.__heap[0]

    def is_empty(self):
        while self.__size and self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        return not self.__heap
