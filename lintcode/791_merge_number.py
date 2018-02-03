from heapq import heappush, heappop


class Solution:
    """
    @param A: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, A):
        ans = 0
        if not A:
            return ans

        heap = []

        for a in A:
            heappush(heap, a)

        while len(heap) > 1:
            _sum = heappop(heap) + heappop(heap)
            ans += _sum
            heappush(heap, _sum)

        return ans
