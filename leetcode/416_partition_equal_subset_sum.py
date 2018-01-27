"""
REF: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592
"""


class Solution:
    def canPartition(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True

        target = sum(A)

        if target & 1 == 1:
            return False

        target //= 2

        """
        `dp[i]` means the specific sum `i` can be gotten from the sum of subset in `A`
        """
        dp = [False] * (target + 1)
        dp[0] = True

        for a in A:
            for i in range(target, a - 1, -1):
                dp[i] = dp[i] or dp[i - a]

        return dp[target]
