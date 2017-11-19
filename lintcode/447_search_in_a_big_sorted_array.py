"""
Test Case:

# if `reader.get(m) == target` when binary searching
# should set the `mid` as the right bound to keep looking for the minimum index
[1,1,1,1,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,11,11,11,11,12,12,12,13,13,13,13,13,14,14,14,14,14,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,18,18,19,19,19,19,20,20,20,20,20,20,20,20,20]
4

# error occurred when `if not reader or not target:`
[0,0,1,1]
0
"""

class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        end = 0
        while reader.get(end) < target:
            # `+1` is to avoid `end == 0`
            end = end * 2 + 1

        l, m, r = 0, 0, end
        while l + 1 < r:
            m = l + (r - l) // 2
            if reader.get(m) < target:
                l = m
            else:
                r = m

        for i in [l, r]:
            if reader.get(i) == target:
                return i
        return -1
