def Reversed(x):
    if len(x) == 0:
        return []
    new = []
    index = len(x)
    while index:
        index -= 1
        new += [x[index]]
    return new


def Sorted(x):
    x = list(x)
    for j in range(len(x) - 1):
        for i in range(len(x) - j - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    return x


# def Filter(x, y):
#     y = list(y)
#     r = []
#     for i in range(len(y)):
#         if x is y[i]:
#             r.append(x)
#     return r
