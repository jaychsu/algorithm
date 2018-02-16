class Solution:
    def sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x or x <= 1:
            return x

        left, right = 0, x

        while left + 1 < right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid

            if square < x:
                left = mid
            else:
                right = mid

        return left
