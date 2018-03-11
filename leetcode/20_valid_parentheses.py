class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        right2left = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char not in (')', ']', '}'):
                return False
            elif not stack or stack.pop() != right2left[char]:
                return False

        return len(stack) == 0
