import heapq


def sort_k_messed_array(nums, k):
    """
    Given an array of integers arr where each element is at most k places away from its sorted position.

    time: O(n * log(k))
    space: O(k)
    """
    if not nums or not k:
        return nums

    n = len(nums)
    heap = []

    for i in range(k + 1):
        heapq.heappush(heap, nums[i])

    for i in range(k + 1, n):
        nums[i - k - 1] = heapq.heappop(heap)
        heapq.heappush(heap, nums[i])

    for i in range(n - k - 1, n):
        nums[i] = heapq.heappop(heap)

    return nums
