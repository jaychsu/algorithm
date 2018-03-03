class Solution:
    """
    @param g: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, g):
        ans = 0
        if not g or not g[0]:
            return ans

        m, n = len(g), len(g[0])

        for i in range(m):
            left, right = 0, n - 1

            while left + 1 < right:
                mid = (left + right) // 2
                if g[i][mid] < 0:
                    left = mid
                else:
                    right = mid

            if g[i][left] >= 0:
                continue

            ans += left + 1 if g[i][right] >= 0 else right + 1

        return ans
