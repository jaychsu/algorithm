class Solution:
    """
    @param: G: a binary matrix with '0' and '1'
    @param: x: the location of one of the black pixels
    @param: y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, G, x, y):
        if not G or not G[0]:
            return 0

        m, n = len(G), len(G[0])

        left = self.binary_search(0, y, G, self.is_empty_col)
        right = self.binary_search(n - 1, y, G, self.is_empty_col)
        top = self.binary_search(0, x, G, self.is_empty_row)
        down = self.binary_search(m - 1, x, G, self.is_empty_row)

        return (right - left + 1) * (down - top + 1)

    def binary_search(self, start, end, G, is_empty):
        mid = cond = None
        if start <= end:
            cond = lambda start, end: start + 1 < end
        else:
            cond = lambda start, end: start - 1 > end

        while cond(start, end):
            mid = start + (end - start) // 2
            if is_empty(G, mid):
                start = mid
            else:
                end = mid
        return end if is_empty(G, start) else start

    def is_empty_row(self, G, x):
        for y in range(len(G[x])):
            if G[x][y] == '1':
                return False
        return True

    def is_empty_col(self, G, y):
        for x in range(len(G)):
            if G[x][y] == '1':
                return False
        return True
