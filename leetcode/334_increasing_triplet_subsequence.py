class Solution:
    def increasingTriplet(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False

        a = b = float('inf')

        for x in A:
            if x <= a:
                a = x
            elif x <= b:
                b = x
            else:
                return True

        return False
