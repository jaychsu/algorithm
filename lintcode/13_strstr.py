"""
Test Case:

["", ""]

["sousource", "e"]

["sousource", "source"]
"""

class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if target == '':
            return 0
        if not source or not target:
            return -1
        m, n = len(source), len(target)
        if m < n:
            return -1

        l = 0
        for r in range(m):
            if source[l:r+1] == target:
                return l
            # if still fit the target
            if source[r] == target[r-l]:
                continue
            # not fit the target, check it
            if source[r] == target[0]:
                # if it equals to the first letter in target,
                # maybe substring appear from here
                l = r
            else:
                # if not fit the previous matched,
                # and its impossible to start a new matched
                # set the left as the next letter
                l = r + 1

        return -1
