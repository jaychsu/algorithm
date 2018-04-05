class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        if not nums or len(nums) < 2:
            return nums

        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while i < j and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        i = i + 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
