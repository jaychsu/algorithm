class NumMatrix:
    def __init__(self, G):
        """
        :type G: List[List[int]]
        """
        if not G or not G[0]:
            return

        m, n = len(G), len(G[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                self.P[x][y] = (self.P[x - 1][y] +
                                self.P[x][y - 1] -
                                self.P[x - 1][y - 1] +
                                G[x - 1][y - 1])

    def sumRegion(self, x1, y1, x2, y2):
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        if not self.P:
            return -1

        return (self.P[x2 + 1][y2 + 1] -
                self.P[x1][y2 + 1] -
                self.P[x2 + 1][y1] +
                self.P[x1][y1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(x1,y1,x2,y2)
