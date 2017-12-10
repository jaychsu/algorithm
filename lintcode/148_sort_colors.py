class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        if not nums:
            return

        left, i, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                # temply ignore it
                # it will be swapped if there is `0` later
                i += 1
            else:
                # cannot `i += 1` since the swapped value still need to check
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
