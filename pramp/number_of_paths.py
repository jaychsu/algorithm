def num_of_paths_to_dest(n):
    if not n or n == 0:
        return 0
    if n == 1:
        return 1

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][n - 1]
