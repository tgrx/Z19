def Reversed(x):
    r = []
    for i in x:
        r.insert(0, i)
    return r

def Sorted(x):
    r = []
    for i in x:
        for n in x:
            if i <= n+1:
                r.append(i)
        return r


def Filter(x, y):
    z = []
    for i in y:
        if x == i:
            z.append(i)
    return z

def TypedReversed(x):
    r = []
    for i in x:
        if type(x) == type(r):
            r.insert(0, i)
        else:
            print("TypeError")
        return r

def Range(x):
    r = []
    if x:
        x = 