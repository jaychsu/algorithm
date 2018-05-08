"""
Approach 1: use built-in function
"""
def reverse_words(arr):
    return list(' '.join(reversed(''.join(arr).split(' '))))


"""
Approach 2: swap children and modify in place
"""
def reverse_words(arr):
    if not arr:
        return []

    n = len(arr)
    reverse_in_range(arr, 0, n - 1)

    left = 0

    for right in range(n):
        if arr[right] != ' ':
            continue

        reverse_in_range(arr, left, right - 1)
        left = right + 1

    reverse_in_range(arr, left, n - 1)

    return arr


def reverse_in_range(arr, i, j):
    """
    to reverse arr[i:j + 1]
    """
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
