"""
Main Concept:

1. from end to start, finding first decreasing element,
   which is `A[i]`
2. from end to start, finding first element just larger than `A[i]`,
   which is `A[j]`.
   and swap `A[i]` and `A[j]`.
3. reverse the elements between `A[i + 1]` and `A[n - 1]`

REF: [Next Permutation](https://leetcode.com/articles/next-permutation/)
"""


class Solution:
    def nextPermutation(self, A):
        """
        :type A: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not A or len(A) < 2:
            return

        n = len(A)
        i = n - 2

        while i >= 0 and A[i] >= A[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0 and A[i] >= A[j]:
                j -= 1
            A[i], A[j] = A[j], A[i]

        i = i + 1
        j = n - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
