"""
BFS
"""
class Solution:
    def coinChange(self, C, amount):
        """
        :type C: List[int]
        :type amount: int
        :rtype: int
        """
        ans = 0
        if not amount:
            return ans

        queue, _queue = [0], []
        visited = [False] * (amount + 1)
        visited[0] = True

        while queue:
            ans += 1
            for x in queue:
                for c in C:
                    _x = x + c

                    if _x == amount:
                        return ans
                    if _x > amount or visited[_x]:
                        continue

                    visited[_x] = True
                    _queue.append(_x)

            queue, _queue = _queue, []

        return -1


"""
DP: TLE
"""
class Solution:
    def coinChange(self, C, amount):
        """
        :type C: List[int]
        :type amount: int
        :rtype: int
        """
        INFINITY = float('inf')
        dp = [INFINITY] * (amount + 1)
        dp[0] = 0

        for c in C:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[amount] if dp[amount] < INFINITY else -1
