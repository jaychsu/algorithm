'''
Test Case

["MedianFinder","addNum","addNum","findMedian","addNum","findMedian","addNum"]
[[],[1],[2],[],[3],[],[5]]

["MedianFinder","addNum","findMedian"]
[[],[1],[]]
: r > l > 0 -> r > l and r > 0
: 0 < r < l -> l > r and l > 0
: r == l -> r == l > 0

["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
: if not num -> if not isinstance(num, int)

'''

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not isinstance(num, int):
            return
        if num > self.findMedian():
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, - num)

    def findMedian(self):
        """
        :rtype: float
        """
        self.balance()
        l = len(self.max_heap)
        r = len(self.min_heap)
        median = 0
        if r > l and r > 0:
            median = self.min_heap[0]
        elif l > r and l > 0:
            median = - self.max_heap[0]
        elif r == l > 0:
            median = (self.min_heap[0] + self.max_heap[0]) / 2 - self.max_heap[0]
        return float(median)

    def balance(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        if abs(r - l) <= 1:
            return
        if r > l:
            heappush(self.max_heap, - heappop(self.min_heap))
        else:
            heappush(self.min_heap, - heappop(self.max_heap))
        self.balance()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
