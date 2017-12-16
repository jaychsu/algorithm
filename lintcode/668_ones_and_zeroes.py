"""
optimized space complexity
"""
class Solution:
    """
    @param: strs: an array with strings include only 0 and 1
    @param: m: An integer
    @param: n: An integer
    @return: find the maximum number of strings
    """
    def findMaxForm(self, strs, m, n):
        if not strs:
            return 0

        """
        `dp[j][k]` means the current str can be made up of
        `j` 0s and `k` 1s
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        c0 = c1 = 0
        for s in strs:
            c0 = s.count('0')
            c1 = len(s) - c0

            for j in range(m, c0 - 1, -1):
                for k in range(n, c1 - 1, -1):
                    """
                    case 1: included current `strs[i - 1]`
                    case 2: not included current `strs[i - 1]`, same as previous
                    """
                    dp[j][k] = max(
                        dp[j][k],
                        dp[j - c0][k - c1] + 1
                    )

        return dp[m][n]


"""
origin
"""
class Solution:
    """
    @param: strs: an array with strings include only 0 and 1
    @param: m: An integer
    @param: n: An integer
    @return: find the maximum number of strings
    """
    def findMaxForm(self, strs, m, n):
        if not strs:
            return 0

        l = len(strs)

        """
        `dp[i][j][k]` means the pre- `i`th strs can be made up of
        `j` 0s and `k` 1s

        dp[0][j][k] = 0
        """
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]

        c0 = c1 = 0
        for i in range(1, l + 1):
            c0 = strs[i - 1].count('0')
            c1 = len(strs[i - 1]) - c0

            for j in range(m + 1):
                for k in range(n + 1):
                    """
                    case 1: included current `strs[i - 1]`
                    """
                    if j >= c0 and k >= c1:
                        dp[i][j][k] = dp[i - 1][j - c0][k - c1] + 1

                    """
                    case 2: not included current `strs[i - 1]`, same as previous
                    """
                    if dp[i - 1][j][k] > dp[i][j][k]:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[l][m][n]
