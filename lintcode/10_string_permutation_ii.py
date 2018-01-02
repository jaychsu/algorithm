class Solution:
    """
    @param: S: A string
    @return: all permutations
    """
    def stringPermutation2(self, S):
        if not S:
            return ['']

        S = sorted(S)

        ans = []
        self.dfs(S, ans, [])
        return ans

    def dfs(self, S, ans, path):
        if not S:
            ans.append(''.join(path))
            return

        for i in range(len(S)):
            if i > 0 and S[i] == S[i - 1]:
                continue
            path.append(S[i])
            self.dfs(S[:i] + S[i + 1:], ans, path)
            path.pop()
