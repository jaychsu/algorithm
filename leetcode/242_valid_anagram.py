class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False

        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1

        for f in freq.values():
            if f != 0:
                return False

        return True
