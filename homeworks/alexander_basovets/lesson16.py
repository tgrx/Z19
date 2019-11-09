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
    f = "".join(zp)
    return f


