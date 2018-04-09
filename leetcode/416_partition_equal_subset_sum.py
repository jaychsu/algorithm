"""
REF: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592


`dp[s]` means the specific sum `s` can be gotten from the sum of subset in `nums`
"""


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        target = sum(nums)

        if target & 1 == 1:
            return False

        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True

        for a in nums:
            for s in range(target, a - 1, -1):
                if dp[s]:
                    continue

                dp[s] = dp[s - a]

        return dp[target]
