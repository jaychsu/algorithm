def calc_drone_min_energy(route):
    ans = 0

    if not route or len(route) < 2:
        return ans

    delta = 0
    max_z = route[0][2]

    for i in range(1, len(route)):
        delta += route[i][2] - route[i - 1][2]

        if route[i][2] > max_z:
            max_z = route[i][2]
            ans = delta

    return ans
