class Solution:
    def totalOccurrence(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int

        given A == [a, b, b, b, c]
                    s        e

        using binary searching to find `s` and `e`
        ans is `e - s`

        * s: start, e: end, l: left, r: right
             [a, b, b, b, c]
        r1  s,l  r
        r2           e,l  r
        """

        if not A:
            return 0

        if A[0] == target or A[-1] == target:
            A = [float('-inf')] + A + [float('inf')]

        n = len(A)
        start = end = 0

        left, mid, right = 0, 0, n - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        start = left

        if start + 1 >= n or A[start + 1] != target:
            return 0

        left, mid, right = 0, 0, n - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        end = left

        return end - start
