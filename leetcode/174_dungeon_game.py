class Solution:
    def calculateMinimumHP(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        INFINITY = float('inf')
        m, n = len(G), len(G[0])
        dp = [[INFINITY] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - G[i][j]
                if dp[i][j] <= 0:
                    dp[i][j] = 1

        return dp[0][0]
