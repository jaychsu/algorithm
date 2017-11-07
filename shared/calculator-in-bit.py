class Calculator:
    max_int = 0xFFFFFFFF

    """
    :example: 1 + 5, that is 0001 + 0101
    step1/ no carry(xor): 0001 ^ 0101 == 0100
    step2/ considering carry(and + shift): (0001 & 0101) << 1 == 0010
        the carry only occurs when the same digit is 1
    step3/ repeat (1) and (2) til the result in (2) is 0

    1 + 5 -> 0001 + 0101
    r1: 0001 ^ 0101 == 0100, (0001 & 0101) << 1 == 0010
    r2: 0100 ^ 0010 == 0110, (0100 & 0010) << 1 == 0000
    got 0110 == 6
    """
    # a + b
    # recursion
    @classmethod
    def plus(cls, a, b):
        if not b:
            return a if a >> 31 is 0 else a ^ ~cls.max_int
        return cls.plus((a ^ b) & cls.max_int, (a & b) << 1)

    # a + b
    # iteration
    @classmethod
    def _plus(cls, a, b):
        while b:
            a, b = a ^ b, (a & b) << 1
            a &= cls.max_int
        return a if a >> 31 is 0 else a ^ ~cls.max_int

    # a - b
    # the simplest way is `a + (-b)`
    @classmethod
    def minus(cls, a, b):

        # to get the complement of `b`, that is `-b`
        # -b = ~b + 1
        b = cls.plus(~b, 1)

        return cls.plus(a, b)

    """
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
    # a * b
    @classmethod
    def times(cls, a, b):
        if not a or not b:
            return 0

        # its equivalent to `abs()`
        _a = a if a > 0 else cls.plus(~a, 1)
        _b = b if b > 0 else cls.plus(~b, 1)

        product = 0
        while _b:

            # check the last digit in `b`
            if _b & 1:
                product = cls.plus(product, _a)

            # see diagram above
            # r1/ 1100 * 0
            # r2/ 11000 * 1
            # r3/ 110000 * 0
            # r4/ 1100000 * 1
            _a = _a << 1

            # allow to check last digit
            _b = _b >> 1

        if a ^ b < 0:
            product = cls.plus(~product, 1)
        return product

    # a / b
    @classmethod
    def divide(cls, a, b):
        if not a or not b:
            return 0

        # its equivalent to `abs()`
        _a = a if a > 0 else cls.plus(~a, 1)
        _b = b if b > 0 else cls.plus(~b, 1)

        quotient = 0
        # remainder = 0

        # max_{positive,negative}_int: 2 ** 31
        for i in range(31, -1, -1):

            # avoid to `_a >= _b << i`
            # it may lead to overflow
            # => in origin, _a < _b
            # => in overflow, _a > _b
            if _a >> i >= _b:
                quotient = cls.plus(quotient, 1 << i)
                _a = cls.minus(_a, _b << i)

        # remainder = _a

        if a ^ b < 0:
            quotient = cls.plus(~quotient, 1)
            # remainder = cls.plus(~_a, 1)

        return quotient
