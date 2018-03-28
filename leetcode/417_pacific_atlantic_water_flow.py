"""
BFS

1. for both p-side and a-side, init with queue and visit set
2. add the edge and do bfs
3. only add the cell which higher or equal the previous cell
4. get the intersection in both set
"""
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        pqueue, aqueue = [], []
        pvisit, avisit = set(), set()

        for y in range(n):
            pvisit.add((0, y))
            pqueue.append((0, y))
            avisit.add((m - 1, y))
            aqueue.append((m - 1, y))

        for x in range(m):
            pvisit.add((x, 0))
            pqueue.append((x, 0))
            avisit.add((x, n - 1))
            aqueue.append((x, n - 1))

        self.bfs(matrix, pqueue, pvisit)
        self.bfs(matrix, aqueue, avisit)

        return list(sorted(pvisit & avisit))

    def bfs(self, matrix, queue, visit):
        m, n = len(matrix), len(matrix[0])

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
                    (_x, _y) not in visit and
                    matrix[_x][_y] >= matrix[x][y]
                ):
                    continue

                queue.append((_x, _y))
                visit.add((_x, _y))


"""
DFS
"""
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        pvisit, avisit = set(), set()

        for y in range(n):
            self.dfs(matrix, 0, y, pvisit)
            self.dfs(matrix, m - 1, y, avisit)

        for x in range(m):
            self.dfs(matrix, x, 0, pvisit)
            self.dfs(matrix, x, n - 1, avisit)

        return list(sorted(pvisit & avisit))

    def dfs(self, matrix, x, y, visit):
        visit.add((x, y))

        for dx, dy in (
            ( 0, -1),
            ( 0,  1),
            (-1,  0),
            ( 1,  0),
        ):
            _x = x + dx
            _y = y + dy

            if not (
                0 <= _x < len(matrix) and
                0 <= _y < len(matrix[0]) and
                (_x, _y) not in visit and
                matrix[_x][_y] >= matrix[x][y]
            ):
                continue

            self.dfs(matrix, _x, _y, visit)
