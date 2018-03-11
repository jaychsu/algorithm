class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        ans = 0

        if not n:
            return ans

        while n != 0:
            n = n & (n - 1)
            ans += 1

        return ans
