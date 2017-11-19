"""
Test Case:

[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
7
"""
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not target:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        mid = x = y = 0

        while l + 1 < r:
            mid = l + (r - l) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] > target:
                r = mid
            else:
                l = mid

        for end in [l, r]:
            x, y = end // n, end % n
            if matrix[x][y] == target:
                return True

        return False
