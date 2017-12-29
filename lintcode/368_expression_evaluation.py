"""
REF: [Reverse Polish Notation](https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95)
REF: [Direct Algebraic Logic to Reverse Polish Notation](http://blog.csdn.net/sgbfblog/article/details/8001651)
"""


class Solution:
    P = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    """
    @param: E: a list of strings
    @return: an integer
    """
    def evaluateExpression(self, E):
        if not E:
            return 0

        E = self.dal2rpn(E)

        """
        for cases like `["(","(","(","(","(",")",")",")",")",")"]`
        """
        if not E:
            return 0

        return self.eval_rpn(E)

    def dal2rpn(self, E):
        """
        `stack` to save operators and brackets temply
        `res` is the RPN of `E`, to save digits and operators
        """
        stack, res = [], []

        for char in E:
            if char.isdigit():
                """
                if its digit
                then directly output
                """
                res.append(char)
                continue

            if char in self.P:
                """
                if `stack` is not empty
                and `stack[-1]` is an operator
                and its priority is higher or same ('*' == '/' > '+' == '-')
                then pop and output
                """
                while (stack and stack[-1] in self.P and
                       self.P[stack[-1]] >= self.P[char]):
                    res.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                """
                if its ')'
                then continue to pop and output
                until meet '('
                """
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()  # evict '('

        """
        output the remaining in `stack`
        """
        while stack:
            res.append(stack.pop())

        return res

    def eval_rpn(self, E):
        stack = []
        for char in E:
            if char.isdigit():
                """
                if its digit
                then temply save in `stack`
                """
                stack.append(int(char))
                continue

            """
            the first poped one is base,
            otherwise there is error occurred when '/' and '-'
            """
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
