class Solution:
    """
    @param: A: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, A, k):
        if not A:
            return 0

        left, right = 0, len(A) - 1

        while left <= right:
            while left <= right and A[left] < k:
                left += 1
            while left <= right and A[right] >= k:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return left
