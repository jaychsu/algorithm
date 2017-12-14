from heapq import heappop, heappush


class Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        if not nums or not k:
            return -1

        heap = []
        for num in nums:
            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)

        return heappop(heap)
