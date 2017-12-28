class Solution:
    """
    @param: A: an integer array
    @return:
    """
    def moveZeroes(self, A):
        if not A:
            return

        n = len(A)
        left = right = 0

        while right < n:
            if A[right] != 0:
                A[left], A[right] = A[right], A[left]
                left += 1
            right += 1
