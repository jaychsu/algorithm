from heapq import heappush, heappop


class Solution:
    """
    @param: A: A list of integers
    @return: the median of numbers
    """
    def medianII(self, A):
        ans = []
        if not A:
            return ans

        minheap = []
        maxheap = []
        median = 0

        for a in A:
            if a < median:
                heappush(maxheap, -a)
            else:
                heappush(minheap, a)

            while len(minheap) > len(maxheap):
                heappush(maxheap, -heappop(minheap))

            while len(maxheap) > len(minheap) + 1:
                heappush(minheap, -heappop(maxheap))

            median = -self.find_median(maxheap)
            ans.append(median)

        return ans

    def find_median(self, maxheap):
        if not maxheap:
            return 0

        return maxheap[0]
