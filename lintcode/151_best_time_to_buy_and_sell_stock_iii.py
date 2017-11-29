class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, P):
        if not P:
            return 0

        K = 2
        STAGE = 2 * K + 1

        """
        `dp[i][j]` means the `i`th day at the `j`th stage
        stage 0: before the first buying
        stage 1: holding the first stock
        stage 2: after the first selling, before the second buying
        stage 3: holding the second stock
        stage 4: after the second selling

        note that, `dp[i][0]` means always stay in stage 0,
        so its never going to be profitable
        """
        dp = [[0] * STAGE for _ in range(2)]

        i = j = prev = curr = profit = 0
        for i in range(1, len(P)):
            prev = curr
            curr = 1 - curr
            profit = P[i] - P[i - 1]
            for j in range(1, STAGE, 2):
                """
                in stage 1 and 3, holding a stock
                profit comes from:
                1. still holding a stock yesterday,
                   and gains profit (may be negative) today
                2. holding no any stock yesterday,
                   just makes a buying today, so no profit
                choose the maximum
                """
                dp[curr][j] = max(dp[prev][j] + profit, dp[prev][j - 1])
            for j in range(2, STAGE, 2):
                """
                in stage 2 and 4, holding no any stock
                profit comes from:
                1. still holding no any stock yesterday,
                   just makes a buying today, so no profit
                2. holding a stock yesterday,
                   and gains profit (may be negative) today
                choose the maximum
                """
                dp[curr][j] = max(dp[prev][j], dp[prev][j - 1] + profit)

        return max(dp[curr])
