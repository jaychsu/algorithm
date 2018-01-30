from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, G, k):
        """
        :type G: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not G or not G[0]:
            return 0

        heap = []

        for x in range(len(G)):
            heappush(heap, (G[x][0], x, 0))

        while heap:
            a, x, y = heappop(heap)

            k -= 1
            if k == 0:
                return a

            if y + 1 < len(G[x]):
                heappush(heap, (G[x][y + 1], x, y + 1))

        return 0
