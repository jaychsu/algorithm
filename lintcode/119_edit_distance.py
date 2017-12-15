class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, A, B):
        if A is None or B is None:
            return 0

        m, n = len(A), len(B)

        """
        `dp[i][j]` means the minimum operations to convert
        the substr end at `A[i - 1]` to
        the substr end at `B[j - 1]`
        """
        dp = [[0] * (n + 1) for _ in range(2)]

        prev = curr = 0

        for j in range(n + 1):
            dp[curr][j] = j

        for i in range(1, m + 1):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = i

            for j in range(1, n + 1):
                """
                no need to init dp[curr][j]

                case 1: no need to do any operations
                """
                if A[i - 1] == B[j - 1]:
                    dp[curr][j] = dp[prev][j - 1]
                    continue

                """
                case 2: remove last char in A
                case 3: add `B[j - 1]` to the end of A
                case 4: replace laster char in A
                """
                dp[curr][j] = 1 + min(
                    dp[prev][j],
                    dp[curr][j - 1],
                    dp[prev][j - 1]
                )

        return dp[curr][n]
