"""
>>> gotcha = []
>>> for _in, _out in (
...     ((4, 2), 2),
...     ((9, 3), 2.08),
...     ((7, 3), 1.913),
...     ((11, 4), 1.821),
... ):
...     res = root(*_in)
...     valid = abs(res - _out) < 0.001
...     if not valid: print(_in, res)
...     gotcha.append(valid)
>>> bool(gotcha) and all(gotcha)
True
"""


def root(x, n):
    if not x or x in (0, 1):
        return x

    left = 0
    right = max(1, x)

    while right - left > 1e-4:
        mid = (left + right) / 2.0
        product = get_product(mid, n)

        if product < x:
            left = mid
        elif product > x:
            right = mid
        else:
            return mid

    return (left + right) / 2.0


def get_product(x, n):
    res = 1

    for _ in range(n):
        res *= x

    return res
