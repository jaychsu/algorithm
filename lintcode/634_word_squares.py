"""
Trie + DFS
"""



"""
TLE: DFS
"""
class Solution:
    def wordSquares(self, words):
        """
        :type words: list[str]
        :rtype: list[list[str]]
        """
        ans = []
        if not words:
            return ans

        self.dfs(words, len(words[0]), ans, [])

        return ans

    def dfs(self, words, n, ans, path):
        if (len(path) == n and
            self.is_valid(path)):
            ans.append(path[:])
            return

        if len(path) >= n:
            return

        for i in range(len(words)):
            path.append(words[i])
            self.dfs(words, n, ans, path)
            path.pop()

    def is_valid(self, path):
        if not path or len(path) != len(path[0]):
            return False

        for i in range(1, len(path)):
            for j in range(i):
                if path[i][j] != path[j][i]:
                    return False

        return True
