while True:
    try:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))
    except ValueError:
        print("Variant is not an integer!")
        continue
    else:
        if m >= 0 and n >= 0:
            print("m and n is available!")
            break
        else:
            print("Your entered numbers are not positive numbers! ")


def f(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return f(m - 1, 1)
    if m > 0 and n > 0:
        return f(m - 1, f(m, n - 1))


print(f(m, n))  # my ubuntu has died again when i enter m=4 and n=1
