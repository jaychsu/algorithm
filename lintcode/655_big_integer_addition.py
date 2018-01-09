class Solution:
    """
    @param: a: a non-negative integers
    @param: b: a non-negative integers
    @return: return sum of a and b
    """
    def addStrings(self, a, b):
        if not a:
            return b
        if not b:
            return a

        i = len(a) - 1
        j = len(b) - 1
        _carry = 0
        ans = []

        while i >= 0 and j >= 0:
            _carry += ord(a[i]) + ord(b[j]) - 2 * ord('0')
            ans.append(str(_carry % 10))
            _carry //= 10
            i -= 1
            j -= 1

        while i >= 0:
            _carry += ord(a[i]) - ord('0')
            ans.append(str(_carry % 10))
            _carry //= 10
            i -= 1

        while j >= 0:
            _carry += ord(b[j]) - ord('0')
            ans.append(str(_carry % 10))
            _carry //= 10
            j -= 1

        if _carry > 0:
            ans.append(str(_carry))

        return ''.join(reversed(ans))
