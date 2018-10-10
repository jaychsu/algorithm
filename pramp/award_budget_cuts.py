"""
Main Concept:

budget = 190
[2, 100, 35, 120, 1000]
=> sort, [1000, 120, 100, 35, 2]
=> total = sum(arr) - budget
=> just treat it as bar chart
   and iterate from start to end to remove the area between `a` and `b`
   from total below
   |-|    -> a
   |=|=|  -> b
   | | |-|
=> untill total < 0 => reach the `cap` line
=> remove the remaining area from total


>>> EPS = 1 ** -3
>>> gotcha = []
>>> for _in, _out in (
...     (([2, 4], 3), 1.5),
...     (([2, 4, 6], 3), 1.0),
...     (([2, 100, 50, 120, 167], 400), 128.0),
...     (([2, 100, 50, 120, 1000], 190), 47.0),
...     (([2, 100, 35, 120, 1000], 190), 51.0),
...     (([21, 100, 50, 120, 130, 110], 140), 23.8),
...     (([210, 200, 150, 193, 130, 110, 209, 342, 117], 1530), 211.0),
... ):
...     res = find_grants_cap(*_in)
...     if abs(res - _out) >= EPS: print(_in, res)
...     gotcha.append(abs(res - _out) < EPS)
>>> bool(gotcha) and all(gotcha)
True
"""


def find_grants_cap(grantsArray, newBudget):
    """
    :type grantsArray: list[int]
    :type newBudget: int
    :rtype: float
    """
    n = len(grantsArray)
    area = sum(grantsArray) - newBudget

    grantsArray.sort(reverse=True)

    i = segment_sum = 0

    while i < n:
        if i == n - 1:
            # (i + 1) * (grantsArray[i] - 0)
            segment_sum = n * grantsArray[i]
        else:
            segment_sum = (i + 1) * (grantsArray[i] - grantsArray[i + 1])

        if area < segment_sum:
            break

        area -= segment_sum
        i += 1

    return grantsArray[i] - area / float(i + 1)
