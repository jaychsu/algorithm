"""
Main Concept:
1. find the max and do `flip` in [0,max_idx]
2. the max is already at `0`, `flip` it to the correct pos
3. repeat (1)

   [1,5,2,4,3]
=> [5,1,2,4,3]
=> [3,4,2,1,5]
=> [4,3,2,1,5]
=> [1,2,3,4,5]

Testing:
>>> gotcha = []
>>> for _in, _out in (
...     (([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5]),
...     (([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5]),
...     (([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1]),
...     (([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1]),
... ):
...     flip(*_in)
...     if _in[0] != _out: print(_in, _out)
...     gotcha.append(_in[0] == _out)
>>> bool(gotcha) and all(gotcha)
True
>>> gotcha = []
>>> for _in, _out in (
...     ([1, 5, 4, 3, 2], [1, 2, 3, 4, 5]),
...     ([5, 1, 3, 4, 2], [1, 2, 3, 4, 5]),
...     ([1, 4, 2, 3, 5], [1, 2, 3, 4, 5]),
...     ([5, 10, 1, 20, 4], [1, 4, 5, 10, 20]),
...     ([5, 1, 4, 20, 10], [1, 4, 5, 10, 20]),
... ):
...     res = pancake_sort(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


def pancake_sort(nums):
    """using `flip` to sort input in order
    :type nums: list[int]
    :rtype: list[int]
    """
    for j in range(len(nums) - 1, -1, -1):
        i = get_max_index(nums, j)
        flip(nums, i + 1)
        flip(nums, j + 1)

    return nums


def flip(nums, k):
    """reverses the order of the first `k` elements in the array `nums` place
    :type nums: list[int]
    :type k: int
    :rtype: void
    """
    if not nums:
        return

    if not k or k <= 1:
        return

    k = min(k, len(nums))
    i, j = 0, k - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def get_max_index(nums, i):
    """return the index of the maximum in [0,i] of `nums`
    :type nums: list[int]
    :type i: int
    :rtype: int
    """
    k = 0

    for j in range(1, i + 1):
        if nums[j] > nums[k]:
            k = j

    return k
