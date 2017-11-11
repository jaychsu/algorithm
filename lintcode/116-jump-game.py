# https://leetcode.com/articles/jump-game/
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return False

        # the last position to get to the destination
        last_p = len(A) - 1

        for i in range(last_p, -1, -1):
            # if:
            # `i` (the distance from the starting position)
            # + `A[i]` (the maximum jump length)
            # is great than `last_p` (the last position to get to the destination)
            # and then we can reach the `last_p` if we at `i`
            if i + A[i] >= last_p:
                last_p = i

        return last_p == 0
