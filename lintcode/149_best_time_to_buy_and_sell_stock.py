class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        ans = 0
        if not prices:
            return ans

        minimum_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - minimum_price > ans:
                ans = prices[i] - minimum_price
            if prices[i] < minimum_price:
                minimum_price = prices[i]

        return ans
