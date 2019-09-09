def Reversed(x):
    y = []
    for i in x:
        y.insert(0, i)
    return y





def Sorted(x):
    r = []
    for i in x:
        for n in x:
            if i <=n:
                r.append(n)
    return r








