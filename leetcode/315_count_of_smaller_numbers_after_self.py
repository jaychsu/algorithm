"""
REF: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/
"""


class BinaryIndexedTree:
    def __init__(self, n):
        self.B = [0] * (n + 1)

    def update(self, i):
        while i < len(self.B):
            self.B[i] += 1
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.B[i]
            i -= i & -i
        return res


class Solution:
    def countSmaller(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        if not A:
            return ans

        I = {v: i for i, v in enumerate(sorted(set(A)))}
        tree = BinaryIndexedTree(len(I))

        for i in range(len(A) - 1, -1, -1):
            ans.append(tree.sum(I[A[i]]))
            tree.update(I[A[i]] + 1)

        return ans[::-1]
