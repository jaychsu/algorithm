class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        F = {}
        for c in t:
            F[c] = F.get(c, 0) + 1

        n, cnt = len(s), len(F)
        start = size = INFINITY = float('inf')
        left = right = 0

        while right < n:
            if s[right] in F:
                F[s[right]] -= 1
                if F[s[right]] == 0:
                    cnt -= 1

            right += 1

            while cnt == 0:
                if s[left] in F:
                    F[s[left]] += 1
                    if F[s[left]] == 1:
                        cnt += 1

                if right - left < size:
                    size = right - left
                    start = left

                left += 1

        return s[start:start + size] if size < INFINITY else ''
