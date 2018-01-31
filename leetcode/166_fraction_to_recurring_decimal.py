class Solution:
    def fractionToDecimal(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        if not b:
            return ''
        if not a:
            return '0'

        ans = []
        if a ^ b < 0:
            ans.append('-')

        if a < 0:
            a = -a
        if b < 0:
            b = -b

        ans.append(str(a // b))

        a %= b
        if a == 0:
            return ''.join(ans)

        ans.append('.')
        D = {a: len(ans)}  # the index of first occurrence of `a`
        while a:
            a *= 10
            ans.append(str(a // b))
            a %= b

            if a in D:
                ans.insert(D[a], '(')
                ans.append(')')
                break

            D[a] = len(ans)

        return ''.join(ans)
