class Calculator:
    INT_RANGE = 0xFFFFFFFF

    """
    a + b

    example: 1 + 5, that is 0001 + 0101
    step1/ no carry(xor): 0001 ^ 0101 == 0100
    step2/ considering carry(and + shift): (0001 & 0101) << 1 == 0010
           the carry only occurs when the same digit is 1
    step3/ repeat (1) and (2) til the result in (2) is 0

    1 + 5 -> 0001 + 0101
    r1: 0001 ^ 0101 == 0100, (0001 & 0101) << 1 == 0010
    r2: 0100 ^ 0010 == 0110, (0100 & 0010) << 1 == 0000
    got 0110 == 6
    """
    """
    recursion
    """
    @classmethod
    def _plus(cls, a, b):
        if b == 0:
            return a if a >> 31 <= 0 else a ^ ~cls.INT_RANGE
        return cls._plus((a ^ b) & cls.INT_RANGE, (a & b) << 1)

    """
    iteration
    """
    @classmethod
    def plus(cls, a, b):
        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= cls.INT_RANGE

        """
        if a < 0 and b == 0,
        => a wont be `&` (cannot enter iteration)
        => a >> 31 == -1
        => a ^ ~INT_RANGE got wrong number

        so the simplest way is
        `a >> 31 == 0` -> `a >> 31 <= 0`
        """
        return a if a >> 31 <= 0 else a ^ ~cls.INT_RANGE

    """
    a - b

    the simplest way is `a + (-b)`
    """
    @classmethod
    def minus(cls, a, b):
        """
        to get the complement of `b`, that is `-b`
        -b = ~b + 1
        """
        b = cls.plus(~b, 1)

        return cls.plus(a, b)

    """
    a * b

    in oct   | in bin
      a  12  |   a  1100
    x b  10  | x b  1010
    -------- | ----------
         00  |      0000
        12   |     1100
    -------- |    0000
        120  |   1100
             | ----------
             |   1111000
    """
    @classmethod
    def times(cls, a, b):
        if not a or not b:
            return 0

        """
        its equivalent to `abs()`
        """
        _a = a if a > 0 else cls.plus(~a, 1)
        _b = b if b > 0 else cls.plus(~b, 1)

        product = 0
        while _b:
            """
            check the last digit in `b`
            """
            if _b & 1:
                product = cls.plus(product, _a)

            """
            r1/ 1100    * 0 =    0000
            r2/ 11000   * 1 =   11000
            r3/ 110000  * 0 =  000000
            r4/ 1100000 * 1 = 1100000
            """
            _a = _a << 1

            """
            allow to check last digit in next iteration
            """
            _b = _b >> 1

        if a ^ b < 0:
            product = cls.plus(~product, 1)

        return product

    """
    a / b

    let `ci = 1 << i = 2 ** i`
    if `_a // _b >= ci`, that is `_a // ci >= _b`
    => `(_a - _b * ci) // _b >= 0`, and `ans += ci`

    start to approch `_a' // _b >= ci'`
    where _a' = _a - _b * ci, i' = i - 1
    """
    @classmethod
    def divide(cls, a, b):
        if not b:
            return float('inf') if a >= 0 else float('-inf')
        if not a:
            return 0

        """
        its equivalent to `abs()`
        """
        _a = a if a > 0 else cls.plus(~a, 1)
        _b = b if b > 0 else cls.plus(~b, 1)

        quotient = 0

        """
        the upper limit of int: 2 ** 31
        """
        for i in range(31, -1, -1):
            """
            avoid to `_a >= _b << i`
            it may lead to overflow
            => in origin, _a < _b
            => in overflow, _a > _b
            """
            if _a >> i >= _b:
                """
                a << i == a * (2 ** i)
                a >> i == a // (2 ** i)
                """
                quotient = cls.plus(quotient, 1 << i)
                """
                continue to use the divisor(b) to reduce the dividend(a)
                until the dividend(a) is less than the divisor(b)
                """
                _a = cls.minus(_a, _b << i)

        if a ^ b >= 0:
            return quotient

        """
        remainder = _a

        if `a ^ b < 0`, that is `a // b < 0`
        if no remainder, just return `-quotient`, that is `~quotient + 1`
        otherwise need to floor `quotient`, that is `~quotient`
        """
        if _a == 0:
            return cls.plus(~quotient, 1)
        else:
            return ~quotient
