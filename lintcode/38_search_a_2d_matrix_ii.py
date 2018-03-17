"""
Heap
"""
import heapq


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: int
        """
        ans = 0
        if not matrix or not matrix[0]:
            return ans

        heap = []
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while heap and heap[0][0] <= target:
            num, x, y = heapq.heappop(heap)

            if num == target:
                ans += 1

            y += 1
            if y < n:
                heapq.heappush(heap, (matrix[x][y], x, y))

        return ans


"""
Iteration
"""
class Solution:
    """
    @param: G: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, G, target):
        if not G or not G[0]:
            return 0

        m, n = len(G), len(G[0])
        x, y = m - 1, 0
        ans = 0

        """
        start from bottom-left of G
        """
        while x >= 0 and y < n:
            """
            since NO duplicate integers in each row or column
            """
            if G[x][y] == target:
                ans += 1
                x -= 1
                y += 1
                continue

            """
            since start from bottom-left

            if `G[x][y] > target`:
                need to check `x - 1`
                all cells before `y - 1` are confirmed in last iteration
            else:
                all cells before `x + 1` are confirmed in last iteration
                need to check `y + 1`
            """
            if G[x][y] > target:
                x -= 1
            else:
                y += 1

        return ans
