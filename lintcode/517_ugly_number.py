class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        if num == 1:
            return True

        for factor in (
            125, 27, 8,
            5, 3, 2,
        ):
            while num % factor == 0:
                num //= factor

            if num == 1:
                return True

        return num == 1
