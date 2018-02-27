class Solution:
    def rotate(self, g):
        """
        :type g: List[List[int]]
        :rtype: void Do not return anything, modify g in-place instead.
        """
        if not g or not g[0] or len(g) != len(g[0]):
            return

        N = len(g)

        # swap by diagonal axis
        for i in range(N - 1):
            y = N - 1 - i
            for j in range(y):
                x = N - 1 - j
                g[i][j], g[x][y] = g[x][y], g[i][j]

        # swap by x-mid axis
        for i in range(N // 2):
            x = N - 1 - i
            for j in range(N):
                y = j
                g[i][j], g[x][y] = g[x][y], g[i][j]
