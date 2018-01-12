class Solution:
    def findSubstring(self, s, W):
        """
        :type s: str
        :type W: List[str]
        :rtype: List[int]
        """
        ans = []
        if not s or not W or len(s) < len(W) * len(W[0]):
            return ans

        m, n, k = len(s), len(W), len(W[0])
        F = {}
        for w in W:
            F[w] = F.get(w, 0) + 1

        for i in range(k):
            _F = {}
            cnt = 0
            left = i
            for right in range(i, m - k + 1, k):
                _s = s[right:right + k]
                if _s in F:
                    _F[_s] = _F.get(_s, 0) + 1
                    if _F[_s] <= F[_s]:
                        cnt += 1
                    while _F[_s] > F[_s]:
                        __s = s[left:left + k]
                        _F[__s] -= 1
                        left += k
                        if _F[__s] < F[__s]:
                            cnt -= 1
                    if cnt == n:
                        ans.append(left)
                        __s = s[left:left + k]
                        _F[__s] -= 1
                        left += k
                        cnt -= 1
                else:
                    _F = {}
                    cnt = 0
                    left = right + k

        return ans
