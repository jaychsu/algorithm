class Solution:

    def kthLargestElement(self, k, nums):
        nums.sort()
        return nums[-k]
