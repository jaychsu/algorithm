"""
>>> CASE = (
...     (['AB', [1, 0]], 2),
...     (['ABCD', [1, 2, 3, 0]], 4),
...     (['ABCDE', [4, 3, 2, 0, 1]], 4),
...     (['ABCDE', [0, 3, 4, 0, 2]], -1),
... )
>>> all(card_shuffler(*inpt) == oupt for inpt, oupt in CASE)
True
"""


def card_shuffler(cards, shuffles):
    """
    :type cards: Iterable[str]
    :type shuffles: list[int]
    :rtype: int
    """
    n = len(cards)
    offsets = [0] * n

    for i in range(n):
        offsets[i] = get_offset(i, shuffles)
        if offsets[i] == -1:
            return -1

    return get_lcm(*offsets)


def get_offset(start, shuffles):
    visited = set()
    i = start
    offset = 0

    while i not in visited:
        visited.add(i)
        i = shuffles[i]
        offset += 1

    return offset if i == start else -1


def get_lcm(*nums):
    lcm = nums[0]

    for i in range(1, len(nums)):
        lcm = lcm // get_gcd(lcm, nums[i]) * nums[i]

    return lcm


def get_gcd(a, b):
    while b:
        a, b = b, a % b

    return a
