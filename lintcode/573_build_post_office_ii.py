"""
Test Case:

[[0,1,0,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]

[[0,1,0,0],
 [1,0,2,1],
 [0,1,0,0]]
: self.visited_time[_x][_y] < count -> and not visited[_x][_y]:


- You cannot pass through wall and house, but can pass through empty.
- You only build post office on an empty.


1. for each house, use `BFS` in level traversal
   to count the distance if the cell is empty and reachable
2. find the minimum of the total distance in each empty cell,
   and it must be reachable for each house
"""


class Solution:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    V = (
        ( 0, -1),
        ( 0,  1),
        (-1,  0),
        ( 1,  0),
    )

    """
    @param: G: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, G):
        if not G or not G[0]:
            return -1

        m, n = len(G), len(G[0])
        houses = []
        for x in range(m):
            for y in range(n):
                if G[x][y] == self.HOUSE:
                    houses.append((x, y))

        C = [[0] * n for _ in range(m)]  # C: visited count
        D = [[0] * n for _ in range(m)]  # D: distance
        for x, y in houses:
            self.bfs(G, x, y, C, D)

        h = len(houses)
        ans = INFINITY = float('inf')
        for x in range(m):
            for y in range(n):
                if G[x][y] != self.EMPTY or C[x][y] != h:
                    continue
                if D[x][y] < ans:
                    ans = D[x][y]

        return ans if ans < INFINITY else -1

    def bfs(self, G, x, y, C, D):
        m, n = len(G), len(G[0])
        visited = [[False] * n for _ in range(m)]

        queue = [(x, y)]
        distance = 0
        while queue:
            _queue = []
            distance += 1

            for x, y in queue:
                for dx, dy in self.V:
                    _x = x + dx
                    _y = y + dy
                    if not (0 <= _x < m and 0 <= _y < n):
                        continue
                    if visited[_x][_y] or G[_x][_y] != self.EMPTY:
                        continue
                    visited[_x][_y] = True
                    C[_x][_y] += 1
                    D[_x][_y] += distance
                    _queue.append((_x, _y))

            queue = _queue
