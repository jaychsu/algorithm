"""
DP
"""
class Solution:
    """
    @param: s: A string
    @param: D: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, D):
        if s is None or D is None:
            return False

        max_size = 0
        for word in D:
            if len(word) > max_size:
                max_size = len(word)

        D = set(D)  # s in set is O(1)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            end = i
            if max_size < end:
                end = max_size
            for j in range(1, end + 1):
                if not dp[i - j]:
                    continue
                if s[i - j:i] in D:
                    dp[i] = True
                    break

        return dp[n]


"""
two pointer: WRONG

failed at case:
"aaaaaaa"
["aaaa","aaa"]
"""
class Solution:
    """
    @param: S: A string
    @param: D: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, S, D):
        if S is None or D is None:
            return False

        D = set(D)  # s in set is O(1)
        n = len(S)
        start = 0
        for end in range(1, n + 1):
            if S[start:end] not in D:
                continue
            start = end

        return start == n
