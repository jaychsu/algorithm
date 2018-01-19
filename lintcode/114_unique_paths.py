class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]

        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        return dp[m - 1][n - 1]
