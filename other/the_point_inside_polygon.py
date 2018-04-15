"""
Questions:
1. Choose a random point from one single rectangle.
    => get_random_point_inside_rectangle
2. Choose a random point from multiple rectangles, if there is no overlapping among them.
    => get_random_point_inside_rectangle2
3. Choose a random point from multiple rectangles, if there is overlapping among them.
    => get_random_point_inside_rectangle3
4. Is a point inside polygon?
    => is_point_inside_polygon

* p.s. overlapping means the point
    - was shared between two recs
    - even the point is a vertex or on edge.
"""
import random


def get_random_point_inside_rectangle(rectangle):
    """
    :type rectangle: list[int]
    :rtype: list[int]
    """
    if not rectangle:
        return []

    x1, y1, x2, y2 = rectangle

    return [
        random.randint(x1, x2),
        random.randint(y2, y1),
    ]

# ======


def get_random_point_inside_rectangle2(rectangles):
    """
    :type rectangles: list[list[int]]
    :rtype: list[int]
    """
    if not rectangles:
        return []

    k = total = 0

    for i in range(len(rectangles)):
        x1, y1, x2, y2 = rectangles[i]
        area = (x2 - x1) * (y1 - y2)

        if random.randrange(total + area) >= total:
            k = i

        total += area

    return get_random_point_inside_rectangle(rectangles[k])

# ======


def get_random_point_inside_rectangle3(rectangles):
    """
    :type rectangles: list[list[int]]
    :rtype: list[int]
    """
    if not rectangles:
        return []

# ======


def is_point_inside_polygon(polygon, point):
    """
    :type polygon: list[list[int]]
    :type point: list[int]
    :rtype: bool
    """
    if not polygon or not point or len(polygon) < 3:
        return False

# ======


if __name__ == '__main__':
    import collections

    gotcha = []

    # single-rec
    freq = collections.defaultdict(int)
    for _ in range(10000):
        x, y = get_random_point_inside_rectangle((0, 2, 3, 0))
        freq[x, y] += 1
    gotcha.append(len(freq) == 12)
    gotcha.append(all(633 <= fq <= 1033 for fq in freq.values()))

    # multi-recs, no overlapping
    freq = collections.defaultdict(int)
    for _ in range(10000):
        x, y = get_random_point_inside_rectangle2((
            (0, 2, 1, 0),
            (2, 2, 3, 0),
        ))
        freq[x, y] += 1
    gotcha.append(len(freq) == 12)
    gotcha.append(all(633 <= fq <= 1033 for fq in freq.values()))

    # # multi-recs, overlapping
    # freq = collections.defaultdict(int)
    # for _ in range(100000):
    #     x, y = get_random_point_inside_rectangle3((
    #         (3, 3, 7, -4),
    #         (-4, 5, 1, -2),
    #         (-2, 7, 5, 1),
    #     ))
    #     freq[x, y] += 1
    # gotcha.append(len(freq) == 115)
    # gotcha.append(all(469 <= fq <= 1269 for fq in freq.values()))

    # # multi-recs, overlapping
    # freq = collections.defaultdict(int)
    # for _ in range(100000):
    #     x, y = get_random_point_inside_rectangle3((
    #         (-6, 2, 0, -4),
    #         (-2, 4, 4, -2),
    #         (-4, 6, 2, 0),
    #     ))
    #     freq[x, y] += 1
    # gotcha.append(len(freq) == 101)
    # gotcha.append(all(590 <= fq <= 1390 for fq in freq.values()))

    # for _in, _out in (
    #     (([[0, 0], [10, 0], [10, 10], [0, 10]], [20, 20]), False),
    #     (([[0, 0], [10, 0], [10, 10], [0, 10]], [5, 5]), True),
    #     (([[0, 0], [5, 5], [5, 0]], [3, 3]), False),
    #     (([[0, 0], [5, 5], [5, 0]], [5, 1]), False),
    #     (([[0, 0], [5, 5], [5, 0]], [8, 1]), False),
    #     (([[0, 0], [10, 0], [10, 10], [0, 10]], [-1, 10]), False),
    #     (([[2, 1], [3, 2], [2, 3]], [1, 2]), False),
    #     (([[0, 0], [5, 0], [10, 10], [5, 10]], [3, 3]), True),
    #     (([[0, 0], [5, 0], [10, 10], [5, 10]], [4, 10]), False),
    #     (([[0, 0], [-5, 0], [-10, -10]], [0, -2]), False),
    #     (([[2, 5], [5, 0], [8, 5], [5, 10]], [0, 0]), False),
    #     (([[2, 5], [5, 0], [8, 5], [5, 10]], [5, 5]), True),
    # ):
    #     res = is_point_inside_polygon(*_in)
    #     if res != _out: print(_in, res)
    #     gotcha.append(res == _out)

    print(bool(gotcha) and all(gotcha))
