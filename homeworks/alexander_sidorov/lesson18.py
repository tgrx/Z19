from decimal import Decimal


def count_pnz(numbers):
    p = n = z = 0
    N = Decimal(len(numbers))

    for i in numbers:
        p += i > 0
        n += i < 0
        z += i == 0

    return tuple(f"{(x / N if N else 0):.6f}" for x in (p, n, z))
