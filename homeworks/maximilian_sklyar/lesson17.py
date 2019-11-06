def compare_triplets(a, b):
    r = [0, 0]
    for z in zip(a, b):
        if z[0] > z[1]:
            r[0] += 1
        if z[0] < z[1]:
            r[1] += 1
    return tuple(r)
