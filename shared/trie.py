class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, string):
        if not string:
            return
        parent = self.root
        for char in string:
            if char in parent:
                parent = parent[char]
            else:
                parent[char] = {}
                parent = parent[char]
        parent['_end'] = True

    def search(self, string):
        if not string:
            return False
        parent = self.root
        for char in string:
            if char in parent:
                parent = parent[char]
            else:
                return False
        return True

    def search_in_regex(self, string):
        if not string:
            return False
        return self._search_in_regex(string, self.root, 0)

    def _search_in_regex(self, string, parent, i):
        if i == len(string):
            return parent.get('_end', False)
        result = False
        if string[i] == '.':
            for child in parent:
                if child[0] != '_' and self._search_in_regex(string, parent[child], i + 1):
                    result = True
        elif string[i] in parent:
            if self._search_in_regex(string, parent[string[i]], i + 1):
                result = True
        return result
