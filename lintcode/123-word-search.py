class Solution:
    def __init__(self):
        self.row_vector = [1, -1, 0, 0]
        self.col_vector = [0, 0, 1, -1]

    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if not board or not word or len(board) < 1:
            return False
        self.board, self.word = board, word
        self.m, self.n, self.l = len(board), len(board[0]), len(word)
        is_visited = [[0 for j in range(self.n)] for i in range(self.m)]
        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == word[0] \
                        and self.find(row, col, 1, is_visited):
                    # Don't return result of `self.find` directly
                    # since there might be multiple `word[0]`
                    return True
        return False

    def find(self, x, y, i, is_visited):
        if self.l == i:
            return True
        for d in range(4):
            _x, _y = x + self.row_vector[d], y + self.col_vector[d]
            if 0 <= _x < self.m \
                    and 0 <= _y < self.n \
                    and not is_visited[_x][_y] \
                    and self.board[_x][_y] == self.word[i]:
                is_visited[_x][_y] = 1
                # Don't return result of `self.find` directly
                # since must reset the cell in `is_visited`
                if self.find(_x, _y, i + 1, is_visited):
                    return True
                else:
                    is_visited[_x][_y] = 0
        return False
