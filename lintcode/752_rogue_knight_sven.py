class Solution:
    def getNumberOfWays(self, n, m, limit, cost):
        """
        :type n: int
        :type m: int
        :type limit: int
        :type cost: List[int]
        :rtype: int
        """

        """
        `dp[i][j]` means the ways to reach planet `i` and still keep `j` coins
        """
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][m] = 1

        for i in range(1, n + 1):
            for j in range(m + 1):
                for k in range(max(0, i - limit), i):
                    if j + cost[i] > m:
                        continue
                    dp[i][j] += dp[k][j + cost[i]]

        return sum(dp[n])
