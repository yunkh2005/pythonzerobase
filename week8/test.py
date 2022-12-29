data = [(10, 10), (20, 10), (25, 8), (30, 5), (15, 12)]

def get_max(data, capacity):
    data = sorted(data, key=lambda x: x[1] / x[0], reverse=True)
    total = 0
    detail = list()

    for dt in data:
        if capacity - dt[0] >= 0:
            capacity -= dt[0]
            total += dt[1]
            detail.append([dt[0], dt[1], 1])
        else:
            fraction = capacity / dt[0]
            total += dt[1] * fraction
            detail.append([dt[0], dt[1], fraction])
            break

    return total, detail

print(get_max(data, 30))