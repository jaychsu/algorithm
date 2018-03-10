from random import randrange


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.origin[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        a = self.nums
        n = len(a)

        for i in range(n):
            _i = randrange(i, n)
            a[i], a[_i] = a[_i], a[i]

        return a


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
