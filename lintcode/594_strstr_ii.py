"""
Rabin-Karp algorithm

https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm


Main Concept:

given S == 'abcde' and T == 'bcd'

1. convert T into hashcode `tcode`
2. iterate S every `n` chars, and compare with `tcode`,
   continue to add `S[i]` and kick out `S[i - n]`,

    a b c d e
    a b c
      b c d
        c d e

3. so we need to reduce `ord(S[i - n]) * MG ** (n - 1)` every turns
   => calculate `MG ** (n - 1)` in advance to save time
4. if became negative, add `MOD` to back to positive

Test Case:

"abcde"
"e"

"abcdef"
"bcd"
"""


class Solution:
    def strStr2(self, S, T):
        """
        :type S: List[str]
        :type T: List[str]
        :rtype: int
        """

        NOT_FOUND = -1

        if S is not None and T is '':
            return 0

        if not S or not T:
            return NOT_FOUND

        m, n = len(S), len(T)
        if n > m:
            return NOT_FOUND

        MOD = 1000000  # hashsize to mod
        MG = 31  # magic number
        A = ord('a')

        p = 1  # `p == MG ** (n - 1)`
        tcode = 0  # the code of T
        for i in range(n):
            tcode = (tcode * MG + ord(T[i]) - A) % MOD

            if i == 0:
                continue
            """
            continue here since p only need `n - 1` times
            """
            p = (p * MG) % MOD

        _code = 0
        for i in range(m):
            """
            kick out `S[i - n]`
            """
            if i >= n:
                _code = (_code - (ord(S[i - n]) - A) * p) % MOD

            if _code < 0:
                _code += MOD

            """
            Add `S[i]`
            """
            _code = (_code * MG + ord(S[i]) - A) % MOD

            if _code == tcode and S[i - n + 1:i + 1] == T:
                return i - n + 1

        return NOT_FOUND
