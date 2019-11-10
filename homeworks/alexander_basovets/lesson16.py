def Zip(text: str) -> str:
    z = len(text)
    s = 0
    count = 0
    num = 0
    m = ""
    zp = []
    i = 1
    while i <= z:
        if text[s] == text[count]:
            count += 1
            num += 1
            m = text[s] + str(num)
            i += 1
        else:
            s = count
            num = 0
            zp.append(m)
    zp.append(m)
    v = "".join(zp)
    return v


def Unzip(text: str) -> str:
    z = int(len(text) / 2)
    s = text
    zp = []
    a = 0
    b = 1
    i = 1
    c = 0
    while i <= z:
        p = s[b]
        m = s[a]
        w = m * float(p)
        zp.append(w)
        a += 2
        b += 2
        i += 1
        c += 1
    v = "".join(zp)

    return v


