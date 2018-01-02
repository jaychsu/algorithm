class Solution:
    """
    @param: A: An array of integers
    @return: nothing
    """
    def nextPermutation(self, A):
        if not A or len(A) < 2:
            return A

        n = len(A)
        i = n - 2
        while i >= 0 and A[i] >= A[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0 and A[i] >= A[j]:
                j -= 1
            A[i], A[j] = A[j], A[i]

        i = i + 1
        j = n - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

        return A
