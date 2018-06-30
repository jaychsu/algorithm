"""
1. Addition

    - go through example: 1 + 5, that is 0001 + 0101

    step1/ no carry(xor): 0001 ^ 0101 == 0100
    step2/ considering carry(and + shift): (0001 & 0101) << 1 == 0010
           the carry only occurs when the same digit is 1
    step3/ repeat (1) and (2) til the result in (2) is 0

    1 + 5 -> 0001 + 0101
    r1: 0001 ^ 0101 == 0100, (0001 & 0101) << 1 == 0010
    r2: 0100 ^ 0010 == 0110, (0100 & 0010) << 1 == 0000
    got 0110 == 6

    - deal with negative values

    if a < 0 and b == 0,
    => a wont be `&` (cannot enter iteration)
    => a >> 31 == -1
    => a ^ ~INT_RANGE got wrong number

    so the simplest way is
    `a >> 31 == 0` -> `a >> 31 <= 0`

2. Subtraction

    the simplest way is `a + (-b)`

    to get the complement of `b`, that is `-b`
    -b = ~b + 1

3. Multiplication

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

    r1/ 1100    * 0 =    0000
    r2/ 11000   * 1 =   11000
    r3/ 110000  * 0 =  000000
    r4/ 1100000 * 1 = 1100000

4. Division

    if a // (2 ** i) >= b:
    => quotient += 2 ** i
    => a -= b * (2 ** i) for next iteration
"""


class Calculator:
    INT_RANGE = 0xFFFFFFFF

    @classmethod
    def _plus(cls, a, b):
        """
        recursion
        """
        if b == 0:
            return a if a >> 31 <= 0 else a ^ ~cls.INT_RANGE

        return cls._plus((a ^ b) & cls.INT_RANGE, (a & b) << 1)

    @classmethod
    def plus(cls, a, b):
        """
        iteration
        """
        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= cls.INT_RANGE

        return a if a >> 31 <= 0 else a ^ ~cls.INT_RANGE

    @classmethod
    def minus(cls, a, b):
        return cls.plus(a, cls.plus(~b, 1))

    @classmethod
    def times(cls, a, b):
        if not a or not b:
            return 0

        x = a if a > 0 else cls.plus(~a, 1)
        y = b if b > 0 else cls.plus(~b, 1)

        product = 0

        while y:
            if y & 1:
                product = cls.plus(product, x)

            x = x << 1
            y = y >> 1

        if a ^ b >= 0:
            return product

        return cls.plus(~product, 1)

    @classmethod
    def divide(cls, a, b):
        if not b:
            return float('inf') if a >= 0 else float('-inf')
        if not a:
            return 0

        x = a if a > 0 else cls.plus(~a, 1)
        y = b if b > 0 else cls.plus(~b, 1)

        quotient = 0

        for i in range(31, -1, -1):
            if x >> i >= y:
                quotient = cls.plus(quotient, 1 << i)
                x = cls.minus(x, y << i)

        if a ^ b >= 0:
            return quotient

        if x == 0:
            return cls.plus(~quotient, 1)

        return ~quotient
