"""
REF: http://massivealgorithms.blogspot.jp/2014/07/dynamic-programming-set-11-egg-dropping.html
"""


class Solution:
    """
    @param: m: the number of eggs
    @param: n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        if not m or not n:
            return 0

        INFINITY = float('inf')

        """
        `dp[i][j]` means the minimum drops to verify
        the worst case in `j` floors with `i` eggs
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        """
        only one egg
        """
        for i in range(1, m + 1):
            dp[i][1] = 1

        """
        only one floor
        """
        for j in range(1, n + 1):
            dp[1][j] = j

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = INFINITY

                for k in range(1, j + 1):
                    """
                    backtracking to drop one egg on arbitrary floor `k`
                    there is two cases, if previous egg is:

                    1. broken: reduce to subproblem (m - 1, k - 1)
                        dp[i - 1][k - 1] + 1 drop
                    2. not broken: reduce to subproblem (m, n - k)
                        dp[i][j - k] + 1 drop
                    """
                    _worst = max(dp[i - 1][k - 1], dp[i][j - k]) + 1

                    """
                    find the minimum worst case
                    """
                    if _worst < dp[i][j]:
                        dp[i][j] = _worst

        return dp[m][n]
