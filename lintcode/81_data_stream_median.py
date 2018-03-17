import heapq


class Solution:
    def medianII(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        ans = []
        if not nums:
            return ans

        minheap = []
        maxheap = []
        median = 0

        for num in nums:
            if num < median:
                heapq.heappush(maxheap, -num)
            else:
                heapq.heappush(minheap, num)

            while len(minheap) > len(maxheap):
                heapq.heappush(maxheap, -heapq.heappop(minheap))

            while len(maxheap) > len(minheap) + 1:
                heapq.heappush(minheap, -heapq.heappop(maxheap))

            if maxheap:
                median = -maxheap[0]
            else:
                median = 0

            ans.append(median)

        return ans
