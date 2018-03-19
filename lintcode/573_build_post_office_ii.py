"""
Note:
- You cannot pass through wall and house, but can pass through empty.
- You only build post office on an empty.

Main Concept:
1. for each house, use `BFS` in level traversal
   to count the distance if the cell is empty and reachable
2. find the minimum of the total distance in each empty cell,
   and it must be reachable for each house
"""


"""
BFS
"""
import collections


class Solution:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        cnt = 0
        times = collections.defaultdict(int)
        dists = collections.defaultdict(int)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.HOUSE:
                    cnt += 1
                    self.bfs(grid, x, y, times, dists)

        ans = INF = float('inf')

        for (x, y), time in times.items():
            if time == cnt and dists[x, y] < ans:
                ans = dists[x, y]

        return ans if ans < INF else -1

    def bfs(self, grid, x, y, times, dists):
        m, n = len(grid), len(grid[0])
        queue, _queue = [(x, y)], []
        visited = set(queue)
        dist = 0

        while queue:
            dist += 1

            for x, y in queue:
                for dx, dy in (
                    ( 0, -1),
                    ( 0,  1),
                    (-1,  0),
                    ( 1,  0),
                ):
                    _x = x + dx
                    _y = y + dy

                    if not (0 <= _x < m and 0 <= _y < n):
                        continue
                    if grid[_x][_y] != self.EMPTY:
                        continue
                    if (_x, _y) in visited:
                        continue

                    visited.add((_x, _y))
                    _queue.append((_x, _y))

                    times[_x, _y] += 1
                    dists[_x, _y] += dist

            queue, _queue = _queue, []


"""
DFS: TLE

If use DFS, need to consider update min dist
so may visit a node many times
"""
import collections


class Solution:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        cnt = 0
        ids = collections.defaultdict(set)
        dists = collections.defaultdict(int)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.HOUSE:
                    cnt += 1
                    steps = collections.defaultdict(int)
                    self.dfs(grid, x, y, cnt, ids, dists, steps)

        ans = INF = float('inf')

        for (x, y), hids in ids.items():
            if len(hids) == cnt and dists[x, y] < ans:
                ans = dists[x, y]

        return ans if ans < INF else -1

    def dfs(self, grid, x, y, id, ids, dists, steps):
        m, n = len(grid), len(grid[0])

        for dx, dy in (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        ):
            _x = x + dx
            _y = y + dy

            if not (0 <= _x < m and 0 <= _y < n):
                continue
            if grid[_x][_y] != self.EMPTY:
                continue
            if steps[x, y] + 1 >= steps[_x, _y] > 0:
                continue

            ids[_x, _y].add(id)

            dists[_x, _y] -= steps[_x, _y]
            steps[_x, _y] = steps[x, y] + 1
            dists[_x, _y] += steps[_x, _y]

            self.dfs(grid, _x, _y, id, ids, dists, steps)
