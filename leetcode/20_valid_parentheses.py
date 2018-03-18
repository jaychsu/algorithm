class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in '([{':
                stack.append(c)
            elif c not in ')]}':
                return False
            elif not stack or pairs[c] != stack.pop():
                return False

        return not stack
