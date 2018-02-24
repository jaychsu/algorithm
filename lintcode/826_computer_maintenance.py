class Solution:
    """
    @param m: the rows of matrix
    @param n: the cols of matrix
    @param P: the bad computers
    @return: The answer
    """
    def maintenance(self, m, n, P):
        if not m or not n or not P:
            return 0

        dp = [[0, 0] for _ in range(m)]
        G = [[0] * n for _ in range(m)]

        for p in P:
            G[p.x][p.y] = 1

        for i in range(m):
            left = right = -1

            for j in range(n):
                if G[i][j] == 0:
                    continue
                left = max(left, n - 1 - j)
                right = max(right, j)

            if i == 0:
                if right == -1:
                    dp[i][0] = 0
                    dp[i][1] = n - 1
                else:
                    dp[i][0] = 2 * right
                    dp[i][1] = n - 1
            else:
                if right == -1:
                    dp[i][0] = dp[i - 1][0] + 1
                    dp[i][1] = dp[i - 1][1] + 1
                else:
                    dp[i][0] = 1 + min(
                        dp[i - 1][0] + 2 * right,
                        dp[i - 1][1] + n - 1
                    )
                    dp[i][1] = 1 + min(
                        dp[i - 1][1] + 2 * left,
                        dp[i - 1][0] + n - 1
                    )

        return min(dp[m - 1][0], dp[m - 1][1])
