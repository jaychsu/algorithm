class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """
    """
    since the fact:
        the minimum negative number * -1 -> the maximum
        the maximum positive number -> the maximum
    so we need record the minimum and the maximum number for each child in nums
    """
    def maxProduct(self, nums):
        if not nums:
            return 0

        ans = min_p = max_p = nums[0]
        for i in range(1, len(nums)):
            min_p, max_p = \
                min(nums[i], min_p * nums[i], max_p * nums[i]), \
                max(nums[i], min_p * nums[i], max_p * nums[i])
            ans = max(ans, max_p)
        return ans
