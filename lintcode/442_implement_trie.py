class TrieNode:
    def __init__(self):
        self.end_of = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        if word is None:
            return

        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        if word is None:
            return False

        node = self.root

        for c in word:
            if c not in node.children:
                return False

            node = node.children[c]

        return node.end_of == word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        if prefix is None:
            return False

        node = self.root

        for c in prefix:
            if c not in node.children:
                return False

            node = node.children[c]

        return True
