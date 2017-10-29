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
