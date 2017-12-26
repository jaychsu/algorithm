"""
Test Case:

"lintcode"
["de","ding","co","code","lint"]

"lintcode"
["li","nt","de","ding","co","code","lint"]

"aaab"
["b","aa"]

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""

"""
dfs: optimized by memory searching
"""
class Solution:
    def wordBreak(self, s, D):
        """
        :type s: str
        :type D: list[str]
        :rtype: list[str]
        """
        return self.memory_search(s, D, {})

    def memory_search(self, s, D, memo):
        if s in memo:
            return memo[s]

        res = []
        if not s:
            return res

        n = len(s)
        for size in range(1, n + 1):
            prefix = s[:size]
            if prefix not in D:
                continue
            if size == n:
                res.append(prefix)
                continue
            _res = self.memory_search(s[size:], D, memo)
            for _word in _res:
                res.append('{0} {1}'.format(prefix, _word))

        memo[s] = res
        return res


"""
dfs: TLE
"""
class Solution:
    def wordBreak(self, s, D):
        """
        :type s: str
        :type D: list[str]
        :rtype: list[str]
        """
        ans = []
        if not s or not D:
            return ans

        self.dfs(s, D, ans, [])

        return ans

    def dfs(self, s, D, ans, path):
        if not s:
            ans.append(' '.join(path))
            return

        for word in D:
            if not word or s.find(word) != 0:
                continue
            path.append(word)
            self.dfs(s[len(word):], D, ans, path)
            path.pop()
