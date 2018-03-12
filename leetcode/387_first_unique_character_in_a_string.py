class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0

            freq[c] += 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
