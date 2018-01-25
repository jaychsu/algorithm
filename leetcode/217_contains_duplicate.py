class Solution:
    def containsDuplicate(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False

        S = set()

        for a in A:
            if a in S:
                return True
            S.add(a)

        return False
