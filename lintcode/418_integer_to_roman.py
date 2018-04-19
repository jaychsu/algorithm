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
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        )

        ans = []

        for symb, amount in symbs:
            if not num:
                break

            while num >= amount:  # num - amount >= 0
                num -= amount
                ans.append(symb)

        return ''.join(ans)
