class Solution:
    def inputStream(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str, 'YES' or 'NO'
        """
        if a is None or b is None:
            return 'NO'

        stack = []

        for c in a:
            if c != '<':
                stack.append(c)
            elif stack:
                # c == '<'
                stack.pop()

        _stack = []

        for c in b:
            if c != '<':
                _stack.append(c)
            elif _stack:
                # c == '<'
                _stack.pop()

        return 'YES' if stack == _stack else 'NO'
