class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        NOT_FOUND = [-1, -1]

        if not A:
            return NOT_FOUND

        n = len(A)

        left, mid, right = 0, 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        start = left if A[left] == target else right

        left, mid, right = 0, 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        end = right if A[right] == target else left

        if start <= end:
            return [start, end]

        return NOT_FOUND
