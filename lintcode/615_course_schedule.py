class Solution:
    """
    @param: n: a total of n courses
    @param: P: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, n, P):
        if not n:
            return False

        indegs = [0 for _ in range(n)]
        edges = [[] for _ in range(n)]
        queue = []

        """
        c: course, p: prerequisite

        in `edges`, the edge between same both points
        will only count once.
        """
        for c, p in P:
            edges[p].append(c)
            indegs[c] += 1

        for i in range(n):
            indeg = indegs[i]
            if indeg == 0:
                queue.append(i)

        cnt = 0
        for p in queue:
            cnt += 1
            for c in edges[p]:
                indegs[c] -= 1
                if indegs[c] == 0:
                    queue.append(c)

        return cnt == n
