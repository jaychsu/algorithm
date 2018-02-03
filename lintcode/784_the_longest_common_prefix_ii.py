class Solution:
    """
    @param D: the n strings
    @param target: the target string
    @return: The ans
    """
    def theLongestCommonPrefix(self, D, target):
        ans = 0

        for word in D:
            i = 0
            for c in word:
                if c != target[i]:
                    break
                i += 1
            if i > ans:
                ans = i

        return ans
