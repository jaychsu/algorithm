"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        """
        ver. | 1 2 3 4 5
        good | T T F F F
        """
        if not n:
            return
        l, m, r = 1, 1, n
        while l + 1 < r:
            m = l + (r - l) / 2
            if SVNRepo.isBadVersion(m):
                r = m
            else:
                l = m
        return l if SVNRepo.isBadVersion(l) else r
