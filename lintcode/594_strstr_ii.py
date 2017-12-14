"""
Rabin-Karp algorithm

https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

Main Concept:

given S == 'abcde' and T == 'bcd'

1. convert T into hashcode `tcode`
2. iterate S every m chars, and compare with `tcode`,
   continue to add `S[i]` and kick out `S[i - m]`,

    a b c d e
    a b c
      b c d
        c d e

3. so we need to reduce `ord(S[i - m]) * MAGIC_NUMBER ** (m - 1)` every turns
   => calculate `MAGIC_NUMBER ** (m - 1)` in advance to save time
4. if became negative, add `BASE` to back to positive

Test Case:

"abcde"
"e"

"abcdef"
"bcd"
"""


class Solution:
    """
    @param: S: A source string
    @param: T: A target string
    @return: An integer as index
    """
    def strStr2(self, S, T):
        NOT_FOUND = -1
        if S is None or T is None:
            return NOT_FOUND

        if T is '':
            return 0

        n, m = len(S), len(T)

        if m > n:
            return NOT_FOUND

        BASE = 1000000
        MAGIC_NUMBER = 31

        tcode = 0  # the code of T
        top = 1  # top == `MAGIC_NUMBER ** (m - 1)`
        for i in range(m):
            # task 1: get `tcode`
            tcode = (tcode * MAGIC_NUMBER + self._to_int(T[i])) % BASE

            # task 2: get `MAGIC_NUMBER ** (m - 1)`
            if i > 0:
                top = (top * MAGIC_NUMBER) % BASE

        _code = 0
        for i in range(n):
            # kick out `S[i - m]`
            if i >= m:
                _code = (_code - self._to_int(S[i - m]) * top) % BASE

            if _code < 0:
                _code += BASE

            # add `S[i]`
            _code = (_code * MAGIC_NUMBER + self._to_int(S[i])) % BASE

            if _code == tcode and S[i - m + 1:i + 1] == T:
                return i - m + 1

        return NOT_FOUND

    def _to_int(self, char):
        return ord(char) - ord('a')
