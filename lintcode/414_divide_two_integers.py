class Solution:
    """
    @param: a: the dividend
    @param: b: the divisor
    @return: the result
    """
    def divide(self, a, b):
        INT_MAX = 0x7FFFFFFF
        ans = 0

        if not b:
            return INT_MAX
        if not a:
            return ans

        _a = -a if a < 0 else a
        _b = -b if b < 0 else b

        for i in range(31, -1, -1):
            """
            let `ci = 1 << i = 2 ** i`
            if `_a // _b >= ci`, that is `_a // ci >= _b`
            => `(_a - _b * ci) // _b >= 0`, and `ans += ci`

            start to approch `_a' // _b >= ci'`
            where _a' = _a - _b * ci, i' = i - 1
            """
            if (_a >> i) < _b:
                continue
            ans += 1 << i
            _a -= _b << i

        if a ^ b < 0:
            ans = ~ans + 1

        return ans if ans < INT_MAX else INT_MAX
