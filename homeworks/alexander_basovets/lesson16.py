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
    l = len(text)
    s = text
    zp = []
    i = 0
    p = ""
    while i < l:
        f = s[i]
        if f.isnumeric():
            s_int = ""
            t = i
            while "0" <= f <= "9":
                s_int += f
                t += 1
                i = t - 1
                if t < l:
                    f = s[t]

                else:
                    break
            m = int(s_int)
            w = p * (m - 1)
            zp.append(w)
        else:
            p = s[i]
            zp.append(p)
        i += 1
    v = "".join(zp)
    return v
