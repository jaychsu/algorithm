class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for j in range(n):
            if j == 0:
                dp[0][j] = grid[0][j]
                continue

            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

            for j in range(1, n):
                if dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
