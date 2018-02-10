class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'

        for _ in range(n - 1):
            res = []
            cnt = 0
            c = ans[0]
            for _c in ans:
                if _c == c:
                    cnt += 1
                    continue
                res.extend((str(cnt), c))
                c = _c
                cnt = 1
            res.extend((str(cnt), c))
            ans = ''.join(res)

        return ans
