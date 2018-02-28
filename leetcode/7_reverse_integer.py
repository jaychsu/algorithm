class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if not x:
            return ans

        INT_MAX = 0x7FFFFFFF
        _x = x if x > 0 else -x

        while _x:
            ans = ans * 10 + _x % 10
            _x //= 10

        if ans >= INT_MAX:
            return 0

        return ans if x > 0 else -ans
