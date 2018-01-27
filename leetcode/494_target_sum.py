"""
REF: https://leetcode.com/problems/target-sum/discuss/97334

P: children used in positive,
N: children used in negative,
A: all children

sum(P) - sum(N) = target
=> sum(P) - sum(N) + sum(P) + sum(N) = target + sum(P) + sum(N)
=> 2 * sum(P) = target + sum(A)
=> sum(P) = (target + sum(A)) // 2
=> find the subset sum
"""


class Solution:
    def findTargetSumWays(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        if not A:
            return 0

        _sum = sum(A)
        if _sum < target or (_sum + target) % 2 == 1:
            return 0

        return self.subset_sum(A, (_sum + target) // 2)

    def subset_sum(self, A, target):
        """
        `dp[i]` means the number of ways
        to make sum `i` using non-repeated children in `A`

        `i` from `target` to `a - 1` => to make sure `i >= a`
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for a in A:
            for i in range(target, a - 1, -1):
                dp[i] += dp[i - a]

        return dp[target]
