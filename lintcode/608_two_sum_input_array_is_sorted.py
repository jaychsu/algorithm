"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if not nums:
            return [-1, -1]

        remaining = {}
        for i in range(len(nums)):
            if nums[i] in remaining:
                return [
                    remaining[nums[i]] + 1,
                    i + 1
                ]
            remaining[target - nums[i]] = i

        return [-1, -1]


"""
time: O(n)
space: O(1)
"""
class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        _sum = 0
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum == target:
                return [
                    left + 1,
                    right + 1
                ]
            if _sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
