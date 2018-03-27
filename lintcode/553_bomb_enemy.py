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

    def maxKilledEnemies(self, grid):
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        ans = 0
        if not grid or not grid[0]:
            return ans

        m, n = len(grid), len(grid[0])
        row, cols = 0, [0] * n

        for x in range(m):
            for y in range(n):
                # calculate bomb in cur section [x, 'WALL' | m) in col
                if x == 0 or grid[x - 1][y] == self.WALL:
                    cols[y] = 0

                    for i in range(x, m):
                        if grid[i][y] == self.WALL:
                            break
                        if grid[i][y] == self.ENEMY:
                            cols[y] += 1

                # calculate bomb in cur section [y, 'WALL' | n) in row
                if y == 0 or grid[x][y - 1] == self.WALL:
                    row = 0

                    for i in range(y, n):
                        if grid[x][i] == self.WALL:
                            break
                        if grid[x][i] == self.ENEMY:
                            row += 1

                if grid[x][y] == self.EMPTY and row + cols[y] > ans:
                    ans = row + cols[y]

        return ans


"""
TLE
time: O(m^2 * n^2)
"""
class Solution:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

    def maxKilledEnemies(self, grid):
        """
        :type grid: list[list[str]]
        :rtype: int
        """
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
        for x in range(i, -1, -1):
            if grid[x][j] == self.WALL:
                break
            if grid[x][j] == self.ENEMY:
                cnt += 1

        # down
        for x in range(i, m):
            if grid[x][j] == self.WALL:
                break
            if grid[x][j] == self.ENEMY:
                cnt += 1

        # left
        for y in range(j, -1, -1):
            if grid[i][y] == self.WALL:
                break
            if grid[i][y] == self.ENEMY:
                cnt += 1

        # right
        for y in range(j, n):
            if grid[i][y] == self.WALL:
                break
            if grid[i][y] == self.ENEMY:
                cnt += 1

        return cnt
