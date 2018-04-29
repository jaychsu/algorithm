class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        if not matrix or not matrix[0]:
            return ans

        # need keep its order to go right, bottom, left, top
        delta = (
            (0, 1), (1, 0),
            (0, -1), (-1, 0),
        )
        m, n = len(matrix), len(matrix[0])
        x = y = turn = 0

        for _ in range(m * n):
            ans.append(matrix[x][y])
            matrix[x][y] = None
            _x = x + delta[turn][0]
            _y = y + delta[turn][1]

            if not (0 <= _x < m and 0 <= _y < n) or matrix[_x][_y] is None:
                turn = (turn + 1) % len(delta)
                _x = x + delta[turn][0]
                _y = y + delta[turn][1]

            x = _x
            y = _y

        return ans
