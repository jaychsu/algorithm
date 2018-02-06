class Solution:
    def longestCommonPrefix(self, S):
        """
        :type S: List[str]
        :rtype: str
        """
        if not S:
            return ''

        for i in range(len(S[0])):
            for word in S:
                if i >= len(word) or word[i] != S[0][i]:
                    return S[0][:i]

        return S[0]
