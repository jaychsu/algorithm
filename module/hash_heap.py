# TODO
# class HashHeap:

from heapq import heappush, heappop


class HashHeapq:
    def __init__(self):
        self.heap = []
        self.deleted = {}

    def __repr__(self):
        return repr(self.heap)

    def push(self, val):
        heappush(self.heap, val)

    def pop(self):
        if self.is_empty():
            return
        return heappop(self.heap)

    def remove(self, val):
        if self.is_empty():
            return
        self.deleted[val] = self.deleted.get(val, 0) + 1

    def top(self):
        if self.is_empty():
            return
        return self.heap[0]

    def is_empty(self):
        while self.heap and self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1
            heappop(self.heap)
        return not self.heap
