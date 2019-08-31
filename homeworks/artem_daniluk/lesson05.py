def Reversed(coll):
    coll = list(coll)
    rev_coll = []
    for i in range(len(coll) - 1, -1, -1):
        rev_coll.append(coll[i])
    return rev_coll


def Sorted(col):
    r = list(col)
    for i in range(len(col) - 1):
        for j in range(len(col) - i - 1):
            if r[j] > r[j + 1]:
                t = r[j]
                r[i] = r[j + 1]
                r[j + 1] = t
    return r


def Filter(p, col):
    col = list(col)
    r = []
    for i in range(len(col)):
        if p(col[i]):
            r.append(col[i])
    return r


def TypedReversed(coll):
    t = type(coll)
    coll = list(coll)
    rev_coll = []
    for i in range(len(coll) - 1, -1, -1):
        rev_coll.append(coll[i])
    if t == str:
        rev_coll = ''.join(rev_coll)
    else:
        rev_coll = t(rev_coll)
    return rev_coll
