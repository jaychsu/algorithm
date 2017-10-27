class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or len(grid) < 1:
            return 0
        m, n = len(grid), len(grid[0])
        is_visited = [[0 for j in range(n)] for i in range(m)]
        row_vector, col_vector = [1, 0, -1, 0], [0, 1, 0, -1]

        # Return 1 if there is an island and not visited
        def isNotVisit(x, y):
            if 0 <= x < m \
                    and 0 <= y < n \
                    and grid[x][y] == 1 \
                    and is_visited[x][y] == 0:
                return 1
            return 0

        # To iterate all the cell at round(r, b, l, u)
        def dfs(x, y):
            for d in range(4):
                _x, _y = x + row_vector[d], y + col_vector[d]
                if isNotVisit(_x, _y):
                    is_visited[_x][_y] = 1
                    # Continue to visit the adjacent cell if it exists
                    dfs(_x, _y)

        count = 0
        for row in range(m):
            for col in range(n):
                if isNotVisit(row, col):
                    is_visited[row][col] = 1
                    dfs(row, col)
                    # Count += 1 if there is an island
                    # and not visited at function `dfs`(means no adjacent)
                    count += 1
        return count
