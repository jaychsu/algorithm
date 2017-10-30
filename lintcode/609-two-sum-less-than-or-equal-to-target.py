class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        ans = sum = 0
        l, r = 0, len(nums) - 1
        nums.sort()
        while l < r:
            sum = nums[l] + nums[r]
            if sum <= target:
                # the count of connections from `l` to `r`
                # e.g, from 1 to 4, 1-2, 1-3, 1-4, got 3 connections
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans
