import platform


def choice_func():
    while True:
        try:
            choice = int(input("Input your choice."))
            if choice == 1:
                first_task()
            elif choice == 2:
                second_task()
            elif choice == 3:
                third_task()
            elif choice == 4:
                fourth_task()
            elif choice == 5:
                fifth_task()
            elif choice == 6:
                six_task()
            else:
                print("Error.")
                continue
        except ValueError:
            print("Input right number.")
            continue


def first_task():
    print("Hello, world!")


def second_task():
    print(f"Information about user: {name} {surname}, {age} years old.")


def third_task():
    print(f"Platform: {platform.platform()}")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")


def fourth_task():
    print(f"Hello,{name}")


def fifth_task():
    while True:
        try:
            option = int(
                input(
                    "Choose the option: 1)'a cup of coffee' or 2)'a cup of tea' or 3)'rumka vodki na stole'"
                )
            )
            if option == 1:
                print("You have chosen a cup of coffee.")
                break
            elif option == 2:
                print("Your choice is a cup of tea.")
                break
            elif option == 3:
                print("Oh, it's OK, you're not an alcoholic:)")
                break
            else:
                print("Wrong number!")
                continue
        except ValueError:
            print("Input the number.")
            continue


def six_task():
    while True:
        try:
            year = int(input("Input the year - "))
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                print(f"The year  is not a leap year.")
                break
            else:
                print(f"The year {year} is a leap year.")
                break
        except ValueError:
            print("Error.")
            continue


name = input("Input your name - ")
surname = input("Input your surname - ")
while True:
    try:
        age = int(input("Input your age - "))
        if type(age) == int:
            break
    except ValueError:
        print("Wrong age! Try one more time")
        continue
choice_func()
