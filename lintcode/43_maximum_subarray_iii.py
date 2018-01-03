"""
http://www.cnblogs.com/sherylwang/p/5635665.html
"""


class Solution:
    """
    @param: A: A list of integers
    @param: k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, A, k):
        if not A or not k or len(A) < k:
            return 0

        _INFINITY = float('-inf')
        n = len(A)

        """
        `G[i][j]` means the global max sum, to pick `j` arrays in [0, i)
        `L[i][j]` means the local max sum, to pick `j` arrays in [0, i),
                  and the `i - 1`th child MUST be included
        """
        G = [[_INFINITY] * (k + 1) for _ in range(n + 1)]
        L = [[_INFINITY] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            L[i][0] = 0
            G[i][0] = 0

        for i in range(1, n + 1):
            end = i
            if k < end:
                end = k
            for j in range(1, end + 1):
                L[i][j] = A[i - 1] + max(L[i - 1][j], G[i - 1][j - 1])
                G[i][j] = max(L[i][j], G[i - 1][j])

        return G[n][k]
