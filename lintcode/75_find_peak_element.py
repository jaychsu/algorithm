class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        if not A:
            return
        l, m, r = 1, 1, len(A) - 1

        while l + 1 < r:
            m = l + (r - l) // 2
            if A[m] < A[m-1]:
                r = m
            else:
                l = m

        return l if A[l] > A[r] else r
