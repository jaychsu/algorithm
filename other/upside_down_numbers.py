def find_upside_down_numbers(n):
    """
    :type n: int
    :rtype: list[int]

    >>> gotcha = []
    >>> for _in, _out in (
    ...     (10, [1, 6, 8, 9]),
    ...     (100, [1, 6, 8, 9, 16, 18, 19, 61, 66, 68, 81, 86, 89, 91, 98, 99]),
    ...     (500, [1, 6, 8, 9, 16, 18, 19, 61, 66, 68, 81, 86, 89, 91, 98, 99, 161, 191]),
    ...     (700, [1, 6, 8, 9, 16, 18, 19, 61, 66, 68, 81, 86, 89, 91, 98, 99, 161, 169, 189, 191, 199, 611, 661, 669, 681]),
    ... ):
    ...     res = find_upside_down_numbers(_in)
    ...     if res != _out: print(_in, res)
    ...     gotcha.append(res == _out)
    >>> bool(gotcha) and all(gotcha)
    True
    """
    ans = []

    if not n or n <= 0:
        return ans

    cands = '01689'
    queue, _queue = ['1', '6', '8', '9'], []
    up_down_nums = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6',
    }

    while queue:
        ans.extend(queue)

        for num in queue:
            for nxt in cands:
                res = num + nxt
                rev = get_reversed_number(res, up_down_nums)

                if rev[0] == '0' or res == rev or int(rev) > n:
                    continue

                if int(res) > n:
                    ans.extend(_queue)
                    return [int(s) for s in ans]

                _queue.append(res)

        queue, _queue = _queue, []

    return [int(s) for s in ans]


def get_reversed_number(s, up_down_nums):
    res = ''

    for i in range(len(s) - 1, -1, -1):
        res += up_down_nums[s[i]]

    return res
