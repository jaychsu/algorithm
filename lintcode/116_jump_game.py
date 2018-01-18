"""
Greedy

https://leetcode.com/articles/jump-game/
"""
class Solution:
    def canJump(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False

        last_at = len(A) - 1

        for i in range(last_at, -1, -1):
            if i + A[i] >= last_at:
                last_at = i

        return last_at == 0


"""
DP
"""
class Solution:
    def canJump(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
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
