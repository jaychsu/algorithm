"""
Test Case

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
        if x < 2:
            return x

        l, m, r = 0, 1, x # l: start, m: middle, r: end

        # `+1` to avoid the comparison at the edge case
        while l + 1 < r:

            # To avoid `(l+r)/2` integer overflow
            m = l + (r - l) // 2

            if m * m < x:
                l = m
            else:
                r = m
            if m * m == x:
                return m

        return l
