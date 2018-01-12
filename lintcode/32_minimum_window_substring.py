class Solution:
    """
    @param: s: A string
    @param: t: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, s, t):
        if not s or not t:
            return ''

        n = len(s)
        F = {}
        for c in t:
            F[c] = F.get(c, 0) + 1

        min_size = INFINITY = float('inf')
        min_start = 0
        cnt = len(F)
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
                    if F[s[left]] > 0:
                        cnt += 1

                if right - left < min_size:
                    min_size = right - left
                    min_start = left

                left += 1

        return s[min_start:min_start + min_size] if min_size < INFINITY else ''
