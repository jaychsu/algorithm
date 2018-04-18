class Solution:
    """
    `dp[i]` means `s[:i]` is segmented by words
    """
    def wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        if not s and not words:
            return True
        if not s or not words:
            return False

        max_size = max(len(w) for w in words)
        word_set = set(words)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(1, min(i, max_size) + 1):
                if dp[i - j] and s[i - j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
