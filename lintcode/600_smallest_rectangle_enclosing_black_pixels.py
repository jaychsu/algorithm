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
        top = self.binary_search(G, 0, x, self.is_empty_row)
        down = self.binary_search(G, m - 1, x, self.is_empty_row)
        left = self.binary_search(G, 0, y, self.is_empty_col)
        right = self.binary_search(G, n - 1, y, self.is_empty_col)

        return (down - top + 1) * (right - left + 1)

    def binary_search(self, G, start, end, is_empty):
        check = None
        if start < end:
            check = lambda start, end: start + 1 < end
        else:
            check = lambda start, end: start - 1 > end

        while check(start, end):
            mid = (start + end) // 2
            if is_empty(G, mid):
                start = mid
            else:
                end = mid

        return end if is_empty(G, start) else start

    def is_empty_row(self, G, x):
        for cell in G[x]:
            if cell == '1':
                return False
        return True

    def is_empty_col(self, G, y):
        for row in G:
            if row[y] == '1':
                return False
        return True
