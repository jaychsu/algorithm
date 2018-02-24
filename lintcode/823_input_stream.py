class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, a, b):
        A = []

        for c in a:
            if c == '<':
                if A: A.pop()
            else:
                A.append(c)

        B = []

        for c in b:
            if c == '<':
                if B: B.pop()
            else:
                B.append(c)

        return 'YES' if A == B else 'NO'
