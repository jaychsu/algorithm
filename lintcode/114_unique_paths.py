class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        mp = {}
        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0:
                    mp[(x, y)] = 1
                else:
                    mp[(x, y)] = mp[(x-1, y)] + mp[(x, y-1)]
        return mp[(m-1, n-1)]
