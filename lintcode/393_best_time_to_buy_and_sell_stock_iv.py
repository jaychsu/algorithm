class Solution:
    """
    @param: K: An integer
    @param: P: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, P):
        if not K or not P:
            return 0

        n = len(P)

        """
        if `K >= n`, this problem is just
        `./lintcode/150_best_time_to_buy_and_sell_stock_ii.py`
        so we dont need to use `dp`, since it lead to overflow
        """
        if K >= n:
            profit = 0
            for i in range(1, n):
                if P[i] > P[i - 1]:
                    profit += P[i] - P[i - 1]
            return profit

        """
        the main concept is in
        `./lintcode/151_best_time_to_buy_and_sell_stock_iii.py`
        """
        STAGE = 2 * K + 1
        dp = [[0] * STAGE for _ in range(2)]

        i = j = prev = curr = profit = 0
        for i in range(1, n):
            prev = curr
            curr = 1 - prev
            profit = P[i] - P[i - 1]
            for j in range(1, STAGE, 2):
                dp[curr][j] = max(dp[prev][j] + profit, dp[prev][j - 1])
            for j in range(2, STAGE, 2):
                dp[curr][j] = max(dp[prev][j], dp[prev][j - 1] + profit)

        return max(dp[curr])
