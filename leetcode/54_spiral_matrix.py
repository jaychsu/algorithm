class Solution:
    def spiralOrder(self, G):
        """
        :type G: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not G:
            return ans

        """
        it means go right, bottom, left, top
        """
        dx = ( 0,  1,  0, -1)
        dy = ( 1,  0, -1,  0)

        m, n = len(G), len(G[0])
        x = y = turn = 0

        for _ in range(m * n):
            ans.append(G[x][y])
            G[x][y] = None
            _x = x + dx[turn]
            _y = y + dy[turn]

            if 0 <= _x < m and 0 <= _y < n and G[_x][_y] is not None:
                x = _x
                y = _y
            else:
                turn = (turn + 1) % 4
                x += dx[turn]
                y += dy[turn]

        return ans
