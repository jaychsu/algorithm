"""
REF: https://leetcode.com/problems/game-of-life/discuss/73223

lives < 2       => 1 -> 0
lives == 2 or 3 => 1 -> 1
lives > 3       => 1 -> 0
lives == 3      => 0 -> 1
"""


class Solution:
    """
    Use bits to save the status in next round
    """
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        for x in range(m):
            for y in range(n):
                lives = self.get_live_neibs(board, x, y)

                if board[x][y] == 1 and lives in (2, 3):
                    board[x][y] = 3
                elif board[x][y] == 0 and lives == 3:
                    board[x][y] = 2

        for x in range(m):
            for y in range(n):
                board[x][y] >>= 1

    def get_live_neibs(self, board, x, y):
        cnt = 0
        m, n = len(board), len(board[0])

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                _x = x + dx
                _y = y + dy

                if not (0 <= _x < m and 0 <= _y < n):
                    continue

                cnt += board[_x][_y] & 1

        return cnt


class Solution:
    """
    Not in-place solution
    """
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        ans = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                lives = self.get_live_neibs(board, x, y)
                ans[x][y] = board[x][y]

                if board[x][y] == 1 and lives < 2:
                    ans[x][y] = 0
                elif board[x][y] == 1 and lives in (2, 3):
                    ans[x][y] = 1
                elif board[x][y] == 1 and lives > 3:
                    ans[x][y] = 0
                elif board[x][y] == 0 and lives == 3:
                    ans[x][y] = 1

        # return ans

        # hacking for in-place
        for x in range(m):
            board[x][:] = ans[x][:]

    def get_live_neibs(self, board, x, y):
        cnt = 0
        m, n = len(board), len(board[0])

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                _x = x + dx
                _y = y + dy

                if not (
                    0 <= _x < m and
                    0 <= _y < n and
                    board[_x][_y] == 1
                ):
                    continue

                cnt += 1

        return cnt
