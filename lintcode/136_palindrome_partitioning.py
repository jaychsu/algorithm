class Solution:
    ans = []
    n = 0
    is_palindrome = None

    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if not s:
            return self.ans

        self.n = len(s)
        self.check_palindrome(s)
        self.dfs(s, 0, [])

        return self.ans

    def check_palindrome(self, s):
        """
        assuming string = 'aabb'
        s: start_index, e: end_index

        `is_palindrome[s][e] == T` means
        the substring(string[s:e+1]) is a palindrome

        the benefit to have the `is_palindrome` in advance is
        we won't need to traverse the whole string again
        when every time we need

            e 0  1  2  3
        s     a  a  b  b
        0 a [[T, T, F, F],
        1 a  [F, T, F, F],
        2 b  [F, F, T, T],
        3 b  [F, F, F, T]]

        and the traversal order to init this matrix is below:
        x: means `start > end`, its impossible

        [[r1, r2, r4, r4],
         [ x, r1, r2, r3],
         [ x,  x, r1, r2],
         [ x,  x,  x, r1]]
        """
        self.is_palindrome = [[False] * self.n for _ in range(self.n)]
        start = end = 0

        # check the diagonal line `r1` and `r2`
        # the traversal order is top-left -> bottom-right, see graph above
        # since the status of `r3`, `r4`, ... depends on that
        for end in range(self.n):
            self.is_palindrome[end][end] = True

            if end > 0:
                start = end - 1
                self.is_palindrome[start][end] = (s[start] == s[end])

        # check the remaining triangle and traverse by line: `r3`, `r4`, ...
        # the traversal order is bottom -> top, see graph above
        # n - 3 = (n - 1) - 2
        # start + 2
        for start in range(self.n - 3, -1, -1):
            for end in range(start + 2, self.n):
                self.is_palindrome[start][end] = (
                    self.is_palindrome[start + 1][end - 1]
                    and s[start] == s[end]
                )

    # traverse all of the possible substring from start
    # if is a palindrome, continue to traverse
    # otherwise will be ignored
    # and catch all result at the end
    def dfs(self, s, start, palindromes):
        if start >= self.n:
            self.ans.append(palindromes)
        next_start = 0
        for end in range(start, self.n):
            if self.is_palindrome[start][end]:
                # `palindromes + [s[start:next_start]]`
                # will create and return new list
                next_start = end + 1
                self.dfs(s, next_start, palindromes + [s[start:next_start]])
