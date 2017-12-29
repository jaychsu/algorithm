"""
DFS
"""
class Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, G):
        NOT_FOUND = -1
        if not G or not G[0] or G[0][0] == 1:
            return NOT_FOUND

        V = (
            (-1,  2),
            ( 1,  2),
            (-2,  1),
            ( 2,  1),
        )
        m, n = len(G), len(G[0])

        queue = [(0, 0)]
        turns = {(0, 0): 0}
        for x, y in queue:
            for dx, dy in V:
                _x = x + dx
                _y = y + dy
                if 0 <= _x < m and 0 <= _y < n and G[_x][_y] == 0:
                    if (_x, _y) in turns:
                        continue

                    turns[_x, _y] = turns[x, y] + 1

                    if _x == m - 1 and _y == n - 1:
                        return turns[_x, _y]

                    queue.append((_x, _y))

        return NOT_FOUND


"""
DP
"""
class Solution:
    """
    @param: G: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, G):
        if not G or not G[0] or G[0][0] == 1:
            return -1

        INFINITY = float('inf')

        m, n = len(G), len(G[0])
        dp = [[INFINITY] * 3 for _ in range(m)]
        pre2 = pre1 = curr = 0
        dp[0][curr] = 0

        """
        x and y is changed since its need from left to right
        """
        for y in range(1, n):
            pre2, pre1 = pre1, curr
            curr = y % 3
            for x in range(m):
                dp[x][curr] = INFINITY

                if G[x][y] == 1:
                    continue

                if (x >= 2 and y >= 1 and dp[x - 2][pre1] < INFINITY and
                    dp[x - 2][pre1] + 1 < dp[x][curr]):
                    dp[x][curr] = dp[x - 2][pre1] + 1

                if (x >= 1 and y >= 2 and dp[x - 1][pre2] < INFINITY and
                    dp[x - 1][pre2] + 1 < dp[x][curr]):
                    dp[x][curr] = dp[x - 1][pre2] + 1

                if (x + 1 < m and y >= 2 and dp[x + 1][pre2] < INFINITY and
                    dp[x + 1][pre2] + 1 < dp[x][curr]):
                    dp[x][curr] = dp[x + 1][pre2] + 1

                if (x + 2 < m and y >= 1 and dp[x + 2][pre1] < INFINITY and
                    dp[x + 2][pre1] + 1 < dp[x][curr]):
                    dp[x][curr] = dp[x + 2][pre1] + 1

        return dp[m - 1][curr] if dp[m - 1][curr] < INFINITY else -1
