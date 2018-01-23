class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if not n:
            return ans

        i = 5
        while n // i > 0:
            ans += n // i
            i *= 5

        return ans
