"""
>>> gotcha = []
>>> for _in, _out in (
...     (('', ''), 0), (('', 'hit'), 3), (('neat', ''), 4),
...     (('heat', 'hit'), 3), (('hot', 'not'), 2), (('some', 'thing'), 9),
...     (('abc', 'adbc'), 1), (('awesome', 'awesome'), 0), (('ab', 'ba'), 2),
... ):
...     for get_distance in (deletion_distance, deletion_distance2):
...         res = get_distance(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


def deletion_distance(s, t):
    if s == t:
        return 0
    if not s and not t:
        return 0
    if not s:
        return len(t)
    if not t:
        return len(s)

    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


def deletion_distance2(s, t):
    if s == t:
        return 0
    if not s and not t:
        return 0
    if not s:
        return len(t)
    if not t:
        return len(s)

    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(2)]
    pre = cur = 0

    for j in range(1, n + 1):
        dp[cur][j] = j

    for i in range(1, m + 1):
        pre, cur = cur, 1 - cur
        dp[cur][0] = i

        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[cur][j] = dp[pre][j - 1]
            else:
                dp[cur][j] = 1 + min(
                    dp[pre][j],
                    dp[cur][j - 1]
                )

    return dp[cur][n]
