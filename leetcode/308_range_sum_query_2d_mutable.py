class NumMatrix:
    def __init__(self, G):
        """
        :type G: List[List[int]]
        """
        if not G or not G[0]:
            return

        m, n = len(G), len(G[0])
        self.B = [[0] * (n + 1) for _ in range(m + 1)]
        self.I = [[0] * (n + 1) for _ in range(m + 1)]

        for x in range(m):
            for y in range(n):
                self.update(x, y, G[x][y])

    def update(self, x, y, val):
        """
        :type x: int
        :type y: int
        :type val: int
        :rtype: void
        """
        x += 1
        y += 1
        delta = val - self.I[x][y]
        self.I[x][y] = val

        _m, _n = len(self.I), len(self.I[0])

        while x < _m:
            i = y
            while i < _n:
                self.B[x][i] += delta
                i += (i & -i)
            x += (x & -x)

    def sumRegion(self, x1, y1, x2, y2):
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        return (self.sum(x2 + 1, y2 + 1) -
                self.sum(x2 + 1, y1) -
                self.sum(x1, y2 + 1) +
                self.sum(x1, y1))

    def sum(self, x, y):
        res = 0

        while x > 0:
            i = y
            while i > 0:
                res += self.B[x][i]
                i -= (i & -i)
            x -= (x & -x)

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(x,y,val)
# param_1 = obj.sumRegion(x1,y1,x2,y2)
