def find_duplicates(arr1, arr2):
    ans = []

    if not arr1 or not arr2:
        return ans

    m, n = len(arr1), len(arr2)
    i = j = 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not ans or arr1[i] != ans[-1]:
                ans.append(arr1[i])
            i += 1
            j += 1

    return ans


def find_duplicates2(arr1, arr2):
    ans = []

    if not arr1 or not arr2:
        return ans

    vals = {}

    for num in arr1:
        vals[num] = False

    for num in arr2:
        if num in vals and vals[num] is False:
            vals[num] = True
            ans.append(num)

    return ans


def find_duplicates3(arr1, arr2):
    if not arr1 or not arr2:
        return []

    val1 = set(arr1)
    val2 = set(arr2)

    return list(val1 & val2)


if __name__ == '__main__':
    print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
    print(find_duplicates2([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates2([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
    print(find_duplicates3([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
    print(find_duplicates3([1, 2, 3, 3, 5, 6, 7], [3, 3, 6, 7, 8, 20]))
