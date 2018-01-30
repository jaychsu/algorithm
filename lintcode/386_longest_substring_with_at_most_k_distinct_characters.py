class Solution:
    """
    @param: s: A string
    @param: k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        ans = 0
        if not s:
            return ans

        F = {}
        n = len(s)

        cnt = left = right = 0

        while right < n:
            F[s[right]] = F.get(s[right], 0) + 1
            if F[s[right]] == 1:
                cnt += 1

            right += 1

            while cnt > k:
                F[s[left]] -= 1
                if F[s[left]] == 0:
                    cnt -= 1

                left += 1

            if right - left > ans:
                ans = right - left

        return ans
