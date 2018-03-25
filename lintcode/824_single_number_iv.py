class Solution:
    def getSingleNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        if not nums:
            return -1

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        left, right = 0, n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid & 1 == 1:
                    left = mid
                else:
                    right = mid
            else:
                if mid & 1 == 1:
                    right = mid
                else:
                    left = mid

        for mid in (left, right):
            if mid > 0 and nums[mid] == nums[mid - 1]:
                continue
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                continue
            return nums[mid]

        return -1
