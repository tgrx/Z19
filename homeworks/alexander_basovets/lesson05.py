def Reversed(L):
    # S = list(L)
    M = []
    for i in L:
        #   c = 0
        M.insert(0, i)
    return M


def Sorted(r):
    S = list(r)
    x = len(r) - 1
    c = len(r) - 1
    while x > 0:
        i = 0
        while c > 0:
            if S[i] > S[i + 1]:
                S[i], S[i + 1] = S[i + 1], S[i]
            i = i + 1
            c = c - 1
        x = x - 1
        c = x
    return S


def TypedReversed(L):
    M = []
    for i in L:
        #   c = 0
        M.insert(0, i)
    if type(L) is list:
        return M
    if type(L) is tuple:
        return tuple(M)
    if type(L) is str:
        return "".join(M)
