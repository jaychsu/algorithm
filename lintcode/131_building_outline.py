"""
this problem familiar with `leetcode/218_the_skyline_problem.py`
with different output
"""
import heapq


class HashHeapq:
    def __init__(self):
        self.heap = []
        self.deleted = {}

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        if self.is_empty():
            return -1

        return heapq.heappop(self.heap)

    def remove(self, val):
        if self.is_empty():
            return

        if val not in self.deleted:
            self.deleted[val] = 0

        self.deleted[val] += 1

    def top(self):
        if self.is_empty():
            return -1

        return self.heap[0]

    def is_empty(self):
        while self.heap and self.deleted.get(self.heap[0]):
            val = heapq.heappop(self.heap)
            self.deleted[val] -= 1

        return not self.heap


class Solution:
    def buildingOutline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not buildings:
            return ans

        time = []

        for x, _x, height in buildings:
            time.append((x, height, True))
            time.append((_x, height, False))

        time.sort()
        heap = HashHeapq()
        tmp = []

        for x, height, is_start in time:
            if is_start:
                heap.push(-height)
            else:
                heap.remove(-height)

            max_h = -heap.top() if not heap.is_empty() else 0

            if tmp and tmp[-1][0] == x:
                tmp.pop()
            if tmp and tmp[-1][1] == max_h:
                continue
            tmp.append([x, max_h])

        _x = pre_h = 0

        for x, height in tmp:
            if pre_h > 0:
                ans.append([_x, x, pre_h])

            _x = x
            pre_h = height

        return ans
