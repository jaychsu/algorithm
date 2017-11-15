class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return -1

        l, m, r = 0, 0, len(nums) - 1

        """
        since the children between `nums[0:maximum]`
        are all great than `nums[minimum:-1]`
        so we can pick the last child, and do the binary searching, if:
        1. child in `nums[0:maximum]`,
           then the left boundary will continue to move to the maximum
        2. child in `nums[minimum:-1]`,
           then the right boundary will to the minimum
        """
        last = nums[-1]

        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] > last:
                l = m
            else:
                r = m

        return min(nums[l], nums[r])
