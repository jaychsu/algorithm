class Solution:
    def addStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return ''
        if not a:
            return b
        if not b:
            return a

        m, n = len(a), len(b)
        idx = max(m, n)
        ans = [''] * (idx + 1)

        i = m - 1
        j = n - 1
        carry = 0
        zero = ord('0')

        while i >= 0 and j >= 0:
            carry += ord(a[i]) + ord(b[j]) - 2 * zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1
            j -= 1

        while i >= 0:
            carry += ord(a[i]) - zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            i -= 1

        while j >= 0:
            carry += ord(b[j]) - zero
            ans[idx] = str(carry % 10)
            carry //= 10
            idx -= 1
            j -= 1

        if carry:
            ans[0] = str(carry)
        else:
            ans = ans[1:]

        return ''.join(ans)
