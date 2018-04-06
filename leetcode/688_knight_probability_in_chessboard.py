import collections


class Solution:
    """
    DP:
    1. init the first pos as 1
    2. keep simulate the process and divide the probability
    3. sum the values
    """
    def knightProbability(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = collections.defaultdict(int)
        dp[r, c] = 1.0

        for _ in range(k):
            nxt = collections.defaultdict(int)

            for x in range(n):
                for y in range(n):
                    for dx, dy in (
                        (-1, -2),
                        ( 1, -2),
                        (-2, -1),
                        ( 2, -1),
                        (-2,  1),
                        ( 2,  1),
                        (-1,  2),
                        ( 1,  2),
                    ):
                        _x = x + dx
                        _y = y + dy

                        if not (0 <= _x < n and 0 <= _y < n):
                            continue

                        nxt[_x, _y] += dp[x, y] / 8.0

            dp = nxt

        return sum(dp.values())


class Solution:
    """
    BFS: TLE
    """
    def knightProbability(self, n, k, r, c):
        """
        :type n: int
        :type k: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if n == 1 and k == 0:
            return 1.0

        queue, _queue = [(r, c)], []
        total = 8 ** k
        valid = 0

        while queue and k:
            k -= 1

            for x, y in queue:
                for dx, dy in (
                    (-1, -2),
                    ( 1, -2),
                    (-2, -1),
                    ( 2, -1),
                    (-2,  1),
                    ( 2,  1),
                    (-1,  2),
                    ( 1,  2),
                ):
                    _x = x + dx
                    _y = y + dy

                    if not (0 <= _x < n and 0 <= _y < n):
                        continue

                    if k == 0:
                        valid += 1

                    if k > 0:
                        _queue.append((_x, _y))

            queue, _queue = _queue, []

        return valid / total
