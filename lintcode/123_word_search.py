class Solution:
    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    """
    @param: G: A list of lists of character
    @param: s: A string
    @return: A boolean
    """
    def exist(self, G, s):
        if G is None or G[0] is None or s is None:
            return False

        m, n = len(G), len(G[0])
        visited = [[False] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if (G[x][y] == s[0] and
                    self.dfs(G, x, y, s, 1, visited)):
                    return True

        return False

    def dfs(self, G, x, y, s, i, visited):
        if i >= len(s):
            return True

        for dx, dy in self.V:
            _x = x + dx
            _y = y + dy
            if not (0 <= _x < len(G) and 0 <= _y < len(G[0])):
                continue
            if visited[_x][_y] or G[_x][_y] != s[i]:
                continue

            visited[_x][_y] = True
            if self.dfs(G, _x, _y, s, i + 1, visited):
                return True
            visited[_x][_y] = False

        return False
