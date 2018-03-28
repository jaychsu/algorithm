def card_shuffler(cards, shuffle):
    """
    :type cards: Iterable[str]
    :type shuffle: list[int]
    :rtype: int

    >>> CASE = (
    ...     (['AB', [1, 0]], 2),
    ...     (['ABCD', [1, 2, 3, 0]], 4),
    ...     (['ABCDE', [4, 3, 2, 0, 1]], 4),
    ...     (['ABCDE', [0, 3, 4, 0, 2]], -1),
    ... )

    >>> all(card_shuffler(*inpt) == oupt for inpt, oupt in CASE)
    True
    """
    n = len(cards)
    offsets = [0] * n

    for i in range(n):
        offsets[i] = get_offset(i, shuffle)
        if offsets[i] == -1:
            return -1

    return get_lcm(*offsets)

def get_offset(start, shuffle):
    i = shuffle[start]
    visited = set([i])
    offset = 1

    while i != start:
        i = shuffle[i]
        if i in visited:
            return -1
        visited.add(i)
        offset += 1

    return offset

def get_lcm(*nums):
    lcm = nums[0]

    for i in range(1, len(nums)):
        lcm = lcm * nums[i] // get_gcd(lcm, nums[i])

    return lcm

def get_gcd(a, b):
    while b:
        a, b = b, a % b

    return a
