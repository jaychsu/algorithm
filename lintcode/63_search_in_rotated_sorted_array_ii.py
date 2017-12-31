class Solution:
    """
    @param: A: an integer ratated sorted array and duplicates are allowed
    @param: target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        if not A:
            return False

        for i in range(len(A)):
            if A[i] == target:
                return True

        return False
