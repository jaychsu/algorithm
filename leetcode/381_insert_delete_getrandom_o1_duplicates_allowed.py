import random


class RandomizedCollection:
    def __init__(self):
        self.A = []
        self.I = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        if val not in I:
            I[val] = set()

        A.append(val)
        I[val].add(len(A) - 1)
        return len(I[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        A, I = self.A, self.I
        if val not in I or not I[val]:
            return False

        i = I[val].pop()
        _val = A[-1]

        I[_val].add(i)
        I[_val].discard(len(A) - 1)

        A[i] = _val
        A.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.A)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
