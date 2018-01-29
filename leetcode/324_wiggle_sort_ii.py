"""
Follow Up: https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing
"""


class Solution:
    def wiggleSort(self, A):
        """
        :type A: List[int]
        :rtype: void Do not return anything, modify A in-place instead.
        """
        if not A:
            return

        n = len(A)
        S = sorted(A)

        for i in range(1, n, 2):
            A[i] = S.pop()

        for i in range(0, n, 2):
            A[i] = S.pop()
