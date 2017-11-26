class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if x == 0 and y > 0:
                    grid[x][y] += grid[x][y - 1]
                elif x > 0 and y == 0:
                    grid[x][y] += grid[x - 1][y]
                elif x > 0 and y > 0:
                    grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])

        return grid[m - 1][n - 1]
