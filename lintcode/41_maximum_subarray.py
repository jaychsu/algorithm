class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if not nums:
            return 0

        max_sum, min_sum, prefix_sum = float('-inf'), 0, 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
