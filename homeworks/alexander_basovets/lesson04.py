def reversed2(L):
    x = list([])
    for s in L:
        x.append(s)
        z = x[::-1]
    print(z)


reversed2([44, 2, 3, 4, 5])
