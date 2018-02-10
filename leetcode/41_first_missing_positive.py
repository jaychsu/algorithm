"""
REF: http://www.cnblogs.com/yuzhangcmu/p/4200096.html
"""


class Solution:
    def firstMissingPositive(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1

        while left <= right:
            """
            for `A[left]`, the index it should be at is `A[left] - 1`
            1. if it is already at `i` => pass
            2. if it out of range or duplicated => let `A[right]` in
            3. if it is legal => swap to let `A[left]` go to `i`
            """
            i = A[left] - 1
            if i == left:
                left += 1
            elif i < 0 or i > right or A[i] == A[left]:
                A[left], A[right] = A[right], A[left]
                # `A[left] = A[right]` is also ok, since no need to visit `A[right]` again
                right -= 1
            else:
                A[left], A[i] = A[i], A[left]

        return left + 1
