class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        if not a:
            return b
        if not b:
            return a

        INT_RANGE = 0xFFFFFFFF

        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= INT_RANGE

        return a if a >> 31 <= 0 else a ^ ~INT_RANGE
