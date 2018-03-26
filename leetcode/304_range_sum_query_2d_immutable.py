"""
Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(x1, y1, x2, y2)
"""


class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        self.ps = [[0] * (n + 1) for _ in range(m + 1)]

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                self.ps[x][y] = sum((
                    self.ps[x - 1][y],
                    self.ps[x][y - 1],
                    - self.ps[x - 1][y - 1],
                    matrix[x - 1][y - 1],
                ))

    def sumRegion(self, x1, y1, x2, y2):
        """
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: int
        """
        if not all((
            self.ps,
            self.ps[0],
            (0 <= x1 < len(self.ps)),
            (0 <= x2 + 1 < len(self.ps)),
            (0 <= y1 < len(self.ps[0])),
            (0 <= y2 + 1 < len(self.ps[0])),
        )):
            return 0

        return sum((
            self.ps[x2 + 1][y2 + 1],
            - self.ps[x1][y2 + 1],
            - self.ps[x2 + 1][y1],
            self.ps[x1][y1],
        ))
