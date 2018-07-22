import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end_of = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return repr(self.root)

    def put(self, word):
        if not self._is_str(word):
            return

        node = self.root

        for char in word:
            node = node.children[char]

        node.end_of = word

    def has_word(self, word):
        if not self._is_str(word):
            return False

        return self._search(word) is word

    def has_prefix(self, word):
        if not self._is_str(word):
            return False

        return self._search(word) is not False

    def get_node(self, char, node=None):
        if not node:
            node = self.root

        if char in node.children:
            return node.children[char]

    def _search(self, word):
        node = self.root

        if not word and node.end_of is None:
            return False

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.end_of

    def _is_str(self, word):
        return isinstance(word, (str, bytes))
