import re


class Solution:
    def fractionAddition(self, E):
        """
        :type E: str
        :rtype: str
        """
        S = []  # signs

        if E[0] != '-':
            S.append('+')

        for c in E:
            if c == '+' or c == '-':
                S.append(c)

        a, b = 0, 1
        i = 0
        for frac in re.split('\+|-', E):
            if not frac:
                continue

            _a, _b = frac.split('/')
            _a = int(_a)
            _b = int(_b)

            # if needs to prevent overflow, `// gcd`
            if S[i] == '+':
                a = a * _b + _a * b
            else:
                a = a * _b - _a * b

            b = b * _b

            gcd = self.get_gcd(a, b)
            a //= gcd
            b //= gcd

            i += 1

        return '{}/{}'.format(a, b)

    def get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
