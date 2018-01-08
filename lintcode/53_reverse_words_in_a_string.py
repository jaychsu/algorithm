class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        s = s.strip()
        if not s:
            return ''

        return ' '.join(reversed(s.split()))
