def find_busiest_period(data):
    timestamp = -1

    if not data:
        return timestamp
    if len(data) == 1: # data[0][2] always 1
        return data[0][0]

    n = len(data)
    cnt = maxi = 0

    for i in range(len(data)):
        if data[i][2] == 1:
            cnt += data[i][1]
        else:
            cnt -= data[i][1]

        if (i == n - 1 or data[i][0] != data[i + 1][0]) and cnt > maxi:
            maxi = cnt
            timestamp = data[i][0]

    return timestamp
