from heapq import heappush, heappop

class HashHeap:
    def __init__(self):
        self.heap = []
        self.deleted = {}
        self._len = 0

    def push(self, val):
        heappush(self.heap, val)
        self._len += 1

    def pop(self):
        self._clean_top()
        self._len -= 1
        return heappop(self.heap)

    def remove(self, val):
        self.deleted[val] = self.deleted.get(val, 0) + 1
        self._len -= 1

    def top(self):
        self._clean_top()
        return self.heap[0]

    def _clean_top(self):
        while self.heap and self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1
            heappop(self.heap)

    def __len__(self):
        return self._len

    def __repr__(self):
        return repr(self.heap)
