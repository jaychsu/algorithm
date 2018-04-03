class Solution:
    """
    BFS
    """
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str

        >>> s = Solution()
        >>> maze = [[0, 0, 0, 0, 0],
        ...         [1, 1, 0, 0, 1],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 1, 0, 0, 1],
        ...         [0, 1, 0, 0, 0]]

        >>> s.findShortestWay(maze, [4, 3], [0, 1])
        'lul'

        >>> s.findShortestWay(maze, [4, 3], [3, 0])
        'impossible'
        """
        NOT_FOUND = 'impossible'

        if not maze or not maze[0]:
            return NOT_FOUND

        m, n = len(maze), len(maze[0])
        sx, sy = ball
        tx, ty = hole
        queue = [(sx, sy)]
        paths = {(sx, sy): []}
        distance = {(sx, sy): 0}

        for x, y in queue:
            for dx, dy, dn in (
                (-1, 0, 'u'), (1, 0, 'd'),
                (0, -1, 'l'), (0, 1, 'r'),
            ):
                _x = x + dx
                _y = y + dy
                _step = 0

                while (
                    0 <= _x < m and 0 <= _y < n and
                    maze[_x][_y] == 0 and
                    not (_x == tx and _y == ty)
                ):
                    _x += dx
                    _y += dy
                    _step += 1

                if not (_x == tx and _y == ty):
                    _x -= dx
                    _y -= dy
                    _step -= 1

                if ((_x, _y) in distance and
                    distance[x, y] + _step > distance[_x, _y]):
                    continue

                if ((_x, _y) in paths and
                    paths[x, y] + [dn] > paths[_x, _y]):
                    continue

                distance[_x, _y] = distance[x, y] + _step
                paths[_x, _y] = paths[x, y] + [dn]
                queue.append((_x, _y))

        return ''.join(paths[tx, ty]) if (tx, ty) in paths else NOT_FOUND


import heapq


class Solution2:
    """
    Dijkstra
    """
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str

        >>> s = Solution2()
        >>> maze = [[0, 0, 0, 0, 0],
        ...         [1, 1, 0, 0, 1],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 1, 0, 0, 1],
        ...         [0, 1, 0, 0, 0]]

        >>> s.findShortestWay(maze, [4, 3], [0, 1])
        'lul'

        >>> s.findShortestWay(maze, [4, 3], [3, 0])
        'impossible'
        """
        NOT_FOUND = 'impossible'

        if not maze or not maze[0]:
            return NOT_FOUND

        m, n = len(maze), len(maze[0])
        sx, sy = ball
        tx, ty = hole
        heap = [(sx, sy)]
        paths = {(sx, sy): []}
        distance = {(sx, sy): 0}

        while heap:
            x, y = heapq.heappop(heap)

            for dx, dy, dn in (
                (-1, 0, 'u'), (1, 0, 'd'),
                (0, -1, 'l'), (0, 1, 'r'),
            ):
                _x = x + dx
                _y = y + dy

                while (
                    0 <= _x < m and 0 <= _y < n and
                    maze[_x][_y] == 0 and
                    not (_x == tx and _y == ty)
                ):
                    _x += dx
                    _y += dy

                if not (_x == tx and _y == ty):
                    _x -= dx
                    _y -= dy

                _step = distance[x, y] + abs(_x - x) + abs(_y - y)

                if (_x, _y) in distance and _step > distance[_x, _y]:
                    continue

                if (_x, _y) in paths and paths[x, y] + [dn] > paths[_x, _y]:
                    continue

                distance[_x, _y] = _step
                paths[_x, _y] = paths[x, y] + [dn]
                heapq.heappush(heap, (_x, _y))

        return ''.join(paths[tx, ty]) if (tx, ty) in paths else NOT_FOUND
