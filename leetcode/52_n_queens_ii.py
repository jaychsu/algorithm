class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        Ys = set()  # ys
        DLs = set()  # left diagonal lines
        DRs = set()  # right diagonal lines
        return self.divide_conquer(n, 0, 0, Ys, DLs, DRs)

    def divide_conquer(self, n, x, cnt, Ys, DLs, DRs):
        for y in range(n):
            if y in Ys:
                continue

            dl = x - y
            if dl in DLs:
                continue

            dr = x + y
            if dr in DRs:
                continue

            if x == n - 1:
                cnt += 1
                continue

            Ys.add(y)
            DLs.add(dl)
            DRs.add(dr)
            cnt = self.divide_conquer(n, x + 1, cnt, Ys, DLs, DRs)
            Ys.discard(y)
            DLs.discard(dl)
            DRs.discard(dr)

        return cnt
