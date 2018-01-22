class Solution(object):
    def addOperators(self, s, target):
        """
        :type s: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        if not s:
            return ans

        self.dfs(s, target, 0, 0, 0, ans, [])
        ans.sort()

        return ans

    def dfs(self, s, target, start, val, product, ans, path):
        if start == len(s):
            if target == val:
                ans.append(''.join(path))
            return

        for i in range(start, len(s)):
            if i > start and s[start] == '0':
                break
            a = int(s[start:i + 1])

            if start == 0:
                self.dfs(s, target, i + 1, a, a, ans, path + [str(a)])
                continue

            """
            in product case, needs to remove product in last recursion, and adds the product in current.
            """
            self.dfs(s, target, i + 1, val + a,  a, ans, path + ['+', str(a)])
            self.dfs(s, target, i + 1, val - a, -a, ans, path + ['-', str(a)])
            self.dfs(s, target, i + 1, val - product + product * a, product * a, ans, path + ['*', str(a)])
