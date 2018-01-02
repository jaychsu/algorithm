"""
main concept

there is MUST a separator to distinct that two subarrays

`L[i]` means the maxsum before `i + 1`
`R[i]` means the maxsum after `i - 1`

     |<- the separator
A[i] | A[i + 1]

the `ans` is to find the maximum of `L[i] + R[i + 1]`
"""


class Solution:
    """
    @param: A: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, A):
        if not A:
            return 0

        n = len(A)
        L = self.get_max_sum(A, range(n))
        R = self.get_max_sum(A, range(n - 1, -1, -1))

        ans = float('-inf')
        for i in range(n - 1):
            _sum = L[i] + R[i + 1]
            if _sum > ans:
                ans = _sum

        return ans

    def get_max_sum(self, A, scope):
        M = [0] * len(A)
        Smax = float('-inf')
        S = Smin = 0

        for i in scope:
            S += A[i]
            if S - Smin > Smax:
                Smax = S - Smin
            if S < Smin:
                Smin = S
            M[i] = Smax

        return M
