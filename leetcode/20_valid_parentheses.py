class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is '':
            return True
        if not s:
            return False

        P = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
                continue
            if c not in (')', ']', '}'):
                return False
            if not stack or P[c] != stack.pop():
                return False

        return len(stack) == 0
