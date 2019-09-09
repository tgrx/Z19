def Reversed(x):
    if not x:
        return x == []
    new = ""
    index = len(x)
    while index:
        index -= 1
        new += x[index]
    return new
