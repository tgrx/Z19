n = int(input('Введите первое число: '))
m = int(input("Введите второе число: "))


def func(n, m):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return func(m - 1, 1)
    if m > 0 and n > 0:
        return func(m - 1, func(m, n - 1))
