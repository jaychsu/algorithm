class Solution:
    """
    @param: A: an integer array and all positive numbers, no duplicates
    @param: target: An integer
    @return: An integer
    """
    def backPackVI(self, A, target):
        if not A:
            return 0

        n = len(A)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(n):
                if i >= A[j]:
                    dp[i] += dp[i - A[j]]

        return dp[target]
