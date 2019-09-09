from datetime import date as d, timedelta as t


def Reversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    for i in l:
        new_l.insert(0, i)
    return new_l


def Sorted(sample):
    if not sample:
        return sample
    nsample = list(sample)
    left = 0
    right = len(nsample) - 1
    while left <= right:
        for i in range(left, right, +1):
            if nsample[i] > nsample[i + 1]:
                nsample[i], nsample[i + 1] = nsample[i + 1], nsample[i]
        right -= 1

        for i in range(right, left, -1):
            if nsample[i - 1] > nsample[i]:
                nsample[i], nsample[i - 1] = nsample[i - 1], nsample[i]
        left += 1
    return nsample


def Filter(foo, coll):
    r = []
    for c in coll:
        if foo(c):
            r.append(c)
    return r


def TypedReversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    for i in l:
        new_l.insert(0, i)
    if type(l) is str:
        return "".join(new_l)
    elif type(l) is tuple:
        return tuple(new_l)
    else:
        return new_l


def LazyReversed(l):
    if not isinstance(l, (str, tuple, list)):
        return "Введенные данные не соответствуют условию."
    new_l = []
    for i in l:
        new_l.insert(0, i)
    return iter(new_l)
