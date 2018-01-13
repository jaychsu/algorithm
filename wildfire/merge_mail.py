class Solution:
    def merge_mail(self, D):
        C = {}  # companies
        M2C = {}  # mails to companies

        for c, M in D.items():
            self.find(C, c)
            for m in M:
                if m not in M2C:
                    M2C[m] = c
                    continue
                M2C[m] = self.connect(C, c, M2C[m])

        ans = {}
        for k, v in C.items():
            if v not in ans:
                ans[v] = []
            ans[v].append(k)
        return list(ans.values())

    def connect(self, N, a, b):
        _a = self.find(N, a)
        _b = self.find(N, b)
        if _a is not _b:
            N[_a] = _b
        return _b

    def find(self, N, a):
        if a not in N:
            N[a] = a
            return a
        if N[a] is a:
            return a
        N[a] = self.find(N, N[a])
        return N[a]


if __name__ == '__main__':
    CASES = (
        ({
            'A1': ['a1@gmail.com', 'a2@gmail.com'],
            'A2': ['b1@gmail.com', 'a2@gmail.com'],
            'A3': ['c1@gmail.com'],
            'A4': ['c1@gmail.com', 'd1@gmail.com'],
            'A5': ['b1@gmail.com', 'e1@gmail.com'],
        }, [['A1', 'A2', 'A5'], ['A3', 'A4']]),
        ({
            'A1': ['a1@gmail.com', 'a2@gmail.com'],
            'A2': ['b1@gmail.com', 'a2@gmail.com'],
            'A3': ['b1@gmail.com', 'c1@gmail.com'],
            'A4': ['c1@gmail.com', 'd1@gmail.com'],
            'A5': ['b1@gmail.com', 'e1@gmail.com'],
        }, [['A1', 'A2', 'A3', 'A4', 'A5']]),
    )

    s = Solution()
    for input, output in CASES:
        ans = s.merge_mail(input)
        if ans == output:
            print('[OK] passed with case: {}'.format(input))
        else:
            print('[FAIL] failed at case: {}'.format(input))
