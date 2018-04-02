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
