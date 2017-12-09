class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        ans = 0
        if not nums:
            return ans

        nums.sort()

        left, right = 0, len(nums) - 1
        _sum = 0
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum == target:
                ans += 1
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left -= 1
                continue

            if _sum > target:
                right -= 1
            else:
                left += 1

        return ans
