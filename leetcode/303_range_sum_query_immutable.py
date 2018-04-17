"""
Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(i,j)
"""


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return

        n = len(nums)
        self.prefix_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (
            not self.prefix_sum or
            i < 0 or
            j + 1 >= len(self.prefix_sum)
        ):
            return 0
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
