class Solution:
    """
    @param: V: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, V):
        if not V:
            return False

        n = len(V)

        # `dp[i][j]` means the maximum value when the current player
        # chosen from `V[i:j+1]`
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = V[i]

        for i in range(n - 1 - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(
                    V[i] - dp[i + 1][j],
                    V[j] - dp[i][j - 1]
                )

        return dp[0][n - 1] >= 0
