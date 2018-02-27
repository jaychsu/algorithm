class Solution:
    def isValidSudoku(self, g):
        """
        :type g: List[List[str]]
        :rtype: bool
        """
        if not g or not g[0] or len(g) != len(g[0]):
            return False

        N = len(g)
        GROUP_CNT = int(N ** 0.5)
        VALID_CHARS = set([str(i) for i in range(1, N + 1)])
        EMPTY = '.'

        for i in range(N):
            used = set()
            for j in range(N):
                if g[i][j] == EMPTY:
                    continue
                if g[i][j] not in VALID_CHARS:
                    return False
                if g[i][j] in used:
                    return False
                used.add(g[i][j])

        for j in range(N):
            used = set()
            for i in range(N):
                if g[i][j] == EMPTY:
                    continue
                if g[i][j] not in VALID_CHARS:
                    return False
                if g[i][j] in used:
                    return False
                used.add(g[i][j])

        for x in range(GROUP_CNT):
            for y in range(GROUP_CNT):
                used = set()
                x_from, x_to = GROUP_CNT * x, GROUP_CNT * x + GROUP_CNT
                y_from, y_to = GROUP_CNT * y, GROUP_CNT * y + GROUP_CNT
                for i in range(x_from, x_to):
                    for j in range(y_from, y_to):
                        if g[i][j] == EMPTY:
                            continue
                        if g[i][j] not in VALID_CHARS:
                            return False
                        if g[i][j] in used:
                            return False
                        used.add(g[i][j])

        return True
