class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0

        if not grid or not grid[0]:
            return ans

        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    self.dfs(grid, x, y)
                    ans += 1

        return ans

    def dfs(self, grid, x, y):
        grid[x][y] = '0'

        for dx, dy in (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        ):
            _x = x + dx
            _y = y + dy

            if not (
                0 <= _x < len(grid) and
                0 <= _y < len(grid[0]) and
                grid[_x][_y] == '1'
            ):
                continue

            self.dfs(grid, _x, _y)
