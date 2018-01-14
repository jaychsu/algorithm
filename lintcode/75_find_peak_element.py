class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid

        return right if A[left] < A[right] else left
