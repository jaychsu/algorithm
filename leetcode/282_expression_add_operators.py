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
        n = len(s)

        if start == n and val == target:
            ans.append(''.join(path))
            return
        if start >= n:
            return

        for i in range(start, n):
            if i > start and s[start] == '0':
                break

            j = i + 1
            num = int(s[start:j])

            if start == 0:
                self.dfs(s, j, target, num, num, ans, [str(num)])
            else:
                self.dfs(s, j, target, val + num,  num, ans, path + ['+', str(num)])
                self.dfs(s, j, target, val - num, -num, ans, path + ['-', str(num)])
                self.dfs(
                    s, j, target,
                    val - multi + num * multi,
                    num * multi,
                    ans, path + ['*', str(num)]
                )
