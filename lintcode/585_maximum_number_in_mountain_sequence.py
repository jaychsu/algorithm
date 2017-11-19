class Solution:
    """
    @param: nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        if not nums:
            return -1

        l, m, r = 0, 0, len(nums) - 1

        while l + 1 < r:
            m = l + (r - l) // 2
            """
            `m+1` will not out of range
            if len(nums) == 1 || 2, the code in this loop will not execute
            """
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m

        return max(nums[l], nums[r])
