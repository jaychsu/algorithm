class Solution:
    def findSubstring(self, s, S):
        """
        :type s: str
        :type S: List[str]
        :rtype: List[int]
        """
        ans = []
        if not s or not S or len(s) < len(S) * len(S[0]):
            return ans

        n, m, k = len(s), len(S), len(S[0])
        F = {}
        for c in S:
            F[c] = F.get(c, 0) + 1

        for start in range(k):
            _F = {}
            cnt = 0
            left = start

            for right in range(start, n - k + 1, k):
                sr = s[right:right + k]
                if sr not in F:
                    _F = {}
                    cnt = 0
                    left = right + k
                    continue

                _F[sr] = _F.get(sr, 0) + 1
                if _F[sr] <= F[sr]:
                    cnt += 1
                while _F[sr] > F[sr]:
                    sl = s[left:left + k]
                    if _F[sl] == F[sl]:
                        cnt -= 1
                    _F[sl] -= 1
                    left += k

                if cnt == m:
                    ans.append(left)
                    sl = s[left:left + k]
                    cnt -= 1
                    _F[sl] -= 1
                    left += k

        return ans
