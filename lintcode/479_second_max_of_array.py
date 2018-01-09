class Solution:
    """
    @param: A: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, A):
        if not A:
            return

        max1 = max2 = float('-inf')
        for a in A:
            if a > max1:
                max2 = max1
                max1 = a
                continue
            if a > max2:
                max2 = a

        return max2
