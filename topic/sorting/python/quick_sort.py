from sorting.python._helper import *


class QuickSort(SortBase):
    """
    remember to save pivot value in advance
    since the array is changing all the time
    """

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
        cls._divide_conquer(res, 0, n - 1)
        return res

    @classmethod
    def _divide_conquer(cls, arr, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = arr[(start + end) // 2]

        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        cls._divide_conquer(arr, start, right)
        cls._divide_conquer(arr, left, end)
