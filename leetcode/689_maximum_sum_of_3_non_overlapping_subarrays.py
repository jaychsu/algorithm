"""
REF: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108231
"""


class Solution:
    def maxSumOfThreeSubarrays(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [-1] * 3
        if not A or len(A) < 3 * k:
            return ans

        n = len(A)
        S = [0] * (n + 1)  # prefix sum
        L = [0] * n  # the starting index of the maximum interval sum with length k in [0, i]
        R = [n - k] * n  # the starting index of the maximum interval sum with length k in [i, n - 1]

        for i in range(1, n + 1):
            S[i] = S[i - 1] + A[i - 1]

        max_sum = S[k] - S[0]  # maximum interval sum
        _sum = 0
        for i in range(k, n):
            L[i] = L[i - 1]
            _sum = S[i + 1] - S[i + 1 - k]
            if _sum > max_sum:
                L[i] = i + 1 - k
                max_sum = _sum

        max_sum = S[n] - S[n - k]
        _sum = 0
        for i in range(n - k - 1, -1, -1):
            R[i] = R[i + 1]
            _sum = S[i + k] - S[i]
            if _sum >= max_sum:
                R[i] = i
                max_sum = _sum

        max_sum = _sum = 0
        for i in range(k, n - 2 * k + 1):
            left = L[i - 1]
            right = R[i + k]
            _sum = S[i + k] - S[i] + S[left + k] - S[left] + S[right + k] - S[right]
            if _sum > max_sum:
                max_sum = _sum
                ans[:] = left, i, right

        return ans
