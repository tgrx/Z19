def count_pnz(m):
    if not m:
        return ('0.000000', '0.000000', '0.000000')
    d = {">": 0, "<": 0, "=": 0}
    for x in m:
        if x > 0:
            d[">"] += 1
        elif x < 0:
            d["<"] += 1
        elif x == 0:
            d["="] += 1
    res = []
    res.append(format(d.get(">") / len(m), ".6f"))
    res.append(format(d.get("<") / len(m), ".6f"))
    res.append(format(d.get("=") / len(m), ".6f"))
    return tuple(res)
