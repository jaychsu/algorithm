class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        if not nums or not target:
            return -1

        l, m, r = 0, 0, len(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m

        """
        considering the edge case: [1, 1, 1, 1]
        we've compared all child above but the both ends
        so we should check the both ends
        """
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        else:
            return -1
