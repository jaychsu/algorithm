class Solution:
    """
    @param: G: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, G, target):
        if not G or target is None:
            return False

        m, n = len(G), len(G[0])
        left, right = 0, m * n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n

            if G[x][y] == target:
                return True

            if G[x][y] < target:
                left = mid
            else:
                right = mid

        for mid in (left, right):
            x = mid // n
            y = mid % n
            if G[x][y] == target:
                return True

        return False
