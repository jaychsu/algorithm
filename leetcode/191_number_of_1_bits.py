class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if not n:
            return ans

        while n != 0:
            n = n & (n - 1)
            ans += 1

        return ans
