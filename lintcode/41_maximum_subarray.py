"""
Prefix Sum: space optimization
"""
class Solution:
    """
    @param: A: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, A):
        """
        the answer is the maximum segment sum,
        that is, `S[i] - Smin`
        """
        if not A:
            return 0

        ans = float('-inf')
        S = Smin = 0
        for i in range(len(A)):
            S += A[i]

            if S - Smin > ans:
                ans = S - Smin

            """
            since the sum of [i, j] in A is `S[j] - S[i - 1]`
            so we need to find the `Smin` at the end of iteration
            """
            if S < Smin:
                Smin = S

        return ans


"""
Prefix Sum
"""
class Solution:
    """
    @param: A: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, A):
        """
        the answer is the maximum segment sum,
        that is, `S[i] - Smin`
        """
        if not A:
            return 0

        n = len(A)
        ans = float('-inf')

        Smin = 0
        S = [0] * (n + 1)
        for i in range(1, n + 1):
            S[i] = S[i - 1] + A[i - 1]

            if S[i] - Smin > ans:
                ans = S[i] - Smin

            """
            since the sum of [i, j] in A is `S[j] - S[i - 1]`
            so we need to find the `Smin` at the end of iteration
            """
            if S[i] < Smin:
                Smin = S[i]

        return ans
