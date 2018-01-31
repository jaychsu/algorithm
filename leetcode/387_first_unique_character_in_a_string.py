class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        F = {}
        for c in s:
            F[c] = F.get(c, 0) + 1

        i = 0
        for c in s:
            if F[c] == 1:
                return i
            i += 1

        return -1
