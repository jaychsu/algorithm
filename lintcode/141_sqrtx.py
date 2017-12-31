"""
Test Case:

0

1

999999999
"""


class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if not x or x <= 1:
            return x

        left, right = 0, x
        while left + 1 < right:
            mid = (left + right) // 2
            _power = mid * mid

            if _power == x:
                return mid

            if _power < x:
                left = mid
            else:
                right = mid

        return left
