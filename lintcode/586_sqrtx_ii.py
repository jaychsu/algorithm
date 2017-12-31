class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if not x:
            return x

        left = 0
        right = x if x > 1 else 1
        eps = 1e-10  # the precision needs `1e-8`, check more two digits
        while right - left > eps:
            mid = (left + right) / 2.0
            if mid * mid < x:
                left = mid
            else:
                right = mid

        return left
