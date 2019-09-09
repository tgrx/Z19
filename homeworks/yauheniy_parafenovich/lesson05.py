def Reversed(y):
    new = ""
    index = len(y)
    while index:
        index = index -1
        new = new + y[index]
    return new
print(Reversed("саша"))
