class Solution:
    """
    @param: s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        if not s:
            return ''

        stack = []
        repet = 0  # repetitions

        for char in s:
            if char.isdigit():
                repet = repet * 10 + int(char)
            elif char == '[':
                stack.append(repet)
                repet = 0
            elif char == ']':
                """
                step 0/ s: '5[a2[bc]]'
                step 1/ stack: [5, a, 2, b, c], strs: []
                step 2/ stack: [5, a, 2], strs: [c, b]
                step 3/ stack: [5, a, bcbc], strs: []
                """
                S = []
                while stack:
                    c = stack.pop()
                    if isinstance(c, int):
                        stack.append(''.join(reversed(S)) * c)
                        break
                    S.append(c)
            else:
                stack.append(char)

        return ''.join(stack)
