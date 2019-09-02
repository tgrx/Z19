def verification(start, ending):
    while True:
        try:
            a = int(input())
        except ValueError:
            print("Variant is not an integer!")
            continue
        else:
            if a in range(start, ending + 1):
                print("Variant is available!")
                return a
            print(f"Variant is not {start} - {ending}!")
