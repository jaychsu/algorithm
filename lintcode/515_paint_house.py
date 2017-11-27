class Solution:
    """
    @param: costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0

        INFINITY = float('inf')
        m, n = len(costs), len(costs[0])
        F = [[0] * n for _ in range(2)]

        """
        i: `i`th house
        j: `j`th color
        k: the used `k`th color in previous house
        """
        i = j = k = prev = curr = 0
        for j in range(n):
            F[0][j] = costs[0][j]
        for i in range(1, m):
            prev = (i - 1) % 2
            curr = i % 2
            for j in range(n):
                F[curr][j] = INFINITY
                for k in range(n):
                    if k != j and F[prev][k] + costs[i][j] < F[curr][j]:
                        F[curr][j] = F[prev][k] + costs[i][j]

        """
        curr == (m - 1) % 2
        """
        return min(F[curr])
