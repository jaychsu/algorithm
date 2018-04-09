"""
Main Concept:
1.


REF:
1. http://marcodiiga.github.io/point-in-polygon-problem
2. https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon
3. http://www.ariel.com.au/a/python-point-int-poly.html


TODO:
1. design api
2. pass the logic code


Testing:

gotcha = []

for _in, _out in (
    (([[0, 0], [10, 0], [10, 10], [0, 10]], [20, 20]), False),
    (([[0, 0], [10, 0], [10, 10], [0, 10]], [5, 5]), True),
    (([[0, 0], [5, 5], [5, 0]], [3, 3]), False),
    (([[0, 0], [5, 5], [5, 0]], [5, 1]), False),
    (([[0, 0], [5, 5], [5, 0]], [8, 1]), False),
    (([[0, 0], [10, 0], [10, 10], [0, 10]], [-1, 10]), False),
    (([[2, 1], [3, 2], [2, 3]], [1, 2]), False),
    (([[0, 0], [5, 0], [10, 10], [5, 10]], [3, 3]), True),
    (([[0, 0], [5, 0], [10, 10], [5, 10]], [4, 10]), False),
    (([[0, 0], [-5, 0], [-10, -10]], [0, -2]), False),
    (([[2, 5], [5, 0], [8, 5], [5, 10]], [0, 0]), False),
    (([[2, 5], [5, 0], [8, 5], [5, 10]], [5, 5]), True),
):
    res = is_point_inside_polygon(*_in)
    if res != _out: print(_in, res)
    gotcha.append(res == _out)

bool(gotcha) and all(gotcha)
True
"""


def is_point_inside_polygon(polygon, point):
    """
    :type polygon: list[list[int]]
    :type point: list[int]
    :rtype: bool
    """
    if not polygon or not point or len(polygon) < 3:
        return False

    n = len(polygon)
    inf = (float('inf'), point[1])
    cnt = 0  # count for intersection
    same_y_points = set()

    for i in range(n):
        j = (i + 1) % n

        if any((
            not _is_intersected(point, inf, polygon[i], polygon[j]),
            tuple(polygon[i]) in same_y_points,
            tuple(polygon[j]) in same_y_points,
        )):
            continue

        cnt += 1

        if point[1] == polygon[i][1]:
            same_y_points.add(tuple(polygon[i]))
        if point[1] == polygon[j][1]:
            same_y_points.add(tuple(polygon[j]))
        if _orientation(polygon[i], polygon[j], point) != 0:
            continue
        if _is_on_segment(polygon[i], polygon[j], point):
            return True

        _i = (i - 1) % n
        _j = (j + 1) % n

        if any((
            polygon[_i][1] <= polygon[i][1] and polygon[_j][1] <= polygon[j][1],
            polygon[_i][1] >= polygon[i][1] and polygon[_j][1] >= polygon[j][1],
        )):
            cnt -= 1

    return cnt & 1 != 0


def _orientation(a, b, c):
    """
    To find orientation of ordered triplet (a, b, c).
    @return 0 => a, b and c are colinear
    @return 1 => Clockwise
    @return -1 => Counterclockwise

    :type a: list[int]
    :type b: list[int]
    :type c: list[int]
    :rtype: int
    """
    val = (b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])

    if val > 0:
        return 1
    if val < 0:
        return -1

    return 0


def _is_on_segment(a, b, c):
    """
    Given three colinear points a, b, c,
    this function checks if point c lies on line segment 'ab'

    :type a: list[int]
    :type b: list[int]
    :type c: list[int]
    :rtype: bool
    """
    return (
        min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
        min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
    )


def _is_intersected(a, b, c, d):
    """
    The function that returns true
    if line segment 'ab' and 'cd' intersect.

    :type a: list[int]
    :type b: list[int]
    :type c: list[int]
    :type d: list[int]
    :rtype: bool
    """
    e = _orientation(a, b, c)
    f = _orientation(a, b, d)
    g = _orientation(c, d, a)
    h = _orientation(c, d, b)

    if e != f and g != h:
        return True

    if e == 0 and _is_on_segment(a, b, c):
        return True
    if f == 0 and _is_on_segment(a, b, d):
        return True
    if g == 0 and _is_on_segment(c, d, a):
        return True
    if h == 0 and _is_on_segment(c, d, b):
        return True

    return False
