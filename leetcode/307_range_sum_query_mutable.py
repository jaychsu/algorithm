"""
REF: https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
REF: http://www.cnblogs.com/grandyang/p/4985506.html
"""


class NumArray:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        n = len(A)
        self.B = [0] * (n + 1)  # bits
        self.I = [0] * (n + 1)  # increments

        for i in range(n):
            self.update(i, A[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += 1
        delta = val - self.I[i]
        self.I[i] = val

        while i < len(self.I):
            self.B[i] += delta
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_sum(j + 1) - self.get_sum(i)

    def get_sum(self, i):
        res = 0

        while i > 0:
            res += self.B[i]
            i -= (i & -i)

        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
