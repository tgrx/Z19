def verification():
    while True:
        try:
            a = int(input("Enter your variant (1-6): "))
        except ValueError:
            print("Variant is not an integer!")
            continue
        else:
            if a in range(1,7):
                print("Variant is available!")
                return a
            print("Variant is not 1-6!")
