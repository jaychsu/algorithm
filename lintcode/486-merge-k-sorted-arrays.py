from heapq import heappush, heappop

class Solution:
    """
    @param: arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        ans = []
        if not arrays:
            return ans
        heap = []
        for i in range(len(arrays)):
            if arrays[i]:
                heappush(heap, (arrays[i][0], i, 0))
        while heap:
            val, x, y = heappop(heap)
            ans.append(val)
            if y + 1 < len(arrays[x]):
                heappush(heap, (arrays[x][y + 1], x, y + 1))
        return ans
