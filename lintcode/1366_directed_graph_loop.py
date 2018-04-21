import collections


class Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    def isCyclicGraph(self, start, end):
        if not start or not end or len(start) != len(end):
            return False

        n = len(start)
        nxt = collections.defaultdict(set)
        visited = set()
        rec_stack = set()

        for i in range(n):
            nxt[start[i]].add(end[i])

        for i in range(n):
            if start[i] in visited:
                continue
            if self.dfs(start[i], nxt, visited, rec_stack):
                return True

        return False

    def dfs(self, u, nxt, visited, rec_stack):
        if u not in nxt:
            return False

        visited.add(u)
        rec_stack.add(u)

        for v in nxt[u]:
            if v in rec_stack:
                return True

            if v not in visited and self.dfs(v, nxt, visited, rec_stack):
                return True

        rec_stack.discard(u)
        return False
