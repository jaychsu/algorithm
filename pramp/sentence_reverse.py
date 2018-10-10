"""
Test Case:

>>> gotcha = []
>>> for _in, _out in (
...     ([' ', ' '], [' ', ' ']),
...     (['a', ' ', ' ', 'b'], ['b', ' ', ' ', 'a']),
...     (['h', 'e', 'l', 'l', 'o'], ['h', 'e', 'l', 'l', 'o']),
...     (
...         ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'],
...         ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
...     ),
...     (
...         ['y', 'o', 'u', ' ', 'w', 'i', 't', 'h', ' ', 'b', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 't', 'h', 'e', ' ', 'm', 'a', 'y'],
...         ['m', 'a', 'y', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'y', 'o', 'u']
...     ),
...     (
...         ['g', 'r', 'e', 'a', 't', 'e', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'f', 'i', 'r', 's', 't', ' ', 'e', 'v', 'e', 'r', ' ', 'n', 'a', 'm', 'e', ' ', 'l', 'a', 's', 't'],
...         ['l', 'a', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'e', 'v', 'e', 'r', ' ', 'f', 'i', 'r', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'g', 'r', 'e', 'a', 't', 'e', 's', 't']
...     ),
...     ([' ', ' ', 'a', ' ', 'b', 'c'], ['b', 'c', ' ', 'a', ' ', ' ']),
...     (['b', 'c', ' ', 'a', ' ', ' '], [' ', ' ', 'a', ' ', 'b', 'c']),
...     ([' ', ' ', 'a', ' ', 'b', 'c', ' '], [' ', 'b', 'c', ' ', 'a', ' ', ' ']),
... ):
...     for test_func in (reverse_words, reverse_words2):
...         res = test_func(_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


"""
Approach 1: use built-in function
"""
def reverse_words(arr):
    return list(' '.join(reversed(''.join(arr).split(' '))))


"""
Approach 2: swap children and modify in place
"""
def reverse_words2(arr):
    if not arr:
        return []

    n = len(arr)
    reverse_in_range(arr, 0, n - 1)

    left = 0

    while left < n and arr[left] == ' ':
        left += 1

    for right in range(n):
        if arr[right] != ' ':
            continue

        reverse_in_range(arr, left, right - 1)
        left = right + 1

    right = n - 1

    while right >= 0 and arr[right] == ' ':
        right -= 1

    reverse_in_range(arr, left, right)

    return arr


def reverse_in_range(arr, i, j):
    """
    to reverse arr[i:j + 1]
    """
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
