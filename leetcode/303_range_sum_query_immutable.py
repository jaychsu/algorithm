"""
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
"""


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.ps = [0] * (n + 1)  # prefix sum

        for i in range(1, n + 1):
            self.ps[i] = self.ps[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.ps[j + 1] - self.ps[i]
