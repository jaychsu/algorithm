class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return ''

        # I, V, X, L, C, D, M
        symbs = (
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        )

        ans = []

        for amount, symb in symbs:
            while num >= amount:  # num - amount >= 0
                num -= amount
                ans.append(symb)

        return ''.join(ans)
