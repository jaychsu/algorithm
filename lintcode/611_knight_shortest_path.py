"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param: grid: a chessboard included 0 (false) and 1 (true)
    @param: source: a point
    @param: destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        ans = -1
        if not grid or not source or not destination:
            return ans

        INFINITY = float('inf')
        vector = (
            (-2, -1),
            (-2,  1),
            (-1, -2),
            (-1,  2),
            ( 1, -2),
            ( 1,  2),
            ( 2, -1),
            ( 2,  1),
        )

        m, n = len(grid), len(grid[0])
        _x = _y = _step = 0

        min_steps = [[INFINITY] * n for _ in range(m)]
        queue = [source]
        min_steps[source.x][source.y] = 0

        for cell in queue:
            for dx, dy in vector:
                _x = cell.x + dx
                _y = cell.y + dy
                _step = min_steps[cell.x][cell.y] + 1
                if 0 <= _x < m and 0 <= _y < n \
                        and not grid[_x][_y] \
                        and _step < min_steps[_x][_y]:
                    min_steps[_x][_y] = _step
                    queue.append(Point(_x, _y))

        if min_steps[destination.x][destination.y] < INFINITY:
            ans = min_steps[destination.x][destination.y]

        return ans
