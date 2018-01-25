"""
REF: https://briangordon.github.io/2014/08/the-skyline-problem.html
"""
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
        return not bool(self.heap)


class Solution:
    def getSkyline(self, B):
        """
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not B:
            return ans

        T = []  # timeline

        for left, right, height in B:
            T.append((left, -height, True))
            T.append((right, -height, False))

        T.sort()
        heap = HashHeapq()

        for x, height, is_shown in T:
            if is_shown:
                heap.push(height)
            else:
                heap.remove(height)

            Hmax = heap.top() if not heap.is_empty() else 0
            if ans and ans[-1][0] == x:
                ans.pop()
            if ans and ans[-1][1] == -Hmax:
                continue
            ans.append([x, -Hmax])

        return ans
