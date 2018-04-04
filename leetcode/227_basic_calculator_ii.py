class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = self.to_rpn(s, {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        })

        if not s:
            return 0

        return self.eval_rpn(s, {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b,
        })

    def to_rpn(self, s, P):
        stack, res = [], []

        for i in range(len(s)):
            char = s[i]

            if i > 0 and s[i - 1].isdigit() and char.isdigit():
                res[-1] += char
            elif char.isdigit():
                res.append(char)
            elif char in P:
                while stack and stack[-1] in P and P[char] <= P[stack[-1]]:
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
            elif char in OP:
                b = stack.pop()
                a = stack.pop()
                stack.append(OP[char](a, b))

        return stack[0]


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = self.to_rpn(s)

        if not s:
            return 0

        return self.eval_rpn(s)

    def to_rpn(self, s):
        stack, res = [], []

        for i in range(len(s)):
            char = s[i]

            if i > 0 and s[i - 1].isdigit() and char.isdigit():
                res[-1] += char
            elif char.isdigit():
                res.append(char)
            elif char in '+-*/':
                while stack and stack[-1] in '+-*/':
                    if char in '*/' and stack[-1] in '+-':
                        break
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

    def eval_rpn(self, s):
        stack = []

        for char in s:
            if char.isdigit():
                stack.append(int(char))
            elif char in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                elif char == '/':
                    stack.append(a // b)

        return stack[0]
