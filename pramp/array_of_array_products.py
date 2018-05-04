"""
thought:
=> nums = [a, b, c, d]
1. fill `ans` with `1`
=> ans = [1, 1, 1, 1]
2. scan from left to right, and do multiply continuously
=> ans = [1, a, a * b, a * b * c]
3. scan from right to left, and do multiply continuously but with a temp var
=> prod = b * c * d,  c * d,  d
=> ans = [b * c * d, a * c * d, a * b * d, a * b * c]
"""


def array_of_array_products(nums):
    """
    :type nums: list[int]
    :rtype: list[int]
    """
    if not nums or len(nums) <= 1:
        return []

    n = len(nums)
    ans = [1] * n

    # 1st scan [1, a, a * b, a * b * c]
    for i in range(1, n):
        ans[i] *= ans[i - 1] * nums[i - 1]

    # 2nd scan
    prod = 1
    for i in range(n - 2, -1, -1):
        prod *= nums[i + 1]
        ans[i] *= prod

    return ans
