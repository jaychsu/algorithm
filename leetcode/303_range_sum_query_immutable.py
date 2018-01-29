class NumArray:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        n = len(A)
        self.P = [0] * (n + 1)  # prefix sum

        for i in range(1, n + 1):
            self.P[i] = self.P[i - 1] + A[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.P[j + 1] - self.P[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
