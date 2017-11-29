class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, P):
        ans = 0
        if not P:
            return ans

        for i in range(1, len(P)):
            if P[i] > P[i - 1]:
                ans += P[i] - P[i - 1]

        return ans
