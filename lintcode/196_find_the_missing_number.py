class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    def findMissing(self, A):
        if not A:
            return 0

        A.sort()
        i = 0

        for j in range(len(A)):
            if i != A[j]:
                return i
            i += 1

        return i
