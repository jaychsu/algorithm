"""
Description:
给一个grid的宽和长，求得从左下的点到右下的点所有可能的路径之和。
起点当然是左下，要求每次只能走三个方向 →↗↘
follow up: 2d dp -> 1d dp

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
