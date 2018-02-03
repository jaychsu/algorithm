class Solution:
    """
    @param S: Generating set of rules.
    @param s: Start symbol.
    @param e: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, S, start, end):
        if not start:
            start = ''

        N = {}

        for s in S:
            cur, nxt = s.split(' -> ')
            if cur not in N:
                N[cur] = set()
            N[cur].add(nxt)

        return self.dfs(N, end, start)

    def dfs(self, N, end, s):
        if len(s) > len(end):
            return False
        if s == end:
            return True

        for i in range(len(s)):
            if (not ord('A') <= ord(s[i]) <= ord('Z') or
                s[i] not in N):
                continue

            for _s in N[s[i]]:
                res = self.dfs(N, end, s[:i] + _s + s[i + 1:])
                if res:
                    return True

        return False
