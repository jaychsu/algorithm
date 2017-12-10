"""
Rolling Array
"""
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        if not m or not A or not V:
            return 0

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) for _ in range(2)]

        prev = curr = 0
        for i in range(1, len(A) + 1):
            prev = curr
            curr = 1 - curr
            for w in range(1, m + 1):
                dp[curr][w] = dp[prev][w]

                if w >= A[i - 1]:
                    dp[curr][w] = max(
                        dp[curr][w],
                        dp[prev][w - A[i - 1]] + V[i - 1]
                    )

        return dp[curr][m]


"""
Origin
"""
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        if not m or not A or not V:
            return 0

        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                dp[i][w] = dp[i - 1][w]

                if w >= A[i - 1]:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i - 1][w - A[i - 1]] + V[i - 1]
                    )

        return dp[n][m]
