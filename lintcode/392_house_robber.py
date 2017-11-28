"""
to borrow the idea of `./lintcode/515_paint_house.py`
a house can be at one of two status: steal or not
"""
class Solution:
    """
    @param: A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0

        n = len(A)
        F = [[0] * 2 for _ in range(2)]
        F[0][1] = A[0]

        prev = curr = 0
        for i in range(1, n):
            prev = curr # (i - 1) % 2
            curr = i % 2

            F[curr][0] = F[prev][0] if F[prev][0] > F[prev][1] else F[prev][1]
            F[curr][1] = F[prev][0] + A[i]

        return max(F[curr])
