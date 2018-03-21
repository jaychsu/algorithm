"""
Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param = obj.insert(val)
param = obj.remove(val)
param = obj.getRandom()
"""
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.val2idx = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.val2idx[val] = len(self.nums)
        self.nums.append(val)

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2idx:
            return False

        i = self.val2idx[val]
        key = self.nums[-1]

        self.val2idx[key] = i
        self.nums[i] = self.nums[-1]

        self.nums.pop()
        del self.val2idx[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = random.randrange(len(self.nums))
        return self.nums[i]
