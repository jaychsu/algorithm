class Solution:
    def evalRPN(self, E):
        """
        :type E: List[str]
        :rtype: int
        """
        if not E:
            return 0

        stack = []
        operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        for char in E:
            if char not in operation:
                stack.append(int(char))
                continue

            b = stack.pop()
            a = stack.pop()

            stack.append(int(operation[char](a, b)))

        return stack[0]
