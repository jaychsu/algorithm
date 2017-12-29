from heapq import heappop, heappush


class Solution:
    """
    @param: G: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, G):
        ans = []
        if not G:
            return ans

        heap = []
        for i in range(len(G)):
            if not G[i]:
                continue

            heappush(heap, (G[i][0], i, 0))

        while heap:
            num, x, y = heappop(heap)
            ans.append(num)
            if y + 1 < len(G[x]):
                heappush(heap, (G[x][y + 1], x, y + 1))

        return ans
