class MinStack:
    """
    @param: a: An integer
    """
    def __init__(self):
        self.stack = []
        self.minstack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.stack.append(number)
        if not self.minstack or number <= self.minstack[-1]:
            self.minstack.append(number)

    """
    @param: a: An integer
    @return: An integer
    """
    def pop(self):
        if not self.stack:
            return
        if self.minstack and self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    """
    @param: a: An integer
    @return: An integer
    """
    def min(self):
        return self.minstack[-1]
