"""
Main Concept
    ver. | 1 2 3 4 5
    good | T T F F F

class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


class Solution:
    def findFirstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return left if isBadVersion(left) else right
