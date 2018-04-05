"""
Description:
给一个grid的宽和长，求所有可能的路径数量。

1. unique_paths_from_three_dir: 从左下的点到右下的点，要求每次只能走三个方向 →↗↘

unique_paths_from_three_dir_1
follow up 1: 2d dp -> 1d dp (
    dp = [0] * m
    since the iterate order, for dp[x + 1] may modified by previous iteration
    so we need maintain two pointer `pre`, `cur` to save origin val in `dp[x]`
    and use this val in next iteration, that is `dp[x + 1]` for next
)


2. unique_paths_from_three_dir2: 从左上角走到右上角 (每一步，只能向正右、右上 或 右下走 →↗↘)

follow up 1：如果给矩形里的三个点，要求解决上述问题的同时，遍历这三个点 (
    unique_paths_from_three_dir2_1_1
    1. 切割矩形，一个一个地做DP，然后相加 (需要注意再进行下一个矩形遍历前，要把同 col 的其他值归零)

    unique_paths_from_three_dir2_1_2
 or 2. 在遍历到指定点时，把同一 col 的其他点归零 (因为 wrap 是沿 y 遍历，所以取 same col)
)

unique_paths_from_three_dir2_2
follow up 2：如何判断这三个点一个是合理的，即存在遍历这三个点的路经 (
    观察得知，把点集合按 y 升序排序，并假设某点座标在 x, y
    则此点的前一点必须位于 (呈现一个三角形)
        if y-1: [x-1, x+1]
        if y-2: [x-2, x+2]
        if y'=y-n: [x-n, x+n]
        ... => get dy = y-y' = n, x' MUST in [x-n, x+n]
    从 y 最大的点往前遍历检查前一点
)

unique_paths_from_three_dir2_3
follow up 3：如果给你一个 h，要求你的路径必须向下越过 h 这个界(x >= h)，怎么做 (
    1. 先遍历一遍超过 h 的，并直接到最底端
    2. 再把低于 h 的归零
    3. 再从 x = h - 1 遍历到 target，
       因为第一次的遍历已经把能到达 x >= h (即 [h, m - 1]) 的方法数找到了
       从 m - 1 开始的话，会有重复计算
)


Main Concept:
1. similiar to unique_path, but need to change iterative order

2. transition equation:
→: dp[x][y - 1]
↗: dp[x + 1][y - 1]
↘: dp[x - 1][y - 1]
"""


