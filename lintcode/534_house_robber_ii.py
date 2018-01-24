"""
Main Concept:

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


Test Case:

[3,6,4]

[1,3,2,1,5]
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


class Solution:
    """
    @param: A: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, A):
        if not A:
            return 0

        n = len(A)
        if n == 1:
            return A[0]
        if n == 2:
            return max(A[0], A[1])

        dp = [0] * 3

        return max(
            # range(0, n - 1)
            self.houseRobber(A, 0, dp),
            # range(1, n)
            self.houseRobber(A, 1, dp)
        )

    def houseRobber(self, A, start, dp):
        n = len(A)
        prev2, prev1, curr = 0, start % 3, (start + 1) % 3
        dp[prev1] = A[start]
        dp[curr] = max(A[start], A[start + 1])

        for i in range(2 + start, n - 1 + start):
            prev2, prev1 = prev1, curr
            curr = i % 3

            dp[curr] = max(dp[prev1], dp[prev2] + A[i])

        return dp[curr]


class Solution:
    def houseRobber2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        n = len(A)
        if n < 2:
            return A[0]

        return max(
            self.rob_in_line(A, 0, n - 2),
            self.rob_in_line(A, 1, n - 1)
        )

    def rob_in_line(self, A, start, end):
        n = end - start + 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = A[start]

        for i in range(2, n + 1):
            dp[i] = max(
                dp[i - 2] + A[start + i - 1],
                dp[i - 1]
            )

        return dp[n]
