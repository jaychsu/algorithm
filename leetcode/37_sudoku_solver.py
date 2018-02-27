class Solution:
    def solveSudoku(self, g):
        """
        :type grid: List[List[str]]
        :rtype: void Do not return anything, modify grid in-place instead.
        """
        if not g or not g[0] or len(g) != len(g[0]):
            return

        self.VALID_CHARS = set([str(i) for i in range(1, len(g) + 1)])
        self.dfs(g, 0, 0)

    def dfs(self, g, x, y):
        N = len(g)
        if x == N:
            return True

        _x, _y = x, y + 1
        if y == N - 1:
            _x = x + 1
            _y = 0  # === (y + 1) % N

        if g[x][y] != '.':
            if not self.is_valid(g, x, y):
                return False
            return self.dfs(g, _x, _y)

        for i in range(1, N + 1):
            g[x][y] = str(i)
            if self.is_valid(g, x, y) and self.dfs(g, _x, _y):
                return True

        g[x][y] = '.'
        return False

    def is_valid(self, g, x, y):
        if g[x][y] not in self.VALID_CHARS:
            return False

        N = len(g)
        GROUP_CNT = int(N ** 0.5)

        for i in range(N):
            if y != i and g[x][y] == g[x][i]:
                return False
            if x != i and g[x][y] == g[i][y]:
                return False

        r = x // GROUP_CNT * GROUP_CNT
        c = y // GROUP_CNT * GROUP_CNT
        for i in range(r, r + GROUP_CNT):
            for j in range(c, c + GROUP_CNT):
                if x == i and y == j:
                    continue
                if g[x][y] == g[i][j]:
                    return False

        return True
