def meeting_planner(slots1, slots2, duration):
    if not slots1 or not slots2 or not duration:
        return []

    m, n = len(slots1), len(slots2)
    i = j = 0

    while i < m and j < n:
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])

        if start + duration <= end:
            return [start, start + duration]

        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1

    return []
