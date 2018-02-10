class Solution:
    def multiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b or a == '0' or b == '0':
            return '0'

        m, n = len(a), len(b)
        tmp = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                carry += tmp[i + j + 1] + int(a[i]) * int(b[j])
                tmp[i + j + 1] = carry % 10
                carry //= 10
            tmp[i] = carry

        i = 0
        while tmp[i] == 0:
            i += 1

        return ''.join([str(j) for j in tmp[i:]])
