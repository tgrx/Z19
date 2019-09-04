def akkerman_func(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akkerman_func(m - 1, 1)
    if m > 0 and n > 0:
        return akkerman_func(m - 1, akkerman_func(m, n - 1))
