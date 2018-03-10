"""
Concept:
bottom-up -> post-order
1. pick mid_int at middle index
2. continue to compare the first int on either side,
   push the smaller one to the tmp,
   that is, 2-way merge sort
3. override origin array by the corresponding int in tmp
4. step up to a larder scale and repeat (1), (2)

# the ints in the same section will sort first
given array: [1, 5, 2, 4, 6, 7, 3]

r1: [1, 5, 2, 4, 6, 7, 3]
         |     |     |

r2: [1, 2, 4, 5, 3, 6, 7]
               |

r3: [1, 2, 3, 4, 5, 6, 7]
"""


def merge_sort(A):
    n = len(A)
    tmp = [0] * n
    _merge_sort(A, 0, n - 1, tmp)
    return A


def _merge_sort(A, start, end, tmp):
    if start >= end:
        return

    mid = (start + end) // 2
    left, right = start, mid + 1
    _merge_sort(A, left, mid, tmp)
    _merge_sort(A, right, end, tmp)

    index = start

    while left <= mid and right <= end:
        if A[left] < A[right]:
            tmp[index] = A[left]
            left += 1
        else:
            tmp[index] = A[right]
            right += 1
        index += 1

    while left <= mid:
        tmp[index] = A[left]
        left += 1
        index += 1

    while right <= end:
        tmp[index] = A[right]
        right += 1
        index += 1

    for index in range(start, end + 1):
        A[index] = tmp[index]
