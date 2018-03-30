"""
Problem: https://www.geeksforgeeks.org/snake-ladder-problem-2/
"""


def get_min_dice_throws(moves):
    """
    :type moves: list[int]
    :type n: int
    :rtype: int

    >>> moves = [-1] * 30
    >>> for i, val in (
    ...     # ladders
    ...     ( 2, 21),
    ...     ( 4,  7),
    ...     (10, 25),
    ...     (19, 28),
    ...     # snakes
    ...     (26,  0),
    ...     (20,  8),
    ...     (16,  3),
    ...     (18,  6),
    ... ):
    ...     moves[i] = val
    >>> get_min_dice_throws(moves)
    3
    """
    if not moves:
        return -1

    n = len(moves)
    queue, _queue = [0], []
    steps = {0: 0}  # min steps to get i

    while queue:
        for i in queue:
            for j in range(i + 1, min(i + 7, n)):
                # 6-faced dice => max 6 steps but up to n
                if j == n - 1:
                    return steps[i]

                if j in steps:
                    # is visited
                    continue

                # next cell
                k = moves[j] if moves[j] != -1 else j
                steps[k] = steps[i] + 1
                _queue.append(k)

        queue, _queue = _queue, []

    return -1
