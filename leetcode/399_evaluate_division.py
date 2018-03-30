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

        if (
            not equations or
            not values or
            not queries or
            len(equations) != len(values)
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

    def dfs(self, start, end, val, nexts, evals, path):
        res = -1

        if start in path or start not in nexts:
            return res
        if start == end:
            return val

        path.add(start)

        for nxt in nexts[start]:
            if (start, nxt) not in evals:
                continue
            if res != -1:
                break

            res = self.dfs(
                nxt,
                end,
                val * evals[start, nxt],
                nexts,
                evals,
                path
            )

        path.discard(start)

        return res
