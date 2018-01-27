from heapq import heappush, heappop


class HashHeapq:
    def __init__(self):
        self.heap = []
        self.deleted = {}

    def push(self, val):
        heappush(self.heap, val)

    def pop(self):
        if self.is_empty():
            return
        heappop(self.heap)

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


class Solution:
    def maxSlidingWindow(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        if not A:
            return ans

        heap = HashHeapq()

        for i in range(len(A)):
            heap.push(-A[i])
            if i >= k - 1:
                ans.append(-heap.top())
                heap.remove(-A[i - k + 1])

        return ans


"""
Failed Solution
Since its a O(n*k) solution
"""
class Solution:
    """
    @param: A: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, A, k):
        ans = []
        if not A or len(A) < 1:
            return ans
        for r in range(len(A)):
            if r >= k - 1:
                ans.append(max(A[r - k + 1 : r + 1]))
        return ans
