"""
REF: https://stackoverflow.com/questions/13093602/finding-subarray-with-maximum-sum-number-of-elements#answer-13094527

You can use binary search.

For a searched value `x`, consider the array `b[i] = a[i] - x`.
Now find the maximum sum subarray of length at least `k`.

This works because the average of a subarray of length `k` is

`(a[p] + ... + a[p + k - 1]) / k`.

So we have:
`(a[p] + ... + a[p + k - 1]) / k >= avg`
=> `a[p] + ... + a[p + k - 1] >= avg * k`
=> `(a[p] - avg) + ... + (a[p + k - 1] - avg) >= 0`

So, if you binary search for the average, by substracting it from each element,
if you can find a positive-sum subarray (find the maximum one and check if it's positive) of length at least k,
then avg is a valid answer,
continue to search in [avg, max_avg] to see if you can find a better one.
If not, reduce search to [0, avg].
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

        """
        ans MUST between `min(A)` and `max(A)`
        """
        left, right = float('inf'), float('-inf')
        for num in A:
            if num < left:
                left = num
            if num > right:
                right = num

        """
        eps is 1e-5

              ans-2c ans-1c ans ans+1c ans+2c
        valid    T      T    T     F      F
        """
        S = [0] * (len(A) + 1)  # prefix sum
        while right - left >= 1e-5:
            mid = left + (right - left) / 2.0
            if self.is_valid(A, S, mid, k):
                left = mid
            else:
                right = mid

        return left

    def is_valid(self, A, S, mid, k):
        S[0] = 0
        min_s = 0  # minimum prefix sum

        for i in range(1, len(A) + 1):
            S[i] = S[i - 1] + A[i - 1] - mid

            if i < k:
                continue
            """
            if there is a positive-sum subarray of length at least k
            => it's valid
            """
            if S[i] >= min_s:  # S[i] - min_s >= 0
                return True
            if S[i - k + 1] < min_s:
                min_s = S[i - k + 1]

        return False
