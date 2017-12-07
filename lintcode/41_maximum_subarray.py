class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if not nums:
            return 0

        max_sum, sum = float('-inf'), 0
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = max(max_sum, sum)
            sum = max(sum, 0)

        return max_sum
