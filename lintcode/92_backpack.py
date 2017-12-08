class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        if not A:
            return 0

        n = len(A)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(m + 1):
                dp[i][j] = dp[i - 1][j]
                if (j >= A[i - 1]
                    and dp[i - 1][j - A[i - 1]]):
                    dp[i][j] = True

        for j in range(m, -1, -1):
            if dp[n][j]:
                return j

        return 0