def unique_paths_from_three_dir(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> unique_paths_from_three_dir(2, 2)
    1
    >>> unique_paths_from_three_dir(2, 3)
    2
    >>> unique_paths_from_three_dir(3, 3)
    2
    >>> unique_paths_from_three_dir(4, 4)
    4
    """
    if not m or not n:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[m - 1][0] = 1

    for y in range(1, n):
        for x in range(m - 1, -1, -1):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

    return dp[m - 1][n - 1]


def unique_paths_from_three_dir_1(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> unique_paths_from_three_dir_1(2, 2)
    1
    >>> unique_paths_from_three_dir_1(2, 3)
    2
    >>> unique_paths_from_three_dir_1(3, 3)
    2
    >>> unique_paths_from_three_dir_1(4, 4)
    4
    """
    if not m or not n:
        return 0

    dp = [0] * m
    dp[m - 1] = 1

    for y in range(1, n):
        pre = cur = 0

        for x in range(m - 1, -1, -1):
            pre, cur = cur, dp[x]

            if x > 0:
                dp[x] += dp[x - 1]

            if x + 1 < m:
                dp[x] += pre

    return dp[m - 1]


def unique_paths_from_three_dir2(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int

    >>> unique_paths_from_three_dir2(2, 2)
    1
    >>> unique_paths_from_three_dir2(2, 3)
    2
    >>> unique_paths_from_three_dir2(3, 3)
    2
    >>> unique_paths_from_three_dir2(4, 4)
    4
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


def unique_paths_from_three_dir2_1_1(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: int

    >>> unique_paths_from_three_dir2_1_1(2, 3, [[1, 0], [1, 1], [1, 2]])
    0
    >>> unique_paths_from_three_dir2_1_1(3, 3, [[1, 0], [2, 1], [1, 2]])
    0
    >>> unique_paths_from_three_dir2_1_1(5, 5, [[0, 1], [2, 2], [1, 3]])
    0
    >>> unique_paths_from_three_dir2_1_1(5, 5, [[1, 1], [2, 2], [1, 3]])
    1
    >>> unique_paths_from_three_dir2_1_1(5, 5, [[2, 2], [1, 1], [1, 3]])
    1
    """
    if not m or not n or not points:
        return 0

    points = sorted(
        [p for p in points if p[1] != 0],
        key=lambda p: (p[1], p[0])
    )

    if len(points) != 3:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    pi = 0

    for y in range(1, n):
        for x in range(m):
            dp[x][y] = dp[x][y - 1]

            if x > 0:
                dp[x][y] += dp[x - 1][y - 1]

            if x + 1 < m:
                dp[x][y] += dp[x + 1][y - 1]

        if pi < 3:
            for x in range(m):
                if x != points[pi][0]:
                    dp[x][y] = 0
            pi += 1

    return dp[0][n - 1]


def unique_paths_from_three_dir2_1_2(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: int

    >>> unique_paths_from_three_dir2_1_2(2, 3, [[1, 0], [1, 1], [1, 2]])
    0
    >>> unique_paths_from_three_dir2_1_2(3, 3, [[1, 0], [2, 1], [1, 2]])
    0
    >>> unique_paths_from_three_dir2_1_2(5, 5, [[0, 1], [2, 2], [1, 3]])
    0
    >>> unique_paths_from_three_dir2_1_2(5, 5, [[1, 1], [2, 2], [1, 3]])
    1
    >>> unique_paths_from_three_dir2_1_2(5, 5, [[2, 2], [1, 1], [1, 3]])
    1
    """
    if not m or not n or not points:
        return 0

    def modify_dp(dp, x1, y1, x2, y2):
        RANGE = range(x1, x2 + 1) if x2 >= x1 else range(x1, x2 - 1, -1)

        for x in range(len(dp)):
            if x != x1:
                dp[x][y1] = 0

        for y in range(y1 + 1, y2 + 1):
            for x in RANGE:
                dp[x][y] = dp[x][y - 1]

                if x > 0:
                    dp[x][y] += dp[x - 1][y - 1]

                if x + 1 < m:
                    dp[x][y] += dp[x + 1][y - 1]

    points.sort(key=lambda p: (p[1], p[0]))

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    modify_dp(dp, 0, 0, points[0][0], points[0][1])
    modify_dp(dp, points[0][0], points[0][1], points[1][0], points[1][1])
    modify_dp(dp, points[1][0], points[1][1], points[2][0], points[2][1])
    modify_dp(dp, points[2][0], points[2][1], 0, n - 1)
    return dp[0][n - 1]


def unique_paths_from_three_dir2_2(m, n, points):
    """
    :type m: int
    :type n: int
    :type points: list[list[int]]
    :rtype: bool

    >>> unique_paths_from_three_dir2_2(2, 3, [[1, 0], [1, 1], [1, 2]])
    False
    >>> unique_paths_from_three_dir2_2(3, 3, [[1, 0], [2, 1], [1, 2]])
    False
    >>> unique_paths_from_three_dir2_2(5, 5, [[0, 1], [2, 2], [1, 3]])
    False
    >>> unique_paths_from_three_dir2_2(5, 5, [[1, 1], [2, 2], [1, 3]])
    True
    >>> unique_paths_from_three_dir2_2(5, 5, [[2, 2], [1, 1], [1, 3]])
    True
    """
    paths = [(0, 0)]
    points.sort(key=lambda p: (p[1], p[0]))
    paths.extend((x, y) for x, y in points)
    paths.append((0, n - 1))

    for i in range(1, len(paths)):
        x, y = paths[i]
        _x, _y = paths[i - 1]
        delta = y - _y

        if not x - delta <= _x <= x + delta:
            return False

    return True


def unique_paths_from_three_dir2_3(m, n, h):
    """
    :type m: int
    :type n: int
    :type h: int
    :rtype: int

    >>> unique_paths_from_three_dir2_3(2, 3, 1)
    1
    >>> unique_paths_from_three_dir2_3(3, 3, 1)
    1
    >>> unique_paths_from_three_dir2_3(3, 3, 2)
    0
    >>> unique_paths_from_three_dir2_3(4, 4, 0)
    4
    >>> unique_paths_from_three_dir2_3(4, 4, 1)
    3
    >>> unique_paths_from_three_dir2_3(4, 4, 2)
    0
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

    if h == 0:
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
