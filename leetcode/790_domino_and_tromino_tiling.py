class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 3:
            return N

        MOD = 10 ** 9 + 7
        dp = [0] * (N + 1)
        dp[:3] = 1, 1, 2

        for i in range(3, N + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % MOD

        return dp[N]
