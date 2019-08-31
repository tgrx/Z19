def verification():
    print('Hello!')
    while True:
        try:
            a = int(input("Enter your variant (1-6): "))
        except ValueError:
            print("Variant is not an integer!")
            continue
        else:
            if a in [1, 2, 3, 4, 5, 6]:
                print("Variant is available!")
                return(a)
            else:
                print("Variant is not 1-6!")
