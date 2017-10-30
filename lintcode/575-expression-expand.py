class Solution:
    """
    @param: s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        stack, strs, c = [], None, ''
        times = number = 0
        for char in s:
            if char.isdigit():
                number = number * 10 ** times + int(char)
                times += 1
            elif char == '[':
                stack.append(number)
                times = number = 0
            elif char == ']':
                # step 0/ s: '5[a2[bc]]'
                # step 1/ stack: [5, a, 2, b, c], strs: []
                # step 2/ stack: [5, a, 2], strs: [c, b]
                # step 3/ stack: [5, a, bcbc], strs: []
                strs = []
                while stack:
                    c = stack.pop()
                    if isinstance(c, int):
                        stack.append(''.join(reversed(strs)) * c)
                        break
                    strs.append(c)
            else:
                stack.append(char)
        return ''.join(stack)
