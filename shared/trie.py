class Trie:
    def __init__(self):
        self.root = self._new_node()

    def put(self, key):
        if not key:
            return
        parent = self.root
        for char in key:
            if char not in parent['children']:
                parent['children'][char] = self._new_node()
            parent = parent['children'][char]
        parent['end_of'] = key

    def has_key(self, key):
        if not key:
            return False
        return self._search(key) is key

    def has_prefix(self, key):
        if not key:
            return False
        return self._search(key) is not False

    def get_node(self, char, parent=None):
        if not parent:
            parent = self.root
        if char in parent['children']:
            return parent['children'][char]

    def _search(self, key):
        parent = self.root
        for char in key:
            if char not in parent['children']:
                return False
            parent = parent['children'][char]
        return parent['end_of']

    def _new_node(self):
        return {
            'end_of': '',
            'children': {}
        }

    def __repr__(self):
        return repr(self.root)
