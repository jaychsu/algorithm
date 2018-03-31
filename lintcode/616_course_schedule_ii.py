class Solution:
    def findOrder(self, n, prerequisites):
        """
        :type n: int
        :type prerequisites: list[list[int]]
        :rtype: list[int]
        """
        ans = []

        if not n:
            return ans

        indeg = [0] * n
        edges = [[] for _ in range(n)]

        for c, p in prerequisites:
            indeg[c] += 1
            edges[p].append(c)

        queue = [c for c in range(n) if indeg[c] == 0]

        for p in queue:
            for c in edges[p]:
                indeg[c] -= 1

                if indeg[c] == 0:
                    queue.append(c)

        if len(queue) != n:
            return []

        return queue
