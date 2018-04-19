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
...     res = flip(*_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
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


def flip(nums, k):
    """reverses the order of the first `k` elements in the array `nums`
    :type nums: list[int]
    :type k: int
    :rtype: list[int]
    """
    if not nums:
        return []

    if not k or k <= 1:
        return nums

    if k > len(nums):
        k = len(nums)

    left, right = 0, k - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def pancake_sort(nums):
    """using `flip` to sort input in order
    :type nums: list[int]
    :rtype: list[int]
    """
    for i in range(len(nums) - 1, -1, -1):
        max_idx = get_max_index(nums, i)
        flip(nums, max_idx + 1)
        flip(nums, i + 1)

    return nums


def get_max_index(nums, i):
    """return the index of the maximum in [0,i] of `nums`
    :type nums: list[int]
    :type i: int
    :rtype: int
    """
    max_idx = 0

    for j in range(1, i + 1):
        if nums[j] > nums[max_idx]:
            max_idx = j

    return max_idx
