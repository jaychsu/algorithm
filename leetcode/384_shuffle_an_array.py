from random import randrange


class Solution:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.B = A[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.A = self.B
        self.B = self.B[:]
        return self.A

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        A = self.A
        n = len(A)

        for i in range(n):
            _i = randrange(i, n)
            A[i], A[_i] = A[_i], A[i]

        return A


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
