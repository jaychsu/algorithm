"""
since the fact:
    the minimum negative number * -1 -> the maximum
    the maximum positive number -> the maximum
so we need record the minimum and the maximum number for each child in nums
"""


class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    def maxProduct(self, A):
        if not A:
            return 0

        ans = Pmin = Pmax = A[0]
        for i in range(1, len(A)):
            """
            adding `A[i]` to reset `min` and `max`
            if its so lowest or highest
            """
            C = (A[i], Pmin * A[i], Pmax * A[i])
            Pmin, Pmax = min(C), max(C)

            if Pmax > ans:
                ans = Pmax

        return ans
