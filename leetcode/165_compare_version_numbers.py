class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 and not version2:
            return 0
        if not version1:
            return -1
        if not version2:
            return 1

        v = version1.split('.')
        w = version2.split('.')
        m, n = len(v), len(w)

        for i in range(max(m, n)):
            a = self.get_int(v[i]) if i < m else 0
            b = self.get_int(w[i]) if i < n else 0

            if a < b:
                return -1
            elif a > b:
                return 1

        return 0

    def get_int(self, s):
        if not s or not s.isdigit():
            return 0

        res = 0
        zero = ord('0')

        for c in s:
            res = res * 10 + ord(c) - zero

        return res
