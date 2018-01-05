class Solution:
    """
    @param: P: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, P):
        ans = 0
        if not P:
            return ans

        Pmin = P[0]

        for i in range(1, len(P)):
            if P[i] - Pmin > ans:
                ans = P[i] - Pmin
            if P[i] < Pmin:
                Pmin = P[i]

        return ans
