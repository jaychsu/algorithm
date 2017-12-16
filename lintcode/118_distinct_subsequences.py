class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        if S is None or T is None:
            return 0

        if S is '' and '':
            return 1

        m, n = len(S), len(T)

        """
        `dp[i][j]` means the count of distinct subsequences
        (the substr end at `T[j - 1]`) in the substr end at `S[i - 1]`
        """
        dp = [[0] * (n + 1) for _ in range(2)]

        prev = curr = 0
        dp[curr][0] = 1
        for i in range(1, m + 1):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = 1

            for j in range(1, n + 1):
                """
                case 1: `S[i - 1]` and `T[j - 1]` is not a pair
                so keep `T[j - 1]` in candidates
                """
                dp[curr][j] = dp[prev][j]

                """
                case 2: `S[i - 1]` and `T[j - 1]` is a pair
                do NOT `+1` -> its for size, this problem is for count
                """
                if S[i - 1] == T[j - 1]:
                    dp[curr][j] += dp[prev][j - 1]

        return dp[curr][n]
