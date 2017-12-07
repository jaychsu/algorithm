class Solution:
    INFINITY = float('inf')

    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)

        median = self.find_kth(A, 0, B, 0, n // 2 + 1)
        if n % 2 == 1:
            return median

        _median = self.find_kth(A, 0, B, 0, n // 2)
        return (median + _median) / 2.0

    def find_kth(self, A, A_start, B, B_start, k):
        """
        example: A: [1, 2, 3, 4, 5, 6]
                 B: [2, 3, 4, 5]

        m + n = 10, median is `(5th + 6th) / 2`
        the process below is to find the `6th`
        r1/ k = 6
            1  2 |3| 4  5  6
            2  3 |4| 5
            _a = _b = 2
            a = 3, b = 4
            a < b
        r2/ k = 3
           -1--2--3-|4| 5  6
           |2| 3  4  5
            _a = 3, _b = 0
            a = 4, b = 2
            a > b
        r3/ k = 2
           -1--2--3-|4| 5  6
           -2-|3| 4  5
            _a = 3, _b = 1
            a = 4, b = 3
            a > b
        r4/ k = 1
           -1--2--3-|4| 5  6
           -2--3-|4| 5
            since k == 1
            return min(4, 4) = `4`
        """
        if A_start >= len(A):
            return B[B_start + k - 1]
        if B_start >= len(B):
            return A[A_start + k - 1]
        if k == 1:
            return min(A[A_start], B[B_start])

        _a = A_start + k // 2 - 1
        _b = B_start + k // 2 - 1
        a = A[_a] if _a < len(A) else self.INFINITY
        b = B[_b] if _b < len(B) else self.INFINITY

        if a < b:
            return self.find_kth(A, A_start + k // 2, B, B_start, k - k // 2)
        else:
            return self.find_kth(A, A_start, B, B_start + k // 2, k - k // 2)
