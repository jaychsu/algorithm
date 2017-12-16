class Solution:
    """
    @param: obstacles: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacles):
        m, n = len(obstacles), len(obstacles[0])

        dp = [[0] * n for _ in range(2)]

        prev = curr = 0

        for j in range(n):
            if obstacles[0][j]:
                break

            if j == 0:
                dp[curr][j] = 1
                continue

            dp[curr][j] = dp[curr][j - 1]

        for i in range(1, m):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = dp[prev][0] if not obstacles[i][0] else 0

            for j in range(1, n):
                dp[curr][j] = 0

                if not obstacles[i][j]:
                    dp[curr][j] = dp[prev][j] + dp[curr][j - 1]

        return dp[curr][n - 1]
