def find_busiest_period(data):
    n = len(data)
    cnt = 0
    max_cnt = 0
    max_time = float('-inf')

    for i in range(n):
        timestamp, people, status = data[i]

        if status == 1:
            cnt += people
        else:
            cnt -= people

        if i + 1 < n and data[i][0] == data[i + 1][0]:
            continue

        if cnt > max_cnt:
            max_cnt = cnt
            max_time = timestamp

    return max_time
