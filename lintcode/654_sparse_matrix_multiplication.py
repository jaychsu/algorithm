class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        if not A or not B or len(A[0]) != len(B):
            return []

        m, n = len(A), len(B[0])
        l = len(B)

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for k in range(l):
                    ans[i][j] += A[i][k] * B[k][j]

        return ans
