class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, A):
        n = len(A)
        left, right = 0, n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if mid > 0 and A[mid] == A[mid - 1]:
                if mid & 1:
                    left = mid
                else:
                    right = mid
            else:
                if mid & 1:
                    right = mid
                else:
                    left = mid

        for mid in (left, right):
            if mid > 0 and A[mid] == A[mid - 1]:
                continue
            if mid + 1 < n and A[mid] == A[mid + 1]:
                continue
            return A[mid]

        return -1
