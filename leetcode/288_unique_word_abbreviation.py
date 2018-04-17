"""
Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(dictionary)
vwa.isUnique("word")
vwa.isUnique("anotherWord")

Testing:
>>> s = ValidWordAbbr(['deer', 'door', 'cake', 'card'])
>>> all((
...     s.isUnique('dear') is False,
...     s.isUnique('cart') is True,
...     s.isUnique('cane') is False,
...     s.isUnique('make') is True,
... ))
True
"""


class ValidWordAbbr:
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = {}

        for word in dictionary:
            abbr = self.abbreviation(word)
            self.abbrs[abbr] = word

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        return abbr not in self.abbrs

    def abbreviation(self, word):
        if len(word) < 3:
            return word

        cnt = len(word) - 2
        return '{}{}{}'.format(
            word[0],
            str(cnt),
            word[-1]
        )
