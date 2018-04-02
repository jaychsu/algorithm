"""
Main Concept:

in product case, needs to remove product in last recursion, and adds the product in current.
"""


class Solution:
    def addOperators(self, s, target):
        """
        :type s: str
        :type target: int
        :rtype: List[str]
        """
        ans = []

        if not s:
            return ans

        self.dfs(s, 0, target, 0, 0, ans, [])
        return ans

    def dfs(self, s, start, target, val, multi, ans, path):
        if start == len(s) and target == val:
            ans.append(''.join(path))
            return
        if start >= len(s):
            return

        for i in range(start, len(s)):
            if i > start and s[start] == '0':
                # only allow i == start and its `0`
                break

            sa = s[start:i + 1]
            a = int(sa)

            if start == 0:
                self.dfs(s, i + 1, target, a, a, ans, [sa])
                continue

            self.dfs(s, i + 1, target, val + a, a, ans, path + ['+', sa])
            self.dfs(s, i + 1, target, val - a, -a, ans, path + ['-', sa])
            self.dfs(s, i + 1, target, val - multi + multi * a, multi * a, ans, path + ['*', sa])
