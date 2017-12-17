"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    V = (
        (-2, -1),
        ( 2,  1),
        (-2,  1),
        ( 2, -1),
        (-1, -2),
        ( 1,  2),
        (-1,  2),
        ( 1, -2),
    )

    """
    @param: G: a chessboard included 0 (false) and 1 (true)
    @param: S: a point
    @param: T: a point
    @return: the shortest path
    """
    def shortestPath(self, G, S, T):
        if not G or not S or not T:
            return -1

        INFINITY = float('inf')
        m, n = len(G), len(G[0])
        min_steps = [[INFINITY] * n for _ in range(m)]

        queue = [S]
        _queue = None
        _x = _y = steps = 0

        while queue:
            _queue = []
            steps += 1

            for P in queue:
                for dx, dy in self.V:
                    _x = P.x + dx
                    _y = P.y + dy

                    if (0 <= _x < m and 0 <= _y < n and
                        not G[_x][_y] and
                        steps < min_steps[_x][_y]):

                        if _x == T.x and _y == T.y:
                            return steps

                        min_steps[_x][_y] = steps
                        _queue.append(Point(_x, _y))

            queue = _queue

        return -1
