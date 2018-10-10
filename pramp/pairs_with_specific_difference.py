def find_pairs_with_given_difference(arr, k):
    ans = []

    if not arr or not isinstance(k, int):
        return ans

    n = len(arr)
    sums = {}

    for i in range(n):
        sums[arr[i] - k] = i

    for j in range(n):
        if arr[j] in sums:
            i = sums[arr[j]]
            ans.append([arr[i], arr[j]])

    return ans
