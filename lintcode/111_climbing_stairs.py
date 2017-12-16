"""
DP: rolling array with `n + 1`
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <= 0:
            return 0

        dp = [0] * 3

        pre2, pre1, curr = 0, 0, 1
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            pre2 = pre1
            pre1 = curr
            curr = i % 3

            dp[curr] = dp[pre1] + dp[pre2]

        return dp[curr]


"""
DP: origin `n`
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <= 0:
            return 0

        dp = [0] * n

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


"""
DP: origin `n + 1`
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <= 0:
            return 0

        dp = [0] * (n + 1)

        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
