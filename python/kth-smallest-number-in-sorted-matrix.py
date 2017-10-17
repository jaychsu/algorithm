import heapq

class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        heap = []
        min_child = -1
        for i in range(min(k, m)):
            heapq.heappush(heap, (matrix[i][0], 0, i))
        while k > 0:
            min_child = heapq.heappop(heap)
            x, y = min_child[1], min_child[2]
            if x + 1 < n:
                heapq.heappush(heap, (matrix[y][x + 1], x + 1, y))
            k -= 1
        return min_child[0]
