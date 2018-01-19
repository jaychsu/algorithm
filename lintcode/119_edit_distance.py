class Solution:
    def minDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None or t is None:
            return 0

        m, n = len(s), len(t)

        """
        `dp[i][j]` means the minimum operations to convert
        the substr end at `A[i - 1]` to
        the substr end at `B[j - 1]`
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                """
                no need to init dp[curr][j]

                case 1: no need to do any operations
                """
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    continue

                """
                case 2: remove last char in A
                case 3: add `B[j - 1]` to the end of A
                case 4: replace laster char in A
                """
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

        return dp[m][n]
