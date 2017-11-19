class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        ans = 0
        if not grid:
            return ans
        self.m, self.n = len(grid), len(grid[0])
        self.dx, self.dy = [1, -1, 0, 0], [0, 0, 1, -1]
        self.visited = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for x in range(self.m):
            for y in range(self.n):
                # Once found an island, search for the cells around it
                # to mark the around island as visited
                # this ensures the count will not be repeated in later iterations
                if not self.visited[x][y] and grid[x][y] == 1:
                    self.visited[x][y] = 1
                    self.check_around(x, y, grid)
                    ans += 1
        return ans

    # To iterate all the around cell
    def check_around(self, x, y, grid):
        for i in range(4):
            _x, _y = x + self.dx[i], y + self.dy[i]
            if 0 <= _x < self.m and 0 <= _y < self.n \
                    and not self.visited[_x][_y] \
                    and grid[_x][_y] == 1:
                self.visited[_x][_y] = 1

                # Continue to visit the adjacent cell if its an island
                self.check_around(_x, _y, grid)
