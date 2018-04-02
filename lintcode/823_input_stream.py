"""
Merge Sort
time: O(n)
space: O(1)
"""
class Solution:
    def inputStream(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        if a == b == '':
            return RES[1]

        BACK = '<'
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        acnt = bcnt = 0  # count the backspace in both a and b

        while i >= 0 and j >= 0:
            while i >= 0 and (a[i] == BACK or acnt):
                acnt += 1 if a[i] == BACK else -1
                i -= 1
            while j >= 0 and (b[j] == BACK or bcnt):
                bcnt += 1 if b[j] == BACK else -1
                j -= 1

            if a[i] != b[j]:
                return RES[0]

            i -= 1
            j -= 1

        while i >= 0 and (a[i] == BACK or acnt):
            acnt += 1 if a[i] == BACK else -1
            i -= 1
        while j >= 0 and (b[j] == BACK or bcnt):
            bcnt += 1 if b[j] == BACK else -1
            j -= 1

        return RES[int(i == j)]


"""
Stack
time: O(n)
space: O(n)
"""
class Solution:
    def inputStream(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        if a == '' and b == '':
            return RES[1]
        if a is None or b is None:
            return RES[0]

        RM = '<'
        stack = []

        for c in a:
            if c != RM:
                stack.append(c)
            elif stack:
                # c == RM
                stack.pop()

        _stack = []

        for c in b:
            if c != RM:
                _stack.append(c)
            elif _stack:
                # c == RM
                _stack.pop()

        return RES[int(stack == _stack)]
