class Solution:
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2

    """
    @param: grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid:
            return -1

        vector = (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        )
        m, n = len(grid), len(grid[0])

        queue, _queue = [], None
        days = -1
        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.ZOMBIE:
                    queue.append((x, y))

        while queue:
            days += 1
            _queue = []
            for x, y in queue:
                for dx, dy in vector:
                    _x = x + dx
                    _y = y + dy
                    if 0 <= _x < m and 0 <= _y < n \
                            and grid[_x][_y] == self.PEOPLE:
                        grid[_x][_y] = self.ZOMBIE
                        _queue.append((_x, _y))
            queue = _queue

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.PEOPLE:
                    return -1

        return days
