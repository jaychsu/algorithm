class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        NOT_FOUND = -1

        if not nums:
            return NOT_FOUND

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[0]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid

        for mid in (left, right):
            if nums[mid] == target:
                return mid

        return NOT_FOUND
