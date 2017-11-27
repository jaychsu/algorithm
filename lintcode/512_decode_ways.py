"""
Test Case

"0"
"""


class Solution:
    """
    @param: s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if not s:
            return 0

        n = len(s)

        # `F[i]` means the decodings way, and it is sum of
        #   end at `s[i - 1]`
        # + end at `s[i - 2:i]`
        F = [0] * (n + 1)

        # ''
        F[0] = 1

        # the meaning of `0` is same as ''
        F[1] = 1 if int(s[0]) != 0 else 0

        for i in range(2, n + 1):
            if int(s[i - 1]) != 0:
                F[i] = F[i - 1]

            if 10 <= int(s[i - 2:i]) <= 26:
                F[i] += F[i - 2]

        return F[n]
