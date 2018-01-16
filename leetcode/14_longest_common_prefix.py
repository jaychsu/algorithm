class Solution:
    def longestCommonPrefix(self, S):
        """
        :type S: List[str]
        :rtype: str
        """
        if not S:
            return ''

        """
        i: `i`th char in `S[0]`
        j: `j`th word in `S`
        """
        for i in range(len(S[0])):
            char = S[0][i]
            for j in range(1, len(S)):
                if i >= len(S[j]) or S[j][i] != char:
                    return S[0][:i]

        """
        if process reach here
        means `len(S) == 1 and len(S[0]) == 1`
        """
        return S[0]
