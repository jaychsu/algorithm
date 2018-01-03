"""
REF: https://stackoverflow.com/questions/13093602/finding-subarray-with-maximum-sum-number-of-elements#answer-13094527

You can use binary search.

For a searched value `avg`, consider the array `B[i] = A[i] - avg`.
Now find the maximum sum subarray of length at least `k`.

This works because the average of a subarray of length `k` is

`(A[i] + ... + A[i + k - 1]) / k`.

So we have:
`(A[i] + ... + A[i + k - 1]) / k >= avg`
=> `A[i] + ... + A[i + k - 1] >= avg * k`
=> `(A[i] - avg) + ... + (A[i + k - 1] - avg) >= 0`

So, if you binary search for the average, by substracting it from each element,

if you can find a non-negative sum subarray of length at least k,
that is, find the maximum one and check if it's non-negative.

then avg is a valid answer,
continue to search in [avg, max_avg] to see if you can find a better one.
If not, reduce search to [0, avg].

       ans-2c ans-c ans ans+c ans+2c
valid    T      T    T    F     F
"""


class Solution:
    def maxAverage(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: float
        """
        if not A or not k:
            return 0

        EPS = 1e-5

        """
        ans MUST between `min(A)` and `max(A)`
        """
        left = right = A[0]
        for num in A:
            if num < left:
                left = num
            if num > right:
                right = num

        S = [0] * (len(A) + 1)  # prefix sum
        while right - left > EPS:
            mid = (left + right) / 2.0
            if self.is_valid(A, k, mid, S):
                left = mid
            else:
                right = mid

        return left

    def is_valid(self, A, k, mid, S):
        S[0] = 0
        Smin = 0

        for i in range(1, len(A) + 1):
            S[i] = S[i - 1] + A[i - 1] - mid

            if i < k:
                continue

            """
            if there is a non-negative sum subarray of length at least k
            => it's valid even if just only one, return True immediately
            """
            if S[i] >= Smin:  # S[i] - Smin >= 0
                return True

            if S[i - k + 1] < Smin:
                Smin = S[i - k + 1]

        return False
