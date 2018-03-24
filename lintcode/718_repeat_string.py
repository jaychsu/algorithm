class Solution:
    def repeatedString(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(b) <= len(a) and b in a:
            return 1
        if not a or not b:
            return -1

        ans = b.count(a)
        c = b.split(a)

        if c[0] and a.endswith(c[0]):
            ans += 1

        if c[-1] and a.startswith(c[-1]):
            ans += 1

        return ans if a.startswith(c[-1]) and a.endswith(c[0]) else -1
