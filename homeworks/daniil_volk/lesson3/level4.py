def valid():
    while True:
        try:
            m = int(input())
            n = int(input())
        except ValueError:
            print("Only integer")
            raise
        if m >= 0 and n >= 0:
            break
        print("Only m>= 0 and n>= 0")


def f(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return f(m - 1, 1)
    if m > 0 and n > 0:
        return f(m - 1, f(m, n - 1))
