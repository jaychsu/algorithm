import random


class RandomizedSet:
    def __init__(self):
        self.A = []  # store vals
        self.I = {}  # store index of each val

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        if val in I:
            return False

        A.append(val)
        I[val] = len(A) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        if val not in I:
            return False

        i = I[val]
        _val = A[-1]

        I[_val] = i
        I.pop(val)

        A[i] = _val
        A.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.A)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
