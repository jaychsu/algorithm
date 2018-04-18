class Solution:
    def alienOrder(self, words):
        """
        :type words: list[str]
        :rtype: str
        """
        if not words:
            return ''

        ans = []
        gotcha = set()
        max_size = max(len(word) for word in words)

        for j in range(max_size):
            for word in words:
                if j >= len(word):
                    continue

                if word[j] in gotcha:
                    continue

                ans.append(word[j])
                gotcha.add(word[j])

        return ''.join(ans)


class Solution:
    """
    REF: https://discuss.leetcode.com/topic/28308/java-ac-solution-using-bfs/2
    """
    def alienOrder(self, words):
        if not words:
            return ''

        ans = []
        edges = {}
        indeg = {}

        for w in words:
            for c in w:
                indeg[c] = 0

        for i in range(len(words) - 1):
            cur = words[i]
            nxt = words[i + 1]
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
