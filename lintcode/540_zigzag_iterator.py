class ZigzagIterator:
    """
    @param: V: A 1d vector
    @param: W: A 1d vector
    """
    def __init__(self, V, W):
        self.queue = [A for A in (V, W) if A]

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


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(V, W), []
# while solution.hasNext(): result.append(solution.next())
# Output result
