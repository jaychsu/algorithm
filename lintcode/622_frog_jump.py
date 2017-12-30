"""
BFS
"""
class Solution:
    """
    @param: S: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, S):
        if not S:
            return False
        if len(S) < 2:
            return True

        _S = set(S)  # x in set is O(1)

        queue = [(S[0], 0)]
        visited = {(S[0], 0): True}
        for pos, k in queue:
            for x in (k - 1, k, k + 1):
                if (x > 0 and pos + x in _S and
                    not visited.get((pos + x, x))):
                    if pos + x == S[-1]:
                        return True
                    visited[pos + x, x] = True
                    queue.append((pos + x, x))

        return False


"""
DP
"""
class Solution:
    """
    @param: S: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, S):
        if not S:
            return False

        dp = {}
        for pos in S:
            dp[pos] = set()

        dp[S[0]].add(0)

        for pos in S:
            for k in dp[pos]:
                if k > 1 and pos + k - 1 in dp:
                    dp[pos + k - 1].add(k - 1)
                if pos + k in dp:
                    dp[pos + k].add(k)
                if pos + k + 1 in dp:
                    dp[pos + k + 1].add(k + 1)

        return len(dp[S[-1]]) > 0
