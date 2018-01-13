class Solution:
    """
    @param: A: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, A):
        """
        `a`: the duplicated num
        `cnt(b)`: the cnt of children less than or equal `b`

        for each `num < a`: `cnt(num) == num`
        for each `num >= a`: `cnt(num) > num`
        """
        left, right = 1, len(A) - 1  # since `len(A) == n + 1`
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_valid(mid, A):
                right = mid
            else:
                left = mid

        return left if self.check_valid(left, A) else right

    def check_valid(self, mid, A):
        cnt = 0
        for a in A:
            if a <= mid:
                cnt += 1
            if cnt > mid:
                return True
        return False


class Solution:
    """
    @param: A: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, A):
        """
        example: [5,4,4,3,2,1]

        i  0, 1, 2, 3, 4, 5
        a  5, 4, 4, 3, 2, 1
        -------------------
           s              f
              f           s
              s  f
                 f     s
                 sf
        -------------------
           f     s
                       s  f
              f  s
                       sf
        """
        if not A:
            return -1

        slow = A[0]
        fast = A[A[0]]

        while slow != fast:
            slow = A[slow]
            fast = A[A[fast]]

        fast = 0

        while slow != fast:
            slow = A[slow]
            fast = A[fast]

        return slow
