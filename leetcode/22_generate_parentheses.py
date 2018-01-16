class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if not n:
            return ans

        self.dfs(n, 0, 0, ans, [])

        return ans

    def dfs(self, n, left, right, ans, path):
        if len(path) == 2 * n:
            ans.append(''.join(path))
            return

        if left < n:
            path.append('(')
            self.dfs(n, left + 1, right, ans, path)
            path.pop()

        if right < left:
            path.append(')')
            self.dfs(n, left, right + 1, ans, path)
            path.pop()
