class Solution:
    """
    @param: C: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, C):
        if not C:
            return False

        n = len(C)

        """
        `dp[i][j]` means the maximum value when
        the current player chosen from [i, j] in `C`
        """
        dp = [[0] * n for _ in range(n)]

        """
        recurring from the end of the game to start
        so init with `dp[i][i]`
        """
        for i in range(n):
            dp[i][i] = C[i]

        """
        i   i+1     j-1  j
        c1  c2  c3  c4  c5

        there are two cases:
            1. if the current player chosen `C[i]`, then
               the cost is `dp[i + 1][j]`
            2. if the current player chosen `C[j]`, then
               the cost is `dp[i][j - 1]`

        chosen the maximum
        """
        for i in range(n - 1 - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(
                    C[i] - dp[i + 1][j],
                    C[j] - dp[i][j - 1]
                )

        return dp[0][n - 1] >= 0
