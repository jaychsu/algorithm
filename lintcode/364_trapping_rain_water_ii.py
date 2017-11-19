from heapq import heappush, heappop

class Solution:
    """
    @param: heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0
        m, n = len(heights), len(heights[0])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        ans = bound = x = y = i = 0
        bounds = []
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # Put the cells on the matrix boundaries into `bounds`
        for i in range(m):
            heappush(bounds, (heights[i][0], i, 0))
            visited[i][0] = 1
            heappush(bounds, (heights[i][n - 1], i, n - 1))
            visited[i][n - 1] = 1
        for i in range(1, n - 1):
            heappush(bounds, (heights[0][i], 0, i))
            visited[0][i] = 1
            heappush(bounds, (heights[m - 1][i], m - 1, i))
            visited[m - 1][i] = 1

        while bounds:
            # Find the min bound of any current boundary
            bound, x, y = heappop(bounds)
            # To keep the water in, keep finding the boundary
            for i in range(4):
                _x = x + dx[i]
                _y = y + dy[i]
                if 0 <= _x < m and 0 <= _y < n and not visited[_x][_y]:
                    visited[_x][_y] = 1
                    # Choosing the boundary of current cell
                    # if its lower than the bound outside
                    # than this cell will store water
                    # otherwise this cell will become the new boundary
                    _bound = max(bound, heights[_x][_y])
                    heappush(bounds, (_bound, _x, _y))
                    if _bound > heights[_x][_y]:
                        ans += _bound - heights[_x][_y]
        return ans
