class ZigzagIterator2:
    """
    @param: V: a list of 1d vectors
    """
    def __init__(self, V):
        self.queue = [A for A in V if A]

    """
    @return: An integer
    """
    def next(self):
        A = self.queue.pop(0)
        val = A.pop(0)
        if A:
            self.queue.append(A)
        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        return self.queue


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(V), []
# while solution.hasNext(): result.append(solution.next())
# Output result
