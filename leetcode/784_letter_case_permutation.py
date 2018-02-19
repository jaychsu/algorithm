class Solution:
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']
        ans = []
        self.dfs(s, 0, ans, [])
        return ans

    def dfs(self, s, i, ans, path):
        if i == len(s):
            ans.append(''.join(path))
            return

        options = [s[i]] if s[i].isdigit() else [s[i].lower(), s[i].upper()]

        for c in options:
            path.append(c)
            self.dfs(s, i + 1, ans, path)
            path.pop()
