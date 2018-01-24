class Solution:
    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    def numIslands(self, G):
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not G or not G[0]:
            return ans

        for x in range(len(G)):
            for y in range(len(G[x])):
                if G[x][y] == '0':
                    continue
                ans += 1
                self.dfs(G, x, y)

        return ans

    def dfs(self, G, x, y):
        G[x][y] = '0'
        for dx, dy in self.V:
            _x = x + dx
            _y = y + dy
            if not (0 <= _x < len(G) and 0 <= _y < len(G[_x])):
                continue
            if G[_x][_y] == '0':
                continue
            self.dfs(G, _x, _y)
