import heapq

class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        ans = j = 0
        heap, m, n = [], len(matrix), len(matrix[0])
        for i in range(min(k, m)): heapq.heappush(heap, (matrix[i][0], i, 0))
        while k > 0:
            ans = heapq.heappop(heap)
            j = ans[2] + 1
            if j < n:
                heapq.heappush(heap, (matrix[ans[1]][j], ans[1], j))
            k -= 1
        return ans[0]
