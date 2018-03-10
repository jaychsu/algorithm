"""
Concept:
top-down -> pre-order
1. pick mid_int at middle index
2. swap the ints on either side to ensure
   all the ints on the left side of mid_int
   are LESS THAN all the ints on the right
3. repeat (1), (2) on both sides of the chosen mid_int in above steps

# s: start, e: end, l: left, r: right, m: mid_int
given array: [1, 5, 2, 4, 6, 7, 3]

r1: [1, 5, 2, 4, 6, 7, 3]
    s,l       m       e,r
    [1, 3, 2, 4, 6, 7, 5]
     s     r     l     e

r2: [1, 3, 2, 4, 6, 7, 5]
     s  m1 r     l  m2 e
    [1, 2, 3, 4, 5, 6, 7]
    s,r               e,l
"""


def quick_sort(A):
    _quick_sort(A, 0, len(A) - 1)
    return A


def _quick_sort(A, start, end):
    if start >= end:
        return

    left, right = start, end

    # remember to save mid value in advance
    # since the array is changing all the time
    pivot = A[(start + end) // 2]

    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1

        while left <= right and pivot < A[right]:
            right -= 1

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    _quick_sort(A, start, right)
    _quick_sort(A, left, end)
