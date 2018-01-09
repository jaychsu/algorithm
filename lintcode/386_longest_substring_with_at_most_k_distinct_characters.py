class Solution:
    """
    @param: s: A string
    @param: k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0

        n = len(s)
        F = {}
        ans = left = right = 0

        while right < n:
            while right < n and (s[right] in F or len(F) < k):
                F[s[right]] = F.get(s[right], 0) + 1
                right += 1

            if right - left > ans:
                ans = right - left

            while left < right and len(F) >= k:
                F[s[left]] -= 1
                if F[s[left]] == 0:
                    del F[s[left]]
                left += 1

        return ans
