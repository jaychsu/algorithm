"""
Heap
"""
import heapq


class Solution:
    def findMedianSortedArrays(self, a, b):
        """
        :type a: list
        :type b: list
        :rtype: float
        """
        heap = []
        n = 0

        for nums in (a, b):
            if not nums:
                continue

            n += len(nums)
            heapq.heappush(heap, (nums[0], nums, 0))

        if n == 0:
            return 0.0

        num = 0
        for _ in range((n + 1) // 2):
            num, nums, i = heapq.heappop(heap)

            i += 1
            if i < len(nums):
                heapq.heappush(heap, (nums[i], nums, i))

        if n & 1 == 1:
            return num * 1.0

        _num = heapq.heappop(heap)[0]
        return (num + _num) / 2.0


"""
Decreasing Approaching
"""
class Solution:
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

    def find_kth(self, A, i, B, j, k):
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
        if i >= len(A):
            return B[j + k - 1]
        if j >= len(B):
            return A[i + k - 1]
        if k == 1:
            return min(A[i], B[j])

        _a = i + k // 2 - 1
        _b = j + k // 2 - 1
        a = A[_a] if _a < len(A) else float('inf')
        b = B[_b] if _b < len(B) else float('inf')

        if a < b:
            return self.find_kth(A, i + k // 2, B, j, k - k // 2)
        else:
            return self.find_kth(A, i, B, j + k // 2, k - k // 2)
