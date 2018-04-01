class Solution:
    """
    BFS
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = 0

        if not coins or not amount:
            return ans

        queue, _queue = [0], []
        visited = set(queue)

        while queue:
            ans += 1

            for a in queue:
                for c in coins:
                    _a = a + c

                    if _a == amount:
                        return ans

                    if _a > amount or _a in visited:
                        continue

                    visited.add(_a)
                    _queue.append(_a)

            queue, _queue = _queue, []

        return -1


class Solution:
    """
    DP: TLE
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or not amount:
            return 0

        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for a in range(c, amount + 1):
                # if a < c: continue
                dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] < INF else -1
