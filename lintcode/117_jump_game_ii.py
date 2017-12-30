"""
Greedy
"""
class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A:
            return -1

        target = len(A) - 1
        start = end = jumps = 0

        while end < target:
            jumps += 1
            furthest = end
            for i in range(start, end + 1):
                if i + A[i] > furthest:
                    furthest = i + A[i]
            start = end + 1
            end = furthest

        return jumps


"""
DP
"""
class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A:
            return -1

        INFINITY = float('inf')

        n = len(A)
        dp = [INFINITY] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if (dp[j] < INFINITY and j + A[j] >= i and
                    dp[j] + 1 < dp[i]):
                    dp[i] = dp[j] + 1

        return dp[n - 1]
