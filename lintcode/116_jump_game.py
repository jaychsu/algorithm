"""
Greedy

https://leetcode.com/articles/jump-game/
"""
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return False

        # the last position to get to the destination
        _last = len(A) - 1

        for i in range(_last, -1, -1):
            # if:
            # `i` (the distance from the starting position)
            # + `A[i]` (the maximum jump length)
            # is great than `_last` (the last position to get to the destination)
            # and then we can reach the `_last` if we at `i`
            if i + A[i] >= _last:
                _last = i

        return _last == 0


"""
DP
"""
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return False

        n = len(A)
        dp = [False] * n

        """
        `dp[i]` means `i` could be reached
        """
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                """
                backtracking
                if `j` could be reached
                """
                if dp[j] and j + A[j] >= i:
                    """
                    if jump from `j` can reach `i`
                    """
                    dp[i] = True
                    break

        return dp[n - 1]
