class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
