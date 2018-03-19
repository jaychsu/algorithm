class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        ans = []
        if not n:
            return ans

        self.dfs(n, 1, 0, ans, ['('])
        return ans

    def dfs(self, n, lcnt, rcnt, ans, path):
        if len(path) == 2 * n:
            ans.append(''.join(path))
            return

        if rcnt < lcnt:
            path.append(')')
            self.dfs(n, lcnt, rcnt + 1, ans, path)
            path.pop()

        if lcnt < n:
            path.append('(')
            self.dfs(n, lcnt + 1, rcnt, ans, path)
            path.pop()
