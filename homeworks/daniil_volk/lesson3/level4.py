def valid():
    while True:
        try:
            m = int(input())
            n = int(input())
        except ValueError:
            raise ValueError
        if m >= 0 and n >= 0:
            break
        raise ValueError


def f(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return f(m - 1, 1)
    if m > 0 and n > 0:
        return f(m - 1, f(m, n - 1))
