class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0] or len(matrix) != len(matrix[0]):
            return

        n = len(matrix)

        # swap by diagonal axis
        for i in range(n - 1):
            for j in range(n - 1 - i):
                x = n - 1 - j
                y = n - 1 - i
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]

        # swap by x-mid axis
        for i in range(n // 2):
            for j in range(n):
                x = n - 1 - i
                y = j
                matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0] or len(matrix) != len(matrix[0]):
            return

        n = len(matrix)
        ans = [[0] * n for _ in range(n)]

        for x in range(n):
            for y in range(n):
                ans[y][n - 1 - x] = matrix[x][y]

        matrix[:] = ans[:]
