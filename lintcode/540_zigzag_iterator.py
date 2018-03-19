"""
Your ZigzagIterator object will be instantiated and called as such:
solution, result = ZigzagIterator(v1, v2), []
while solution.hasNext(): result.append(solution.next())
Output result
"""


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.g = (v1, v2)
        self.x = 0
        self.y = 0
        self.max_y = max(len(vec) for vec in self.g)

    """
    @return: An integer
    """
    def next(self):
        if not self.hasNext():
            return -1

        x = self.x
        y = self.y

        self.x += 1

        return self.g[x][y]

    """
    @return: True if has next
    """
    def hasNext(self):
        while self.y < self.max_y:
            if (
                self.x < len(self.g) and
                self.y < len(self.g[self.x])
            ):
                return True

            if self.x >= len(self.g):
                self.x = 0
                self.y += 1

            if self.y >= len(self.g[self.x]):
                self.x += 1

        return False


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.queue = [vec for vec in (v1, v2) if vec]

    """
    @return: An integer
    """
    def next(self):
        if not self.hasNext():
            return -1

        vec = self.queue.pop(0)
        val = vec.pop(0)

        if vec:
            self.queue.append(vec)

        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        return bool(self.queue)
