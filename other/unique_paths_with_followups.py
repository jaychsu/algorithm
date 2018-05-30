"""
给定一个矩形的宽和长，求所有可能的路径数量

Rules：
1. 从左上角走到右上角
2. 要求每一步只能向正右、右上或右下走，即 →↗↘

followup1: 优化空间复杂度至 O(n)
followup2: 给定矩形里的三个点，判断是否存在遍历这三个点的路经
followup3: 给定矩形里的三个点，找到遍历这三个点的所有路径数量
followup4: 给定一个下界 (x == H)，找到能经过给定下界的所有路径数量 (x >= H)
followup5: 起点和终点改成从左上到左下，每一步只能 ↓↘↙，求所有可能的路径数量
"""


def find_unique_paths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 2), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 21), ((6, 7), 51),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    if not m or not n:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for y in range(1, n):
        for x in range(m):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    return dp[0][n - 1]


def find_unique_paths1(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths1(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 2), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 21), ((6, 7), 51),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    if not m or not n:
        return 0

    dp = [0] * m
    dp[0] = 1
    pre = cur = 0

    for y in range(1, n):
        pre = cur = 0

        for x in range(m):
            pre, cur = cur, dp[x]

            if x > 0:
                dp[x] += pre

            if x + 1 < m:
                dp[x] += dp[x + 1]

    return dp[0]


def find_unique_paths2(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: bool

    >>> gotcha = [
    ...     find_unique_paths2(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, [[1, 0], [1, 1], [1, 2]]), False),
    ...         ((3, 3, [[1, 0], [2, 1], [1, 2]]), False),
    ...         ((3, 3, [[1, 0], [1, 1], [1, 2]]), False),
    ...         ((5, 5, [[0, 1], [2, 2], [1, 3]]), False),
    ...         ((5, 5, [[1, 1], [2, 2], [1, 3]]), True),
    ...         ((5, 5, [[2, 2], [1, 1], [1, 3]]), True),
    ...         ((6, 8, [[0, 0], [4, 3], [0, 7]]), False),
    ...         ((8, 6, [[1, 1], [0, 4], [1, 3]]), True),
    ...         ((8, 6, [[1, 1], [0, 4], [2, 3]]), False),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    if not m or not n or not points or len(points) < 3:
        return False

    path = [(0, 0), (0, n - 1)]
    path.extend(tuple(p) for p in points)
    path.sort(key=lambda p: (p[1], p[0]))

    for i in range(1, len(path)):
        x, y = path[i]
        _x, _y = path[i - 1]
        delta = y - _y

        if not (x - delta <= _x <= x + delta):
            return False

    return True


def find_unique_paths3(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths3(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, [[1, 0], [1, 1], [1, 2]]), 0),
    ...         ((3, 3, [[1, 0], [2, 1], [1, 2]]), 0),
    ...         ((3, 3, [[1, 0], [1, 1], [1, 2]]), 0),
    ...         ((5, 5, [[0, 1], [2, 2], [1, 3]]), 0),
    ...         ((5, 5, [[1, 1], [2, 2], [1, 3]]), 1),
    ...         ((5, 5, [[2, 2], [1, 1], [1, 3]]), 1),
    ...         ((6, 8, [[0, 0], [4, 3], [0, 7]]), 0),
    ...         ((8, 6, [[0, 0], [0, 5], [0, 4]]), 9),
    ...         ((8, 6, [[1, 1], [0, 4], [2, 3]]), 0),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    NOT_FOUND = 0

    if not m or not n or not points:
        return NOT_FOUND

    points.sort(key=lambda p: (p[1], p[0]))

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    k = len(points)
    i = 0

    while points[i][1] == 0:
        i += 1

    if i >= k:
        return NOT_FOUND

    for y in range(1, n):
        for x in range(m):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

        if i < k and y == points[i][1]:
            for x in range(m):
                if x != points[i][0]:
                    dp[x][y] = 0
            i += 1

    return dp[0][n - 1] if i == k else NOT_FOUND


def find_unique_paths4(m, n, h):
    """
    :type m: int
    :type n: int
    :type h: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths4(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 3, 1), 1), ((3, 3, 1), 1), ((3, 3, 2), 0),
    ...         ((4, 4, 0), 4), ((4, 4, 1), 3), ((4, 4, 2), 0),
    ...         ((6, 7, 0), 51), ((6, 7, 1), 50), ((6, 7, 2), 19),
    ...         ((6, 7, 3), 1), ((6, 7, 4), 0), ((6, 7, 5), 0)
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    if not m or not n:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for y in range(1, n):
        for x in range(m):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    if h < 1:
        return dp[0][n - 1]

    for y in range(n):
        for x in range(h):
            dp[x][y] = 0

    for y in range(1, n):
        for x in range(h - 1, -1, -1):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    return dp[0][n - 1]


def find_unique_paths5(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> gotcha = [
    ...     find_unique_paths5(*_in) == _out
    ...     for _in, _out in (
    ...         ((2, 2), 1), ((2, 3), 1), ((3, 3), 2),
    ...         ((5, 5), 9), ((7, 6), 51), ((6, 7), 21),
    ...     )
    ... ]
    >>> bool(gotcha) and all(gotcha)
    True
    """
    if not m or not n:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for x in range(1, m):
        for y in range(n):
            dp[x][y] = dp[x - 1][y]

            if y > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if y + 1 < n:
                dp[x][y] += dp[x - 1][y + 1]

    return dp[m - 1][0]
