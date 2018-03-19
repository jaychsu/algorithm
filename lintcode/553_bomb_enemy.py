"""
Cache sharing nodes

Main Concept:

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
class Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        ans = 0
        if not grid or not grid[0]:
            return ans

        m, n = len(grid), len(grid[0])
        rs, cs = 0, [0] * n

        for x in range(m):
            for y in range(n):
                if x == 0 or grid[x - 1][y] == self.WALL:
                    cs[y] = 0
                    for i in range(x, m):
                        if grid[i][y] == self.WALL:
                            break
                        if grid[i][y] == self.ENEMY:
                            cs[y] += 1

                if y == 0 or grid[x][y - 1] == self.WALL:
                    rs = 0
                    for i in range(y, n):
                        if grid[x][i] == self.WALL:
                            break
                        if grid[x][i] == self.ENEMY:
                            rs += 1

                if grid[x][y] == self.EMPTY and rs + cs[y] > ans:
                    ans = rs + cs[y]

        return ans


"""
TLE
time: O(m^2 * n^2)
"""
class Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        ans = 0
        if not grid or not grid[0]:
            return ans

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == self.EMPTY:
                    ans = max(
                        ans,
                        self.get_killed_cnt(grid, x, y)
                    )

        return ans

    def get_killed_cnt(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        cnt = 0

        # up
        x, y = i, j
        while x >= 0 and grid[x][y] != self.WALL:
            if grid[x][y] == self.ENEMY:
                cnt += 1
            x -= 1

        # down
        x, y = i, j
        while x < m and grid[x][y] != self.WALL:
            if grid[x][y] == self.ENEMY:
                cnt += 1
            x += 1

        # left
        x, y = i, j
        while y >= 0 and grid[x][y] != self.WALL:
            if grid[x][y] == self.ENEMY:
                cnt += 1
            y -= 1

        # right
        x, y = i, j
        while y < n and grid[x][y] != self.WALL:
            if grid[x][y] == self.ENEMY:
                cnt += 1
            y += 1

        return cnt
