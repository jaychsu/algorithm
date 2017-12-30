class Solution:
    """
    @param: A: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, A, target):
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right
        return -1
