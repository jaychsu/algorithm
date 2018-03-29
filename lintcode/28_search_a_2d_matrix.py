class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: list[list[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n

            if matrix[x][y] < target:
                left = mid
            elif matrix[x][y] > target:
                right = mid
            else:
                return True

        return any(
            matrix[mid // n][mid % n] == target
            for mid in (left, right)
        )
