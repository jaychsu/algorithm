def flatten_dictionary(dictionary):
    ans = {}

    if not dictionary:
        return ans

    dfs(dictionary, [], ans)
    return ans


def dfs(dictionary, keys, ans):
    if not isinstance(dictionary, dict):
        key = '.'.join(keys)
        ans[key] = dictionary
        return

    for key in dictionary:
        if key:
            keys.append(key)

        dfs(dictionary[key], keys, ans)

        if key:
            keys.pop()
