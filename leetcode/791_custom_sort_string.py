class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        return ''.join(sorted(T, key=lambda c: S.find(c)))
