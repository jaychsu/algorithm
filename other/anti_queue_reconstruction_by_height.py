"""
This question is related with `leetcode/406_queue_reconstruction_by_height`
"""


def reorder(nums):
    """
    :type nums: list[int]
    :rtype: list[int]

    >>> reorder([0, 1, 2, 1, 0])
    [4, 2, 1, 3, 5]
    """
    if not nums:
        return []

    n = len(nums)
    ans = [0] * n
    cands = [i for i in range(1, n + 1)]

    for i in range(n - 1, -1, -1):
        ans[i] = cands.pop(i - nums[i])

    return ans
