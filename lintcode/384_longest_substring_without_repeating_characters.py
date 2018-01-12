class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        ans = 0
        if not s:
            return ans

        n = len(s)
        F = {}
        cnt = left = right = 0

        while right < n:
            F[s[right]] = F.get(s[right], 0) + 1
            if F[s[right]] > 1:
                cnt += 1

            right += 1

            while cnt > 0:
                if F[s[left]] > 1:
                    cnt -= 1
                F[s[left]] -= 1

                left += 1

            if right - left > ans:
                ans = right - left

        return ans
