class Solution:
    """
    @param: A: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, A):
        if not A:
            return 0

        n = len(A)
        B = [-1 * num for num in A]
        Lmin = self.get_sum(B, range(n), factor=-1)
        Lmax = self.get_sum(A, range(n), factor=1)
        Rmin = self.get_sum(B, range(n - 1, -1, -1), factor=-1)
        Rmax = self.get_sum(A, range(n - 1, -1, -1), factor=1)

        ans = float('-inf')
        for i in range(n - 1):
            ans = max(
                ans,
                Lmax[i] - Rmin[i + 1],
                Rmax[i + 1] - Lmin[i]
            )

        return ans

    def get_sum(self, A, scope, factor):
        """
        factor ==  1: max sum
        factor == -1: min sum
        """

        M = [0] * len(A)
        Smax = float('-inf')
        S = Smin = 0

        for i in scope:
            S += A[i]
            if S - Smin > Smax:
                Smax = S - Smin
            if S < Smin:
                Smin = S
            M[i] = Smax * factor

        return M
