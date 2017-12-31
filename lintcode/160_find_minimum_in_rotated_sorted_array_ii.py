"""
Iteration
"""
class Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, A):
        if not A:
            return -1

        _min = A[0]
        for i in range(1, len(A)):
            if A[i] < _min:
                _min = A[i]
                break

        return _min


"""
Binary Searching
"""
class Solution:
    """
    @param: A: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, A):
        """
        all chilren before the pivot are great than or equal the child at end
        all chilren after the pivot are less than or equal the child at end
        """
        if not A:
            return -1

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == A[right]:
                # means it's ok to remove the end child
                right -= 1
            elif A[mid] < A[right]:
                # mid at the right side of pivot
                right = mid
            else:
                # mid at the left side of pivot
                left = mid

        return A[left] if A[left] < A[right] else A[right]
