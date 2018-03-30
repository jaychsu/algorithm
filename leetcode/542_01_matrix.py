class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        ans = [[float('inf')] * n for _ in range(m)]
        queue = []

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    ans[x][y] = 0
                    queue.append((x, y))

        for x, y in queue:
            for dx, dy in (
                ( 0, -1),
                ( 0,  1),
                (-1,  0),
                ( 1,  0),
            ):
                _x = x + dx
                _y = y + dy

                if not (
                    0 <= _x < m and
                    0 <= _y < n and
                    matrix[_x][_y] == 1 and
                    ans[_x][_y] > ans[x][y]
                ):
                    continue

                ans[_x][_y] = ans[x][y] + 1
                queue.append((_x, _y))

        return ans
