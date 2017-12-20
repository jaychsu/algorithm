"""
Test Case:

[[1,1,1], [1,0,1], [1,1,1]]

[[1,1,1,0,0,0,0,0,0], [1,0,1,0,1,1,1,1,1], [1,1,1,0,0,0,0,0,0]]

# In the process of spreading will intersect
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

# needs to dedup `ex_virus` and `spreading`
[[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]
"""


class Solution:
    NORMAL = 0
    VIRUS = 1
    EX_VIRUS = -1

    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    def containVirus(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """

        walls = 0

        if not G or not G[0]:
            return walls

        while True:
            _walls = self.build_walls(G)
            if _walls == 0:
                break
            walls += _walls

        return walls

    def build_walls(self, G):
        m, n = len(G), len(G[0])
        ex_virus = []
        spreading = []
        walls = []
        visited = [[False] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if G[x][y] == self.VIRUS and not visited[x][y]:
                    ex_virus.append(set())
                    spreading.append(set())
                    walls.append(0)
                    self.dfs(x, y, G, visited, ex_virus, spreading, walls)

        _max_save = _max_i = -1
        s = len(spreading)
        for i in range(s):
            t = len(spreading[i])
            if t > _max_save:
                _max_save = t
                _max_i = i

        if _max_save == -1:
            return 0

        for i in range(s):
            if i == _max_i:
                for x, y in ex_virus[i]:
                    G[x][y] = self.EX_VIRUS
            else:
                for x, y in spreading[i]:
                    G[x][y] = self.VIRUS

        return walls[_max_i]

    def dfs(self, x, y, G, visited, ex_virus, spreading, walls):
        m, n = len(G), len(G[0])
        if not (0 <= x < m and 0 <= y < n) or visited[x][y]:
            return

        if G[x][y] == self.VIRUS:
            visited[x][y] = True
            ex_virus[-1].add((x, y))
            for dx, dy in self.V:
                _x = x + dx
                _y = y + dy
                self.dfs(_x, _y, G, visited, ex_virus, spreading, walls)
        elif G[x][y] == self.NORMAL:
            spreading[-1].add((x, y))
            walls[-1] += 1
