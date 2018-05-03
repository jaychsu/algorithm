def index_equals_value_search(nums):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if nums[left] == left:  # lowest index
            return left
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            left = mid
        else:
            right = mid

    for mid in (left, right):
        if nums[mid] == mid:
            return mid

    return -1
