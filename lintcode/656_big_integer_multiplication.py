class Solution:
    """
    @param: A: a non-negative integers
    @param: B: a non-negative integers
    @return: return product of A and B
    """
    def multiply(self, A, B):
        if not A or not B or A == '0' or B == '0':
            return '0'

        m, n = len(A), len(B)
        tmp = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            carry = 0
            for j in range(n - 1, -1, -1):
                product = carry + tmp[i + j + 1] + int(A[i]) * int(B[j])
                tmp[i + j + 1] = product % 10
                carry = product // 10
            tmp[i] = carry

        i = 0
        while tmp[i] == 0:
            i += 1

        return ''.join([str(a) for a in tmp[i:]])
