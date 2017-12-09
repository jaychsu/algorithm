class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        ans = 0

        if not nums or len(nums) < 2:
            return ans

        nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                # the count of connections from `left` to `right`
                # e.g, from 1 to 4, 1-2, 1-3, 1-4, got 3 connections
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans
