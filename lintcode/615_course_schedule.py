class Solution:
    def canFinish(self, n, P):
        """
        :type n: int
        :type P: List[List[int]]
        :rtype: bool
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

        return len(queue) == n
