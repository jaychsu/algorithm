"""
Test Case

[3,6,4]

[1,3,2,1,5]
"""
"""
if we insist on not stealing one of the houses
=> the remaining houses become a sequence
=> the problem becomes `./lintcode/392_house_robber.py`

we can pick any pair of adjacent houses,
and to make the calculation easier,
we pick the first and last houses

1. insist on not stealing the first house
   that is, the range becomes `[1, n - 1]`
2. insist on not stealing the last house
   that is, the range becomes `[0, n - 2]`

and choose the maximum amount as the answer
"""
class Solution:
    """
    @param: A: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return A[0]

        dp = [[0] * 2 for _ in range(2)]

        return max(
            self.houseRobber(A, 0, dp),
            self.houseRobber(A, 1, dp)
        )

    def houseRobber(self, A, start, dp):
        n = len(A)
        prev, curr = 0, start % 2
        dp[curr][0] = 0
        dp[curr][1] = A[start]

        for i in range(1 + start, n - 1 + start):
            prev = curr
            curr = i % 2

            dp[curr][0] = max(dp[prev])
            dp[curr][1] = dp[prev][0] + A[i]

        return max(dp[curr])
