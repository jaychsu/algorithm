"""
Binary Searching
"""
class Solution:
    def longestIncreasingSubsequence(self, A):
        """
        :type A: List[int]
        :rtype: int

        the iteration of B:
        [-inf, 0, inf, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 8, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 4, inf, inf, inf, inf, inf, inf]
        [-inf, 0, 4, 12, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 12, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 10, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 6, inf, inf, inf, inf, inf]
        [-inf, 0, 2, 6, 14, inf, inf, inf, inf]

        lis_size = 4
        """
        if not A:
            return 0

        INFINITY = float('inf')
        _INFINITY = float('-inf')
        n = len(A)
        B = [_INFINITY] + [INFINITY] * n

        for i in range(n):
            b = self.binary_search(B, A[i])
            B[b] = A[i]
            # print(B)

        for i in range(n, -1, -1):
            if B[i] < INFINITY:
                return i

        return 0

    def binary_search(self, B, num):
        left, right = 0, len(B) - 1
        mid = None
        while left + 1 < right:
            mid = left + (right - left) // 2
            if B[mid] < num:
                left = mid
            else:
                right = mid
        return right


"""
DP + Print Paths
"""
class Solution:
    def longestIncreasingSubsequence(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lis_size = 0
        if not A:
            return lis_size

        n = len(A)

        """
        `dp[i]` means the maximum size of LIS end at `i`
        note that there is size, so init with `1`
        """
        dp = [1] * n
        # pi = [0] * n
        # end_at = -1

        for i in range(n):
            for j in range(i):
                """
                `dp[j]` the existing subseq end at `j`
                `+ 1` means included `A[i]`
                """
                if A[j] < A[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    # pi[i] = j

                if dp[i] > lis_size:
                    lis_size = dp[i]
                    # end_at = i

        # paths = [0] * lis_size
        # for i in range(lis_size - 1, -1, -1):
        #     paths[i] = A[end_at]
        #     end_at = pi[end_at]
        # print(paths)

        return lis_size
