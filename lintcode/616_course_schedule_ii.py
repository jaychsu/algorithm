class Solution:
    def findOrder(self, n, P):
        """
        :type n: int
        :type P: List[List[int]]
        :rtype: List[int]
        """
        indeg = [0] * n
        edges = [[] for _ in range(n)]

        for c, p in P:
            indeg[c] += 1
            edges[p].append(c)

        queue = [i for i in range(n) if indeg[i] == 0]

        for p in queue:
            for c in edges[p]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    queue.append(c)

        if len(queue) != n:
            return []
        return queue
