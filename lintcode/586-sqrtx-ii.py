class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        l, m = 0.0, 1.0
        r = 1.0 if x < 1.0 else x
        eps = 1e-12

        while r - l > eps:
            m = l + (r - l) / 2
            if m * m < x:
                l = m
            else:
                r = m

        return l
