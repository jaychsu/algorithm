class Solution:
    """
    @param s: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, s):
        if not s:
            return ''

        return ''.join(sorted(s, key=lambda c: (-s.count(c), c)))
