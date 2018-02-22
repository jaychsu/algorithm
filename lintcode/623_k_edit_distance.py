class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word):
        if not isinstance(word, str):
            return

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.end_of = word


class Solution:
    """
    @param: S: a set of stirngs
    @param: target: a target string
    @param: K: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, S, target, K):
        trie = Trie()
        for word in S:
            trie.put(word)

        ans = []
        dp = [i for i in range(len(target) + 1)]

        self.dfs(trie.root, K, target, ans, dp)
        return ans

    def dfs(self, node, k, target, ans, pre):
        n = len(target)

        if node.end_of is not None and pre[n] <= k:
            ans.append(node.end_of)

        dp = [0] * (n + 1)

        for char in node.children:
            dp[0] = pre[0] + 1

            for i in range(1, n + 1):
                if target[i - 1] == char:
                    dp[i] = min(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1]
                    )
                else:
                    dp[i] = min(
                        dp[i - 1] + 1,
                        pre[i] + 1,
                        pre[i - 1] + 1
                    )

            self.dfs(node.children[char], k, target, ans, dp)
