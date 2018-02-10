from heapq import heappush, heappop


class Solution:
    def swimInWater(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        ans = 0
        if not G or not G[0]:
            return ans

        n = len(G)
        V = ((-1, 0), (1, 0), (0, -1), (0, 1))

        heap = [(G[0][0], 0, 0)]
        visited = {(0, 0): True}

        while heap:
            depth, x, y = heappop(heap)
            if depth > ans:
                ans = depth
            if x == y == n - 1:
                return ans
            for dx, dy in V:
                _x = x + dx
                _y = y + dy
                if not (0 <= _x < n and 0 <= _y < n):
                    continue
                if (_x, _y) in visited:
                    continue
                visited[_x, _y] = True
                heappush(heap, (G[_x][_y], _x, _y))

        return ans
