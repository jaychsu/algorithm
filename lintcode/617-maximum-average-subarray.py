"""
REF: https://leetcode.com/articles/maximum-average-subarray-ii/#approach-2-using-binary-search-accepted

Assuming the answer we want is
dividing the cumulative sum from `A[i]` to `A[j-1]` by `j - i`
where `j - i >= k`,
and there is a `mid`, that is max avg., between `M = max(A)` and `m = min(A)`

1. Assumption
so that, `(A[i] + A[i+1] + ... + A[j-1]) / (j - i) >= mid`
=> `A[i] + A[i+1] + ... + A[j-1] >= mid * (j - i)`
=> let `S = (A[i] - mid) + ... + (A[j-1] - mid) >= 0`

Let `P[i] = (A[0] - mid) + ... + (A[i-1] - mid)
          = P[i-1] + A[i-1] - mid`

So, `S = P[j] - P[i] >= 0`
=> For each `A[i-1]` in `P[i]`, satisfies `j - (i-1) >= k`
=> `i <= j - k + 1`
=> `S = P[j] - P[j-k+1] >= 0`
=> `P[j] >= P[j-k+1]`

2. Approaching the `mid` by Binary Search
=> 1st round, mid = (M + m) / 2

after 1st round:
if we find a `P[j]` that satisfies `P[j] - P[j-k+1] >= 0`,
we can achieve an average value greater than `mid`.
thus, in this case, we need to set the `mid` as the new minimum element and continue the approaching

otherwise, if `P[j] - P[j-k+1] < 0` always truthy, we can't achieve `mid` as the average.
thus, we need to set `mid` as the new maximum element and continue the process.
"""

class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if not nums or not k:
            return 0
        l, r, n = min(nums), max(nums), len(nums)
        P = [0] * (n + 1)
        m = min_sum = is_check = 0

        # eps is 1e-5
        while r - l >= 1e-5:
            min_sum = is_check = 0
            m = l + (r - l) / 2.0
            for i in range(1, n + 1):
                P[i] = P[i - 1] + nums[i - 1] - m
                if i < k:
                    continue

                # if we find a `P[j]` that satisfies `P[j] - P[j-k+1] >= 0`
                if P[i] >= min_sum:
                    is_check = 1
                    break
                min_sum = min(min_sum, P[i - k + 1])
            if is_check:
                l = m
            else:
                r = m
        return l
