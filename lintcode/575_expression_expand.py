class Solution:
    def expressionExpand(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        stack = []
        times = 0

        for c in s:
            if c.isdigit():
                times = times * 10 + int(c)
            elif c == '[':
                stack.append(times)
                times = 0
            elif c == ']':
                tmp = []

                while stack and isinstance(stack[-1], str):
                    tmp.append(stack.pop())

                t = int(stack.pop()) if stack else 1
                stack.append(t * ''.join(reversed(tmp)))
            else:
                stack.append(c)

        return ''.join(stack)
