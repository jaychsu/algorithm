class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        Xs = set()
        DLs = set()  # left diagonal lines
        DRs = set()  # right diagonal lines
        return self.divide_conquer(n, 0, 0, Xs, DLs, DRs)

    def divide_conquer(self, n, y, cnt, Xs, DLs, DRs):
        for x in range(n):
            if x in Xs:
                continue

            dl = x - y
            if dl in DLs:
                continue

            dr = x + y
            if dr in DRs:
                continue

            if y == n - 1:
                cnt += 1
                continue

            Xs.add(x)
            DLs.add(dl)
            DRs.add(dr)
            cnt = self.divide_conquer(n, y + 1, cnt, Xs, DLs, DRs)
            Xs.discard(x)
            DLs.discard(dl)
            DRs.discard(dr)

        return cnt
