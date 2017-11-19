class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        self.map = {}
        n = 0
        for key in dict:
            n = len(key)
            for l in range(n):
                for r in range(l + 1, n + 1):
                    substr = key[l:r]
                    if substr not in self.map:
                        self.map[substr] = [key]
                    elif self.map[substr][-1] != key:
                        self.map[substr].append(key)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        if str in self.map:
            return self.map[str]
        return []


# Solution2
'''
This solution does not meet the demand.
Since the description said 'return all words that contains the string as a substring.'

But its a good solution for the auto-completion
'''
class Trie:
    def __init__(self):
        self.root = self.new_node()

    def new_node(self):
        return {
            'result': [],
            'children': {}
        }

    def put(self, key):
        if not key:
            return
        for word in key.split():
            self._put(word, key)

    def _put(self, word, key):
        parent = self.root
        for char in word.lower():
            if char not in parent['children']:
                parent['children'][char] = self.new_node()
            parent = parent['children'][char]
            parent['result'].append(key)

    def search(self, key):
        if not key:
            return []
        parent = self.root
        for char in key.lower():
            if char not in parent['children']:
                return []
            parent = parent['children'][char]
        return parent['result']

    # To support search with 2+ word
    # def search(self, key):
    #     if not key:
    #         return []
    #     result = []
    #     for word in key.split():
    #         result += self._search(word)
    #     return result
    # def _search(self, word):
    #     parent = self.root
    #     for char in word.lower():
    #         if char not in parent['children']:
    #             return []
    #         parent = parent['children'][char]
    #     return parent['result']

class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        self.trie = Trie()
        for word in dict:
            self.trie.put(word)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        return self.trie.search(str)
