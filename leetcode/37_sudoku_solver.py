class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0] or len(board) != len(board[0]):
            return

        self.dfs(board, 0, 0)

    def dfs(self, board, x, y):
        n = len(board)

        if x == n:
            return True

        _x, _y = x, y + 1

        if y == n - 1:
            _x = x + 1
            _y = 0

        if board[x][y] != '.':
            if not self.is_valid(board, x, y):
                return False
            return self.dfs(board, _x, _y)

        for i in range(1, n + 1):
            board[x][y] = str(i)
            if (
                self.is_valid(board, x, y) and
                self.dfs(board, _x, _y)
            ):
                return True

        board[x][y] = '.'
        return False

    def is_valid(self, board, x, y):
        if board[x][y] not in '123456789':
            return False

        n = len(board)

        for i in range(n):
            if y != i and board[x][y] == board[x][i]:
                return False
            if x != i and board[x][y] == board[i][y]:
                return False

        r = x // 3 * 3
        c = y // 3 * 3

        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if x == i and y == j:
                    continue
                if board[x][y] == board[i][j]:
                    return False

        return True
