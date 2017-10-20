class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        if not nums \
        or len(nums) < 2:
            return 0
        ans = sum = 0
        l, r = 0, len(nums) - 1
        nums.sort()
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            else:
                # since the items from nums[l+1] to nums[r] meet the demands,
                # `r-(l+1)+1 = r-l`, `+1` means including nums[l+1] itself
                ans += r - l
                l += 1
        return ans
