"""
Design a algorithm to initialize the board of Candy Crush Saga.
With M x N board, Q types of candies.

Rules:
1. with randomization
2. no 3 for run after initialization
3. must contain at least one valid move at the beginning

REF:
1. LC 723
2. http://massivetechinterview.blogspot.com/2015/11/how-to-initialize-board-of-candy-crush.html

TODO:
1. refactoring conflict resolving strategy, for current its just do `reset` again
2. implement `move` to move candy to D/R/U/L, and
    - remove the connected candy
    - the candy will drop if there is empty below
3. count score
4. end up game if no more valid move or the game is finished

Testing:
>>> gotcha = []
>>> for params in (
...     (7, 7, 3), (10, 10, 3), (20, 20, 3),
...     (7, 7, 5), (10, 10, 4), (20, 20, 6),
... ):
...     game = CandyCrush(*params)
...     for _ in range(10):
...         gotcha.append(_check_board_valid(game.get_board()))
>>> bool(gotcha) and all(gotcha)
True
"""
import random


def _check_board_valid(board):
    # for testing
    m, n = len(board), len(board[0])

    for x in range(2, m):
        for y in range(n):
            if board[x][y] == board[x - 1][y] == board[x - 2][y]:
                return False

    for y in range(2, n):
        for x in range(m):
            if board[x][y] == board[x][y - 1] == board[x][y - 2]:
                return False

    return True


class CandyCrush:
    def __init__(self, m, n, q):
        """
        :type m: int
        :type n: int
        :type q: int
        """
        self.__board = [[-1] * n for _ in range(m)]
        self.__types = q
        self.__patterns = (   # with rotating, we can find up to 12 patterns
            (-1, -1, 1,  0),  # /--
            (-1,  1, 1,  0),  # --\
            (-1, -1, 1, -1),  # /-\
        )
        self.reset_board()

    def reset_board(self):
        """
        :rtype: void
        """
        b = self.__board
        m, n = len(b), len(b[0])
        b[:] = [[-1] * n for _ in range(m)]
        x, y = random.randint(1, m - 2), random.randint(1, n - 2)
        d = random.choice(self.__patterns)  # dx1, dy1, dx2, dy2

        fixed = ((x + d[0], y + d[1]), (x, y), (x + d[2], y + d[3]))
        q = random.randrange(self.__types)
        for x, y in fixed:
            b[x][y] = q

        for x in range(m):
            for y in range(n):
                if (x, y) in fixed:
                    continue

                cnt = 0

                while not self._check_cell_valid(x, y):
                    if cnt > 50:
                        self.reset_board()

                    b[x][y] = random.randrange(self.__types)
                    cnt += 1

    def get_board(self):
        """
        :rtype: list[list[int]]
        """
        return self.__board

    def _check_cell_valid(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: bool
        """
        b = self.__board
        m, n = len(b), len(b[0])

        if b[x][y] == -1:
            return False

        for x1, y1, x2, y2 in (
            (x - 2, y, x - 1, y), (x + 1, y, x + 2, y),  # most up, down
            (x, y - 2, x, y - 1), (x, y + 1, x, y + 2),  # most left, right
            (x - 1, y, x + 1, y), (x, y - 1, x, y + 1),  # cross middle
        ):
            if not (
                0 <= x1 < m and 0 <= y1 < n and
                0 <= x2 < m and 0 <= y2 < n
            ):
                continue

            if b[x][y] == b[x1][y1] == b[x2][y2]:
                return False

        return True

    def _print_board(self):
        # for testing
        print('\n'.join(str(r) for r in self.__board))
