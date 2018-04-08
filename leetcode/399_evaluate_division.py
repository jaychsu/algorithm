import collections


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ans = []

        if not (
            equations and
            values and
            queries and
            len(equations) == len(values)
        ):
            return ans

        nexts = collections.defaultdict(set)
        evals = collections.defaultdict(float)

        for i in range(len(equations)):
            a, b = equations[i]
            nexts[a].add(b)
            nexts[b].add(a)
            evals[a, b] = 1.0 * values[i]
            evals[b, a] = 1.0 / values[i]

        for a, b in queries:
            res = self.dfs(a, b, 1, nexts, evals, set())
            ans.append(float(res))

        return ans

    def dfs(self, a, b, val, nexts, evals, visited):
        res = -1

        if a not in nexts:
            return res
        if a == b:
            # this condition must be after `a not in nexts`
            # to prevent the node not in graph
            return val

        visited.add(a)

        for c in nexts[a]:
            if c in visited or (a, c) not in evals:
                continue

            res = self.dfs(c, b, val * evals[a, c], nexts, evals, visited)

            if res != -1:
                break

        visited.discard(a)
        return res
