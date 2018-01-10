class Solution:
    """
    @param: n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        D = (
            (1000,  'M'),
            ( 900, 'CM'),
            ( 500,  'D'),
            ( 400, 'CD'),
            ( 100,  'C'),
            (  90, 'XC'),
            (  50,  'L'),
            (  40, 'XL'),
            (  10,  'X'),
            (   9, 'IX'),
            (   5,  'V'),
            (   4, 'IV'),
            (   1,  'I'),
        )

        ans = []

        for a, sym in D:
            while n >= a:  # n - a >= 0
                n -= a
                ans.append(sym)

        return ''.join(ans)
