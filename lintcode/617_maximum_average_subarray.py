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
    def maxAverage(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: float
        """
        if not nums or not k:
            return 0.0

        EPS = 1e-5

        # ans MUST between `min(nums)` and `max(nums)`
        left = right = nums[0]
        for num in nums:
            if num < left:
                left = num
            if num > right:
                right = num

        # prefix sum
        s = [0] * (len(nums) + 1)
        while right - left > EPS:
            mid = (left + right) / 2.0

            if self.is_valid(nums, k, mid, s):
                left = mid
            else:
                right = mid

        return left

    def is_valid(self, nums, k, mid, s):
        s[0] = smin = 0

        for i in range(1, len(nums) + 1):
            s[i] = s[i - 1] + nums[i - 1] - mid

            if i < k:
                continue

            """
            if there is a non-negative sum subarray of length at least k
            => it's valid even if just only one, return True immediately
            """
            if s[i] >= smin:  # s[i] - smin >= 0
                return True

            if s[i - k + 1] < smin:
                smin = s[i - k + 1]

        return False
