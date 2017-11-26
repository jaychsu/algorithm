class Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    """
    @param: grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        """
        1. the number of enemies killed is same between the two walls in line

                y
                0 1 2 3 4
            x 0   W
              1 k 0 k W l
              2   n
              3   W
              4   m

            the number of enemies killed is `n + k` at (1, 1)

        2. since the iteration order, we can optimize
           the space complexity in row

            x  y   0    1    2    3
            0 [[ | 0, | E, | 0, | 0 ],  --1-->
            1  [ | E, | 0, v W, | E ],  --2-->
            2  [ v 0, v E, v 0, v 0 ]]  --3-->
        """
        ans = 0
        # killed_location = None
        if not grid:
            return ans

        m, n = len(grid), len(grid[0])
        rows, cols = 0, [0] * n

        for x in range(m):
            for y in range(n):
                if x == 0 or grid[x - 1][y] == self.WALL:
                    cols[y] = 0
                    for i in range(x, m):
                        if grid[i][y] == self.WALL:
                            break
                        if grid[i][y] == self.ENEMY:
                            cols[y] += 1
                if y == 0 or grid[x][y - 1] == self.WALL:
                    rows = 0
                    for i in range(y, n):
                        if grid[x][i] == self.WALL:
                            break
                        if grid[x][i] == self.ENEMY:
                            rows += 1
                if grid[x][y] == self.EMPTY and ans < rows + cols[y]:
                    ans = rows + cols[y]
                    # killed_location = (x, y)

        # print(killed_location)

        return ans
