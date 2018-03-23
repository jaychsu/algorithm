"""
REF: https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
REF: http://www.cnblogs.com/grandyang/p/4985506.html

Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
obj.update(i,val)
param_2 = obj.sumRange(i,j)
"""


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.bits = [0] * (n + 1)  # bits
        self.incr = [0] * (n + 1)  # increments

        for i in range(n):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void

        It must increase `i` here, since this api is public,
        so look from outside, the `i` is just the index of `nums`
        """
        i += 1
        delta = val - self.incr[i]
        self.incr[i] = val

        while i < len(self.incr):
            self.bits[i] += delta
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j + 1) - self.sum(i)

    def sum(self, i):
        res = 0

        while i > 0:
            res += self.bits[i]
            i -= (i & -i)

        return res
