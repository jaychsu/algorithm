class Solution:
    def wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        if s is None or not words:
            return False

        max_size = max(len(word) for word in words)
        word_set = set(words)  # in set is O(1)

        n = len(s)

        """
        `dp[i]` means `s[:i]` is segmented by words
        """
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(1, min(i, max_size) + 1):
                if dp[i - j] and s[i - j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
