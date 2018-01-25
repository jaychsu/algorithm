class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        OP = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
        }

        s = self.dal2rpn(s, OP)

        if not s:
            return 0

        return self.eval_rpn(s, OP)

    def dal2rpn(self, s, OP):
        stack, res = [], []

        for i in range(len(s)):
            char = s[i]
            if i > 0 and s[i - 1].isdigit() and char.isdigit():
                res[-1] += char
            elif char.isdigit():
                res.append(char)
            elif char in OP:
                while stack and stack[-1] in OP:
                    res.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()

        while stack:
            res.append(stack.pop())

        return res

    def eval_rpn(self, s, OP):
        stack = []

        for char in s:
            if char.isdigit():
                stack.append(int(char))
                continue
            b = stack.pop()
            a = stack.pop()

            stack.append(int(OP[char](a, b)))

        return stack[0]
