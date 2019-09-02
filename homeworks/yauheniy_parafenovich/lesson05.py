# def reversed2(L):
#    x = list([])
#   for s in L:
#      x.append(s)
#     z = x[::-1]
# print(z)  # функция реверса


def sorted(a):
    n = len(a)
    count = 0
    b = [1]
    i = 1
    while count < n:
        if a[0] > a[i]:
            b[0] = a[0]
            print(b)
        else:
            print(a)
        count = count + 1
    i = i + 1


# sorted((13, 6, 5, 4))

sorted((5, 3, 4, 2, 1))
