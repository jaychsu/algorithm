class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n or n < 1:
            return []
        if n == 1:
            return [[1]]

        ans = [[0] * n for _ in range(n)]
        delta = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0),
        )
        x = y = turn = 0

        for i in range(1, n * n + 1):
            ans[x][y] = i
            _x = x + delta[turn][0]
            _y = y + delta[turn][1]

            if not (0 <= _x < n and 0 <= _y < n) or ans[_x][_y] != 0:
                turn = (turn + 1) % len(delta)
                _x = x + delta[turn][0]
                _y = y + delta[turn][1]

            x = _x
            y = _y

        return ans
