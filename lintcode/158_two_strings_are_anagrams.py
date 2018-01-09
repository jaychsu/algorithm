class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if s == '' and t == '':
            return True
        if not s or not t:
            return False

        s = sorted(s)
        t = sorted(t)

        return s == t
