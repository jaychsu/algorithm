class Solution:
    """
    @param: dividend: the dividend
    @param: divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        INT_MAX = 0x7FFFFFFF
        if not divisor:
            return INT_MAX
        if not dividend:
            return 0

        _a = dividend if dividend > 0 else - dividend
        _b = divisor if divisor > 0 else - divisor
        quotient = 0

        for i in range(31, -1, -1):
            if _a >> i >= _b:
                quotient += 1 << i
                _a -= _b << i

        if dividend ^ divisor < 0:
            quotient = ~quotient + 1

        return quotient if quotient < INT_MAX else INT_MAX
