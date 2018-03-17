class Solution:
    def findPeak(self, nums):
        """
        :type nums: list
        :rtype: int
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        return right if nums[left] < nums[right] else left
