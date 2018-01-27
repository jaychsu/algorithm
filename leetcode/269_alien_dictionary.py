"""
REF: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs/2
"""


class Solution:
    def alienOrder(self, W):
        if not W:
            return ''

        ans = []
        edges = {}
        indeg = {}

        for w in W:
            for c in w:
                indeg[c] = 0

        for i in range(len(W) - 1):
            cur = W[i]
            nxt = W[i + 1]
            for j in range(min(len(cur), len(nxt))):
                if cur[j] == nxt[j]:
                    continue
                if cur[j] not in edges:
                    edges[cur[j]] = set()
                if nxt[j] not in edges[cur[j]]:
                    edges[cur[j]].add(nxt[j])
                    indeg[nxt[j]] = indeg.get(nxt[j], 0) + 1
                break

        queue = [c for c, deg in indeg.items() if deg == 0]
        for c in queue:
            ans.append(c)
            if c not in edges:
                continue
            for _c in edges[c]:
                indeg[_c] -= 1
                if indeg[_c] == 0:
                    queue.append(_c)

        return ''.join(ans) if len(ans) == len(indeg) else ''
