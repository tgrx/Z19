def verification(start, ending):
    while True:
        try:
            a = int(input())
        except ValueError:
            continue
        else:
            if a in range(start, ending + 1):
                return a
