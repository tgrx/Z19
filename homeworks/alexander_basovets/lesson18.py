def count_pnz(x):
    y = len(x) - 1
    s = len(x)
    i = 0
    a = 0
    b = 0
    c = 0
    d = [""]
    if x != []:
        while i <= y:
            if x[i] > 0:
                a += 1
            elif x[i] < 0:
                b += 1
            else:
                c += 1
            i += 1
        af = a / s
        bf = b / s
        cf = c / s
        d[0] = format(af, ".6f")
        d.append(format(bf, ".6f"))
        d.append(format(cf, ".6f"))
        m = tuple(d)
    else:
        m = tuple(d)
    return m
