def Reversed(x):
    if len(x) == 0:
        return []
    new = []
    index = len(x)
    while index:
        index -= 1
        new += [x[index]]
    return new
