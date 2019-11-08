def count_pnz(a):
    p = 1 / len(a)
    r = [0, 0, 0]
    for e in a:
        if e > 0:
            r[0] += p
        if e < 0:
            r[1] += p
        if e == 0:
            r[2] += p
    return tuple("{0:.6f}".format(e) for e in r)
