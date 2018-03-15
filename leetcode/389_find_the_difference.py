class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = ord('a')
        ans = ord(t[-1]) - a

        for i in range(len(s)):
            ans ^= ord(s[i]) - a
            ans ^= ord(t[i]) - a

        return chr(ans + a)


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t:
            return ''

        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0

            freq[c] += 1

        for c in t:
            if c not in freq:
                return c

            freq[c] -= 1

        for c, cnt in freq.items():
            if cnt:
                return c

        return ''
