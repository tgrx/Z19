def count_pnz(massive):
    empty = ("0.000000", "0.000000", "0.000000")
    if not massive:
        return empty

    output = []
    total = len(massive)
    minus, plus, zero = 0, 0, 0

    for i in massive:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1

    share_plus = "{:.6f}".format(plus / total)
    share_minus = "{:.6f}".format(minus / total)
    share_zero = "{:.6f}".format(zero / total)

    output.append(str(share_plus))
    output.append(str(share_minus))
    output.append(str(share_zero))

    return tuple(output)
