"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""


class TrieNode:
    def __init__(self):
        self._end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        if not word:
            return
        parent = self.root
        for char in word:
            if char in parent.children:
                parent = parent.children[char]
            else:
                parent.children[char] = TrieNode()
                parent = parent.children[char]
        parent._end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        if not word:
            return False
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent._end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        if not prefix:
            return False
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
