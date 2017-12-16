class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(2)]

        prev = curr = 0

        for j in range(n):
            dp[curr][j] = 1

        for i in range(1, m):
            prev = curr
            curr = 1 - prev

            dp[curr][0] = 1

            for j in range(1, n):
                dp[curr][j] = dp[prev][j] + dp[curr][j - 1]

        return dp[curr][n - 1]
