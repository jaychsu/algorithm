class Solution:
    """
    BFS
    """
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        if not maze or not maze[0]:
            return -1

        m, n = len(maze), len(maze[0])
        sx, sy = start
        tx, ty = destination
        queue = [(sx, sy)]
        distance = {(sx, sy): 0}

        for x, y in queue:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _x = x + dx
                _y = y + dy
                _step = 0

                while 0 <= _x < m and 0 <= _y < n and maze[_x][_y] == 0:
                    _x += dx
                    _y += dy
                    _step += 1

                _x -= dx
                _y -= dy

                if ((_x, _y) in distance and
                    distance[x, y] + _step >= distance[_x, _y]):
                    continue

                distance[_x, _y] = distance[x, y] + _step

                if _x == tx and _y == ty:
                    return distance[_x, _y]

                queue.append((_x, _y))

        return -1




import heapq


class Solution2:
    """
    Dijkstra
    """
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution2()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        if not maze or not maze[0]:
            return -1

        m, n = len(maze), len(maze[0])
        sx, sy = start
        tx, ty = destination
        heap = [(sx, sy)]
        distance = {(sx, sy): 0}

        while heap:
            x, y = heapq.heappop(heap)

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _x = x + dx
                _y = y + dy

                while 0 <= _x < m and 0 <= _y < n and maze[_x][_y] == 0:
                    _x += dx
                    _y += dy

                _x -= dx
                _y -= dy

                _step = distance[x, y] + abs(_x - x) + abs(_y - y)

                if (_x, _y) in distance and _step >= distance[_x, _y]:
                    continue

                if _x == tx and _y == ty:
                    return _step

                distance[_x, _y] = _step
                heapq.heappush(heap, (_x, _y))

        return -1
