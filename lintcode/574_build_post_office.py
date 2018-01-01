"""
Prefix Sum + Binary Searching
http://yuanyuanzhangcs.blogspot.hk/2017/02/build-post-office.html

for `X = [1, 2, 3, 4], x = 3`
and we want to get the sum of distances between `X[i]` and `x`
=> d = (3 - 1) + (3 - 2) + (3 - 3) + (4 - 3)

so we can use binary search to find the `i` of `x` in `X`
=> n = 4, i = 2 (since 2 < x == 3)
=> d = x * i - (1 + 2)  +  (3 + 4) - (n - i) * x

and we building prefix sum of `X`
=> `S = [0, 1, 3, 6, 10]`
=> d = x * i - S[i]  +  (S[n] - S[i]) - x * (n - i)
"""
class Solution:
    EMPTY = 0
    HOUSE = 1

    """
    @param: G: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, G):
        if not G or not G[0]:
            return -1

        m, n = len(G), len(G[0])
        X, Y = [], []
        for x in range(m):
            for y in range(n):
                if G[x][y] != self.HOUSE:
                    continue
                X.append(x)
                Y.append(y)

        if not X or len(X) == m * n:
            return -1
        Y.sort()

        s = len(X) + 1
        Sx, Sy = [0] * s, [0] * s  # prefix sum
        for i in range(1, s):
            Sx[i] = Sx[i - 1] + X[i - 1]
            Sy[i] = Sy[i - 1] + Y[i - 1]

        ans = INFINITY = float('inf')
        for x in range(m):
            for y in range(n):
                if G[x][y] != self.EMPTY:
                    continue
                distance = self.get_distance(Sx, X, x)
                distance += self.get_distance(Sy, Y, y)
                if distance < ans:
                    ans = distance

        return ans if ans < INFINITY else -1

    def get_distance(self, S, X, x):
        n = len(X)
        if X[0] > x:
            return S[n] - x * n
        if X[-1] < x:
            return x * n - S[n]

        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if X[mid] < x:
                left = mid
            else:
                right = mid

        return (x * right - S[right] +
                S[n] - S[right] - x * (n - right))


"""
BFS: TLE

time: O(mn)
find the center of the shape composed of houses
and then do bfs
"""
class Solution:
    EMPTY = 0
    HOUSE = 1

    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    """
    @param: G: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, G):
        if not G or not G[0]:
            return -1

        m, n = len(G), len(G[0])
        houses = []
        xc = yc = 0  # the center of the shape composed of houses
        for x in range(m):
            for y in range(n):
                if G[x][y] == self.HOUSE:
                    houses.append((x, y))
                    xc += x
                    yc += y
        xc //= len(houses)
        yc //= len(houses)

        ans = INFINITY = float('inf')
        visited = [[False] * n for _ in range(m)]
        visited[xc][yc] = True
        queue = [(xc, yc)]
        for x, y in queue:
            distance = self.get_distance(houses, x, y)
            if distance < ans and G[x][y] == self.EMPTY:
                ans = distance

            for dx, dy in self.V:
                _x = x + dx
                _y = y + dy
                if not (0 <= _x < m and 0 <= _y < n):
                    continue
                if visited[_x][_y]:
                    continue
                visited[_x][_y] = True
                queue.append((_x, _y))

        return ans if ans < INFINITY else -1

    def get_distance(self, houses, x, y):
        distance = 0
        for _x, _y in houses:
            distance += abs(_x - x) + abs(_y - y)
        return distance


"""
BFS: TLE

time: O((mn)^2)
brute force to bfs
"""
class Solution:
    EMPTY = 0
    HOUSE = 1

    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    """
    @param: G: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, G):
        if not G or not G[0]:
            return -1

        m, n = len(G), len(G[0])
        steps = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if G[x][y] == self.HOUSE:
                    self.bfs(G, x, y, steps)

        ans = INFINITY = float('inf')
        for x in range(m):
            for y in range(n):
                if G[x][y] != self.EMPTY:
                    continue
                if steps[x][y] < ans:
                    ans = steps[x][y]

        return ans if ans < INFINITY else -1

    def bfs(self, G, x, y, steps):
        m, n = len(G), len(G[0])
        visited = [[False] * n for _ in range(m)]

        queue = [(x, y)]
        visited[x][y] = True
        distance = 0
        while queue:
            _queue = []
            distance += 1

            for x, y in queue:
                for dx, dy in self.V:
                    _x = x + dx
                    _y = y + dy
                    if not (0 <= _x < m and 0 <= _y < n):
                        continue
                    if visited[_x][_y]:
                        continue
                    visited[_x][_y] = True
                    steps[_x][_y] += distance
                    _queue.append((_x, _y))

            queue = _queue
