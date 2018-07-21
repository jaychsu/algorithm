from sorting.python._helper import *


class MergeSort(SortBase):
    @classmethod
    def sort(cls, iterable):
        """
        :type iterable: Iterable
        :rtype: list
        """
        if not cls._is_valid_payload(iterable):
            return []

        res = list(iterable)
        n = len(iterable)
        cls._divide_conquer(res, 0, n - 1, [None] * n)
        return res

    @classmethod
    def _divide_conquer(cls, arr, start, end, tmp):
        if start >= end:
            return

        mid = (start + end) // 2
        left, right = start, mid + 1
        cls._divide_conquer(arr, left, mid, tmp)
        cls._divide_conquer(arr, right, end, tmp)

        idx = start

        while left <= mid and right <= end:
            if arr[left] < arr[right]:
                tmp[idx] = arr[left]
                left += 1
            else:
                tmp[idx] = arr[right]
                right += 1
            idx += 1

        while left <= mid:
            tmp[idx] = arr[left]
            left += 1
            idx += 1

        while right <= end:
            tmp[idx] = arr[right]
            right += 1
            idx += 1

        for idx in range(start, end + 1):
            arr[idx] = tmp[idx]
