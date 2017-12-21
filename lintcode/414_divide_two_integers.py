class Solution:
    """
    @param: a: the dividend
    @param: b: the divisor
    @return: the result
    """
    def divide(self, a, b):
        INT_MAX = 0x7FFFFFFF

        if not b:
            return INT_MAX
        if not a:
            return 0

        _a = a if a > 0 else -a
        _b = b if b > 0 else -b

        quotient = 0

        for i in range(31, -1, -1):
            if _a >> i >= _b:
                quotient += 1 << i
                _a -= _b << i

        if a ^ b < 0:
            quotient = ~quotient + 1

        return quotient if quotient < INT_MAX else INT_MAX
