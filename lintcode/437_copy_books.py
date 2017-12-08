"""
DP Solution: TLE
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

        INFINITY = float('inf')
        n = len(pages)
        if k > n:
            k = n

        dp = [[0] * k for _ in range(n)]

        for j in range(k):
            dp[0][j] = pages[0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + pages[i]

        for i in range(1, n):
            for j in range(1, k):
                if j > i:
                    dp[i][j] = dp[i][j - 1]
                    continue

                dp[i][j] = INFINITY
                for h in range(j - 1, i + 1):
                    dp[i][j] = min(
                        dp[i][j],
                        max(
                            dp[h][j - 1],
                            dp[i][0] - dp[h][0]
                        )
                    )

        return dp[n - 1][k - 1]


"""
DP Solution
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

        # `dp[i][j]` means the minimum time to assign `i` books to `j` people
        dp = [[0] * k for _ in range(n)]
        i = j = h = 0

        for j in range(k):
            dp[0][j] = pages[0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + pages[i]

        for j in range(1, k):
            for i in range(1, j):
                # if i < j
                # means books more than copiers
                # `j`th people dont have to work
                dp[i][j] = dp[i][j - 1]

            # `h` means the maximum books `j - 1` men copied
            # in the shortest time
            h = 0
            for i in range(j, n):
                # if i >= j
                # 1. find the maximum books `j - 1` men copied
                #    in the shortest time
                while h < i and dp[h][j - 1] < dp[i][0] - dp[h][0]:
                    h += 1

                dp[i][j] = dp[h][j - 1]

                if h == 0:
                    continue

                # 2. check again the `h - 1` books
                dp[i][j] = min(
                    dp[i][j],
                    max(dp[h - 1][j - 1], dp[i][0] - dp[h - 1][0])
                )

        return dp[n - 1][k - 1]


"""
Binary Search
======

1. the minimum spent time, that is `m`,
   locates between `max(pages)` and `sum(pages)` (1 page spent 1 min)
2. the `p` below means possible to finish work,
   if the spent time less than `m`
   and then the `k` people are impossible to finish that
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
        n = len(pages)
        if k > n:
            k = n

        l, m, r = pages[0], 0, 0
        for i in range(n):
            r += pages[i]
            if l < pages[i]:
                l = pages[i]

        while l + 1 < r:
            m = l + (r - l) // 2
            if self.check_if_possible(m, k, pages):
                r = m
            else:
                l = m

        return l if self.check_if_possible(l, k, pages) else r

    def check_if_possible(self, spent_time, max_copiers, pages):
        """
        check if possible to copy all `pages` in `spent_time`
        and participation is not more than `max_copiers`
        """
        copied_pages, copiers = 0, 1

        for i in range(len(pages)):
            if copied_pages + pages[i] > spent_time:
                copied_pages = 0
                copiers += 1
            if copiers > max_copiers:
                return False
            copied_pages += pages[i]

        return True
