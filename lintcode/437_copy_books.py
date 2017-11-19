# REF: https://zhengyang2015.gitbooks.io/lintcode/copy_books_437.html

"""
DP Solution
======

1. `P[i][j]` means the minimum time to assign `i` books to `j` people
2. For the assigned `j`th person, the `h` means
   the number of books assigned to the former `j-1` people.
   That is, the 0 ~ `h` books has been assigned.
3. `P[h][j-1]` means the min cost time from `j-1` people,
   `P[i][0] - P[h][0]` means the spent time for the `j`th person copied the `h+1` ~ `i` books
"""
class Solution:
    """
    @param: pages: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0

        n = len(pages)
        if k > n:
            k = n
        h = 0
        P = [[0 for _ in range(k)] for _ in range(n)]

        P[0][0] = pages[0]
        for i in range(1, n):
            P[i][0] = P[i-1][0] + pages[i]

        for j in range(1, k):
            h = 0
            P[0][j] = pages[0]
            for i in range(1, j):
                P[i][j] = max(P[i-1][j], pages[i])
            for i in range(j, n):
                while h < i and P[h][j-1] < P[i][0] - P[h][0]:
                    h += 1

                # since the final spent time depends on the slower completion
                P[i][j] = max(P[h][j-1], P[i][0] - P[h][0])

                if h > 0:
                    h -= 1

                # find the minimum time
                P[i][j] = min(P[i][j], max(P[h][j-1], P[i][0] - P[h][0]))

        return P[n-1][k-1]


"""
Binary Search
======

1. the minimum spent time, that is `m`, locates between `max(pages)` and `sum(pages)` (1 page spent 1 min)
2. the `p` below means possible to finish work,
   if the spent time less than `m` and then the `k` people are impossible to finish that
      t | ... m-2 m-1 m m+1 m+2 ...
      p | ..F  F   F  T  T   T  T..
"""
class Solution:
    """
    @param: pages: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0

        l, m, r = pages[0], 0, 0
        for i in range(len(pages)):
            r += pages[i]
            if l < pages[i]:
                l = pages[i]

        while l + 1 < r:
            m = l + (r - l) / 2
            if self.neededCopiers(m, pages) <= k:
                r = m
            else:
                l = m

        return l if self.neededCopiers(l, pages) <= k else r

    def neededCopiers(self, spent_time, pages):
        total, copiers = 0, 1

        for i in range(len(pages)):
            if total + pages[i] > spent_time:
                total = 0
                copiers += 1
            total += pages[i]

        return copiers
