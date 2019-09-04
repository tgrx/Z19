def a(m, n):
    if m < 0 or n < 0:
        return "Input values less than zero"

    if m == 0:
        return n + 1
    elif n == 0:
        return a(m - 1, 1)
    else:
        return a(m - 1, a(m, n - 1))


for i in range(0, 10):
    for j in range(0, 10):
        try:
            a(i, j)
            print("Pass: m = {m}, n = {n}".format(m=i, n=j))
        except RecursionError:
            print("Error: m = {m}, n = {n}".format(m=i, n=j))
