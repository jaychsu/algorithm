"""
REF: https://leetcode.com/problems/game-of-life/discuss/73223
"""


class Solution:
    def gameOfLife(self, G):
        """
        :type G: List[List[int]]
        :rtype: void Do not return anything, modify G in-place instead.
        """
        if not G or not G[0]:
            return

        V = (
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1), ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        )
        m, n = len(G), len(G[0])

        for x in range(m):
            for y in range(n):
                lives = self.get_live_neibs(G, x, y, V)

                if G[x][y] == 1 and 2 <= lives <= 3:
                    G[x][y] = 3

                if G[x][y] == 0 and lives == 3:
                    G[x][y] = 2

        for x in range(m):
            for y in range(n):
                G[x][y] >>= 1

    def get_live_neibs(self, G, x, y, V):
        cnt = 0
        m, n = len(G), len(G[0])

        for dx, dy in V:
            _x = x + dx
            _y = y + dy
            if not (0 <= _x < m and 0 <= _y < n):
                continue
            cnt += G[_x][_y] & 1

        return cnt
