"""
DP: MLE
"""
class Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    def backPackV(self, A, target):
        if not A:
            return 0

        n = len(A)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1]:
                    dp[i][j] += dp[i - 1][j - A[i - 1]]

        return dp[n][target]


"""
DP: optimized space complexity
"""
class Solution:
    """
    @param: A: an integer array and all positive numbers
    @param: target: An integer
    @return: An integer
    """
    def backPackV(self, A, target):
        if not A:
            return 0

        n = len(A)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(target, A[i] - 1, -1):
                dp[j] += dp[j - A[i]]

        return dp[target]
