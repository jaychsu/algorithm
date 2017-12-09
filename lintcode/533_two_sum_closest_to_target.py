class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        if not nums or len(nums) < 2:
            return -1

        nums.sort()

        left, right = 0, len(nums) - 1
        _sum = 0
        diff = float('inf')
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum < target:
                diff = min(diff, target - _sum)
                left += 1
            else:
                diff = min(diff, _sum - target)
                right -= 1

        return diff
