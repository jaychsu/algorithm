"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> s = Solution()
>>> for _in, _out in (
...     ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...     ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...     ((['great'], ['great'], []), True),
...     ((['great'], ['fine', 'drama'], pairs), False),
... ):
...     res = s.areSentencesSimilar(*_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


import collections


class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        simils = collections.defaultdict(set)

        for a, b in pairs:
            simils[a].add(b)
            simils[b].add(a)

        for i in range(len(words1)):
            a = words1[i]
            b = words2[i]

            if a != b and b not in simils[a]:
                return False

        return True
