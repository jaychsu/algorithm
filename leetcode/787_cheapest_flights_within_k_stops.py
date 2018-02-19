class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        min_cost = [float('inf')] * n  # the minimum cost to get to node
        costs = [float('inf')] * n
        min_cost[src] = costs[src] = 0

        for _ in range(K + 1):
            for u, v, cost in flights:
                costs[v] = min(costs[v], min_cost[u] + cost)
            min_cost = costs

        return costs[dst] if costs[dst] < float('inf') else -1
