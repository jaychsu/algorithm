class Solution:
    """
    @param: k: An integer
    @param: nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        nums.sort()
        return nums[k-1]
