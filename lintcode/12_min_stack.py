class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1

        x = self.stack.pop()

        if self.mins and x == self.mins[-1]:
            self.mins.pop()

        return x

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1

        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        if not self.mins:
            return -1

        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
