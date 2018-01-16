class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'

        for _ in range(n - 1):
            S = []
            _s = s[0]
            cnt = 0
            for c in s:
                if c == _s:
                    cnt += 1
                    continue
                S.append(str(cnt))
                S.append(_s)
                _s = c
                cnt = 1
            S.append(str(cnt))
            S.append(_s)
            s = ''.join(S)

        return s
