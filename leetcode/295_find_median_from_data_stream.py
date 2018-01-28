from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, a):
        """
        :type a: int
        :rtype: void
        """
        if a < self.findMedian():
            heappush(self.maxheap, -a)
        else:
            heappush(self.minheap, a)

        # to handle odd case, it make sure `minheap` has one more child than `maxheap`
        while len(self.minheap) > len(self.maxheap) + 1:
            heappush(self.maxheap, -heappop(self.minheap))

        # to handle even case, it make sure `minheap` and `maxheap` are same size
        while len(self.maxheap) > len(self.minheap):
            heappush(self.minheap, -heappop(self.maxheap))

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.minheap:
            return 0

        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0] * 1.0

        # since the child in maxheap is negative
        return (self.minheap[0] - self.maxheap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
