"""
DP: TLE
"""
class Solution:
    """
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, P, k):
        if not P or not k:
            return 0
        n = len(P)
        if n == 1:
            return P[0]

        if k > n:
            k = n

        INFINITY = float('inf')

        """
        `dp[i][j]` means the minimum time to assign `i` books to `j` people
        """
        dp = [[INFINITY] * k for _ in range(n)]

        for j in range(k):
            dp[0][j] = P[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + P[i]

        for i in range(1, n):
            for j in range(1, k):
                if j > i:
                    """
                    if `j > i`, means books more than copiers
                    the people after `j`th people dont have to work
                    """
                    dp[i][j] = dp[i][j - 1]
                    continue

                for h in range(j - 1, i + 1):
                    """
                    `copied_pages` is the maximum copied pages,
                    and also means the maximum time spent
                    by the `j - 1` people before `j`

                    if the `j - 1` people can copy as much as they can
                    then `j`th man will be able to spend less time finishing it
                    """
                    copied_pages = dp[i][0] - dp[h][0]
                    if dp[h][j - 1] > copied_pages:
                        copied_pages = dp[h][j - 1]
                    if copied_pages < dp[i][j]:
                        dp[i][j] = copied_pages

        return dp[n - 1][k - 1]


"""
DP
"""
class Solution:
    """
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, P, k):
        if not P or not k:
            return 0
        n = len(P)
        if n == 1:
            return P[0]

        if k > n:
            k = n

        """
        `dp[i][j]` means the minimum time to assign `i` books to `j` people
        """
        dp = [[0] * k for _ in range(n)]

        for j in range(k):
            dp[0][j] = P[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + P[i]

        for j in range(1, k):
            for i in range(1, j):
                """
                if `j > i`, means books more than copiers
                the people after `j`th people dont have to work
                """
                dp[i][j] = dp[i][j - 1]

            h = copied_pages = 0
            for i in range(j, n):
                """
                `h` means the maximum books `j - 1` men copied in shortest time
                """
                while h < i and dp[h][j - 1] < dp[i][0] - dp[h][0]:
                    h += 1

                dp[i][j] = dp[h][j - 1]

                if h == 0:
                    continue

                """
                check again the `h - 1` books

                `copied_pages` is the maximum copied pages,
                and also means the maximum time spent
                by the `j - 1` people before `j`

                if the `j - 1` people can copy as much as they can
                then `j`th man will be able to spend less time finishing it
                """
                copied_pages = dp[i][0] - dp[h - 1][0]
                if dp[h - 1][j - 1] > copied_pages:
                    copied_pages = dp[h - 1][j - 1]
                if copied_pages < dp[i][j]:
                    dp[i][j] = copied_pages

        return dp[n - 1][k - 1]


"""
Binary Search

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
    @param: P: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, P, k):
        if not P or not k:
            return 0
        n = len(P)
        if n == 1:
            return P[0]

        if k > n:
            k = n

        left = right = P[0]
        for i in range(1, len(P)):
            if P[i] > left:
                left = P[i]

            right += P[i]

        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_if_possible(P, mid, k):
                right = mid
            else:
                left = mid

        """
        MUST check `left` first, since we need the min spent time
        """
        return left if self.check_if_possible(P, left, k) else right

    def check_if_possible(self, P, spent_time, max_copiers):
        """
        check if possible to copy all `pages` in `spent_time`
        and participation is not more than `max_copiers`
        """
        copied_pages, copiers = 0, 1

        for i in range(len(P)):
            """
            if a copier will spend more than `spent_time`
            add one more copier in
            """
            if copied_pages + P[i] > spent_time:
                copied_pages = 0
                copiers += 1
            if copiers > max_copiers:
                return False
            copied_pages += P[i]

        return True
