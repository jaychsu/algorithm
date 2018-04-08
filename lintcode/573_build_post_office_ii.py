"""
Note:
- You cannot pass through wall and house, but can pass through empty.
- You only build post office on an empty.
"""


import collections


class Solution:
    """
    BFS

    1. for each house, use `BFS` in level traversal
       to count the distance if the cell is empty and reachable
    2. find the minimum of the total distance in each empty cell,
       and it must be reachable for each house
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    def shortestDistance(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        cnt = 0
        times = collections.defaultdict(int)
        steps = collections.defaultdict(int)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.HOUSE:
                    cnt += 1
                    self.bfs(grid, x, y, times, steps)

        ans = INF = float('inf')

        for (x, y), t in times.items():
            if t == cnt and steps[x, y] < ans:
                ans = steps[x, y]

        return ans if ans < INF else -1

    def bfs(self, grid, x, y, times, steps):
        m, n = len(grid), len(grid[0])
        queue, _queue = [(x, y)], []
        visited = set(queue)
        step = 0

        while queue:
            step += 1

            for x, y in queue:
                for dx, dy in (
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1),
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

                    steps[_x, _y] += step
                    times[_x, _y] += 1

            queue, _queue = _queue, []


import collections


class Solution:
    """
    DFS: TLE

    If use DFS, need to consider update min dist
    so may visit a node many times
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    def shortestDistance(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        cnt = 0
        ids = collections.defaultdict(set)  # record house ids
        steps = collections.defaultdict(int)  # total steps for all houses

        for x in range(m):
            for y in range(n):
                if grid[x][y] != self.HOUSE:
                    continue

                cnt += 1
                step = collections.defaultdict(int)  # steps for current house
                self.dfs(grid, x, y, cnt, ids, steps, step)

        ans = INF = float('inf')

        for (x, y), hids in ids.items():
            if len(hids) == cnt and steps[x, y] < ans:
                ans = steps[x, y]

        return ans if ans < INF else -1

    def dfs(self, grid, x, y, id, ids, steps, step):
        m, n = len(grid), len(grid[0])

        for dx, dy in (
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
        ):
            _x = x + dx
            _y = y + dy

            if not (0 <= _x < m and 0 <= _y < n):
                continue
            if grid[_x][_y] != self.EMPTY:
                continue
            if step[x, y] + 1 >= step[_x, _y] > 0:  # > 0 means visited, since its defaultdict
                continue

            ids[_x, _y].add(id)

            steps[_x, _y] -= step[_x, _y]
            step[_x, _y] = step[x, y] + 1
            steps[_x, _y] += step[_x, _y]

            self.dfs(grid, _x, _y, id, ids, steps, step)
